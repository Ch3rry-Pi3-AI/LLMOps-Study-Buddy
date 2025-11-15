"""
helpers.py

Utility helpers and quiz management logic for the LLMOps StudyBuddy project.

This module provides:
- A `rerun` helper for triggering Streamlit app reruns via session state.
- A `QuizManager` class for generating, presenting, and evaluating quizzes
  built from LLM-generated questions.
"""

# --------------------------------------------------------------
# Imports
# --------------------------------------------------------------
from __future__ import annotations

import os
from datetime import datetime
from typing import Any, List, Optional

import pandas as pd
import streamlit as st

from src.generator.question_generator import QuestionGenerator


# --------------------------------------------------------------
# Streamlit Helpers
# --------------------------------------------------------------
def rerun() -> None:
    """
    Toggle a session-state flag to trigger a Streamlit rerun.

    This helper flips a boolean value in `st.session_state` under the key
    'rerun_trigger'. It can be used in callbacks to force the app to refresh.
    """
    # Flip the rerun trigger flag in session state
    st.session_state["rerun_trigger"] = not st.session_state.get(
        "rerun_trigger",
        False,
    )


# --------------------------------------------------------------
# Quiz Management
# --------------------------------------------------------------
class QuizManager:
    """
    Manage quiz generation, user interaction, evaluation, and persistence.

    This class coordinates:
    - Question generation via `QuestionGenerator`
    - Interactive question display using Streamlit
    - Answer collection and scoring
    - Export of results to a CSV file

    Attributes
    ----------
    questions : list of dict
        The list of generated questions in a simple serialisable format.
    user_answers : list of str
        The user's answers in the order questions were presented.
    results : list of dict
        Evaluation records including correctness, question text, and user answer.
    """

    def __init__(self) -> None:
        """Initialise an empty quiz state."""
        # Stores generated questions and metadata
        self.questions: List[dict[str, Any]] = []

        # Stores user answers captured via the UI
        self.user_answers: List[str] = []

        # Stores evaluation results after marking
        self.results: List[dict[str, Any]] = []

    def generate_questions(
        self,
        generator: QuestionGenerator,
        topic: str,
        question_type: str,
        difficulty: str,
        num_questions: int,
    ) -> bool:
        """
        Generate a batch of unique questions using the provided QuestionGenerator.

        This method:
        - Resets the current quiz state
        - Calls the LLM-backed generator repeatedly
        - Rejects duplicate question texts and retries a few times
        - Populates `self.questions` with only unique questions

        Parameters
        ----------
        generator : QuestionGenerator
            The question generator service used to query the LLM.
        topic : str
            The topic the questions should focus on.
        question_type : str
            The question type, e.g. 'Multiple Choice' or 'Fill in the blank'.
        difficulty : str
            Difficulty level (e.g. 'Easy', 'Medium', 'Hard').
        num_questions : int
            Number of questions to generate.

        Returns
        -------
        bool
            True if at least one question is generated successfully.
            False if generation fails entirely.
        """
        # Reset internal quiz state for a new quiz
        self.questions = []
        self.user_answers = []
        self.results = []

        # Track seen question texts to avoid duplicates (case-insensitive)
        seen_questions: set[str] = set()

        # Limit how many times we will retry per requested question
        max_attempts_per_question = 5

        try:
            for _ in range(num_questions):
                attempts = 0
                unique_question_added = False

                while attempts < max_attempts_per_question and not unique_question_added:
                    attempts += 1

                    if question_type == "Multiple Choice":
                        # Generate a multiple-choice question
                        question = generator.generate_mcq(topic, difficulty.lower())

                        question_text = question.question.strip().lower()

                        # Skip duplicates
                        if question_text in seen_questions:
                            continue

                        # Accept this question
                        seen_questions.add(question_text)
                        self.questions.append(
                            {
                                "type": "MCQ",
                                "question": question.question,
                                "options": question.options,
                                "correct_answer": question.correct_answer,
                            }
                        )
                        unique_question_added = True

                    else:
                        # Generate a fill-in-the-blank question
                        question = generator.generate_fill_blank(
                            topic,
                            difficulty.lower(),
                        )

                        question_text = question.question.strip().lower()

                        # Skip duplicates
                        if question_text in seen_questions:
                            continue

                        # Accept this question
                        seen_questions.add(question_text)
                        self.questions.append(
                            {
                                "type": "Fill in the blank",
                                "question": question.question,
                                "correct_answer": question.answer,
                            }
                        )
                        unique_question_added = True

                # If we could not get a unique question after several attempts,
                # stop trying to generate more for this run.
                if not unique_question_added:
                    st.warning(
                        "Could not generate enough unique questions for this topic. "
                        "The quiz will contain fewer questions than requested."
                    )
                    break

        except Exception as exc:
            st.error(f"Error generating questions: {exc}")
            return False

        # Return True if we managed to generate at least one question
        if not self.questions:
            st.error("No questions were generated.")
            return False

        return True


    def attempt_quiz(self) -> None:
        """
        Render the quiz interface in Streamlit and capture user answers.

        This method uses Streamlit widgets (radio buttons and text inputs)
        to present each question and collect the user's response.

        It rebuilds `self.user_answers` on every run so that Streamlit's
        rerun behaviour does not accumulate stale or duplicate answers.
        """
        # Always rebuild answers from the current UI state
        self.user_answers = []

        for i, q in enumerate(self.questions):
            # Display question text
            st.markdown(f"**Question {i + 1}: {q['question']}**")

            if q["type"] == "MCQ":
                # Multiple-choice selection widget
                user_answer = st.radio(
                    f"Select an answer for Question {i + 1}",
                    q["options"],
                    key=f"mcq_{i}",
                )
                self.user_answers.append(user_answer)
            else:
                # Free-text fill-in-the-blank widget
                user_answer = st.text_input(
                    f"Fill in the blank for Question {i + 1}",
                    key=f"fill_blank_{i}",
                )
                self.user_answers.append(user_answer)

    def evaluate_quiz(self) -> None:
        """
        Evaluate the quiz by comparing user answers against correct answers.

        Populates `self.results` with per-question evaluation details such as:
        - question number
        - question text
        - question type
        - user answer
        - correct answer
        - correctness flag
        - options (if applicable)
        """
        # Reset previous evaluation results
        self.results = []

        for i, (q, user_ans) in enumerate(zip(self.questions, self.user_answers)):
            # Base result record for each question
            result_dict: dict[str, Any] = {
                "question_number": i + 1,
                "question": q["question"],
                "question_type": q["type"],
                "user_answer": user_ans,
                "correct_answer": q["correct_answer"],
                "is_correct": False,
            }

            if q["type"] == "MCQ":
                # For MCQs, store options and compare directly
                result_dict["options"] = q["options"]
                result_dict["is_correct"] = user_ans == q["correct_answer"]
            else:
                # For fill-in-the-blank, normalise case and whitespace
                result_dict["options"] = []
                result_dict["is_correct"] = (
                    user_ans.strip().lower()
                    == q["correct_answer"].strip().lower()
                )

            self.results.append(result_dict)

    def generate_result_dataframe(self) -> pd.DataFrame:
        """
        Convert the quiz results into a pandas DataFrame.

        Returns
        -------
        pandas.DataFrame
            A DataFrame containing one row per question result. Returns an
            empty DataFrame if no results are available.
        """
        # Return an empty DataFrame if there are no results yet
        if not self.results:
            return pd.DataFrame()

        return pd.DataFrame(self.results)

    def save_to_csv(self, filename_prefix: str = "quiz_results") -> Optional[str]:
        """
        Save quiz results to a timestamped CSV file in a `results/` directory.

        Parameters
        ----------
        filename_prefix : str, optional
            Prefix for the generated CSV filename, by default 'quiz_results'.

        Returns
        -------
        str or None
            The full path to the saved CSV file, or None if saving fails
            or there are no results to save.
        """
        # Warn if called before results are available
        if not self.results:
            st.warning("No results to save.")
            return None

        # Build a DataFrame from current results
        df = self.generate_result_dataframe()

        # Create a unique timestamped filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        unique_filename = f"{filename_prefix}_{timestamp}.csv"

        # Ensure the output directory exists
        os.makedirs("results", exist_ok=True)
        full_path = os.path.join("results", unique_filename)

        try:
            # Write DataFrame to CSV without the index column
            df.to_csv(full_path, index=False)
            st.success("Results saved successfully.")
            return full_path
        except Exception as exc:
            # Handle and display any file I/O errors
            st.error(f"Failed to save results: {exc}")
            return None
