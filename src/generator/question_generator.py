"""
question_generator.py

Service module for generating structured study questions in the
LLMOps StudyBuddy project.

This module uses:
- LangChain `PromptTemplate` objects,
- Groq's `ChatGroq` LLM client,
- Pydantic models for MCQ and fill-in-the-blank questions,

to produce validated question objects with controlled retries and
robust logging.
"""

# --------------------------------------------------------------
# Imports
# --------------------------------------------------------------
from __future__ import annotations

from typing import Any

from langchain.output_parsers import PydanticOutputParser
from src.models.question_schemas import MCQQuestion, FillBlankQuestion
from src.prompts.templates import mcq_prompt_template, fill_blank_prompt_template
from src.llm.groq_client import get_groq_llm
from src.config.settings import settings
from src.common.logger import get_logger
from src.common.custom_exception import CustomException


# --------------------------------------------------------------
# Question Generation Service
# --------------------------------------------------------------
class QuestionGenerator:
    """
    Service class for generating validated study questions.

    This class wraps the Groq LLM client, LangChain prompt templates,
    and Pydantic output parsers to produce structured MCQ and
    fill-in-the-blank questions. It includes retry logic and logging
    for reliability.

    Attributes
    ----------
    llm : ChatGroq
        Configured Groq chat model used to generate questions.
    logger : logging.Logger
        Logger instance used for informational and error messages.
    """

    def __init__(self) -> None:
        """Initialise the question generator with LLM client and logger."""
        # Groq LLM client configured via global settings
        self.llm = get_groq_llm()

        # Logger scoped to this class
        self.logger = get_logger(self.__class__.__name__)

    # Internal helper to handle retries and Pydantic parsing
    def _retry_and_parse(
        self,
        prompt: Any,
        parser: PydanticOutputParser,
        topic: str,
        difficulty: str,
    ) -> Any:
        """
        Attempt to generate and parse a question with retry logic.

        Parameters
        ----------
        prompt : Any
            A LangChain prompt object supporting `.format(...)`.
        parser : PydanticOutputParser
            Parser to convert raw LLM output into a Pydantic model.
        topic : str
            Topic the question should be about.
        difficulty : str
            Difficulty level (e.g. 'easy', 'medium', 'hard').

        Returns
        -------
        Any
            Parsed Pydantic model instance (e.g. MCQQuestion or FillBlankQuestion).

        Raises
        ------
        CustomException
            If generation or parsing fails after the maximum number of retries.
        """
        for attempt in range(settings.MAX_RETRIES):
            try:
                # Log the current generation attempt
                self.logger.info(
                    "Generating question for topic '%s' at difficulty '%s' (attempt %d/%d)",
                    topic,
                    difficulty,
                    attempt + 1,
                    settings.MAX_RETRIES,
                )

                # Format the prompt with the provided topic and difficulty
                formatted_prompt = prompt.format(topic=topic, difficulty=difficulty)

                # Invoke the LLM with the formatted prompt
                response = self.llm.invoke(formatted_prompt)

                # Parse the response into the target Pydantic model
                parsed = parser.parse(response.content)

                self.logger.info("Successfully parsed the question response.")
                return parsed

            except Exception as exc:
                # Log the error and either retry or escalate as a CustomException
                self.logger.error("Error during question generation: %s", str(exc))
                if attempt == settings.MAX_RETRIES - 1:
                    raise CustomException(
                        f"Generation failed after {settings.MAX_RETRIES} attempts",
                        exc,
                    )

    def generate_mcq(self, topic: str, difficulty: str = "medium") -> MCQQuestion:
        """
        Generate a multiple-choice question (MCQ).

        Parameters
        ----------
        topic : str
            Topic the question should focus on.
        difficulty : str, optional
            Desired difficulty level, by default 'medium'.

        Returns
        -------
        MCQQuestion
            A validated multiple-choice question object.

        Raises
        ------
        CustomException
            If generation or validation of the MCQ fails.
        """
        try:
            # Output parser configured for the MCQQuestion schema
            parser = PydanticOutputParser(pydantic_object=MCQQuestion)

            # Call helper to generate and parse the MCQ
            question: MCQQuestion = self._retry_and_parse(
                mcq_prompt_template,
                parser,
                topic,
                difficulty,
            )

            # Sanity checks on MCQ structure
            if len(question.options) != 4 or question.correct_answer not in question.options:
                raise ValueError("Invalid MCQ structure: options must be 4 and include the correct answer.")

            self.logger.info("Generated a valid MCQ question.")
            return question

        except Exception as exc:
            self.logger.error("Failed to generate MCQ: %s", str(exc))
            raise CustomException("MCQ generation failed", exc)

    def generate_fill_blank(
        self,
        topic: str,
        difficulty: str = "medium",
    ) -> FillBlankQuestion:
        """
        Generate a fill-in-the-blank question.

        Parameters
        ----------
        topic : str
            Topic the question should focus on.
        difficulty : str, optional
            Desired difficulty level, by default 'medium'.

        Returns
        -------
        FillBlankQuestion
            A validated fill-in-the-blank question object.

        Raises
        ------
        CustomException
            If generation or validation of the fill-in-the-blank question fails.
        """
        try:
            # Output parser configured for the FillBlankQuestion schema
            parser = PydanticOutputParser(pydantic_object=FillBlankQuestion)

            # Call helper to generate and parse the fill-in-the-blank question
            question: FillBlankQuestion = self._retry_and_parse(
                fill_blank_prompt_template,
                parser,
                topic,
                difficulty,
            )

            # Ensure the placeholder is present in the question text
            if "___" not in question.question:
                raise ValueError("Fill-in-the-blank questions must contain '___' in the question text.")

            self.logger.info("Generated a valid fill-in-the-blank question.")
            return question

        except Exception as exc:
            self.logger.error("Failed to generate fill-in-the-blank question: %s", str(exc))
            raise CustomException("Fill-in-the-blank generation failed", exc)
