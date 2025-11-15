"""
question_generator.py

High-level question generation service for the LLMOps StudyBuddy project.

This module provides the `QuestionGenerator` class, which:
- Uses LangChain prompt templates and the Groq Chat model
- Parses outputs into Pydantic models
- Retries on failure, with logging and structured error handling
"""

# --------------------------------------------------------------
# Imports
# --------------------------------------------------------------
from __future__ import annotations

from typing import Any

from langchain_core.output_parsers import PydanticOutputParser
from src.models.question_schemas import MCQQuestion, FillBlankQuestion
from src.prompts.templates import mcq_prompt_template, fill_blank_prompt_template
from src.llm.groq_client import get_groq_llm
from src.config.settings import settings
from src.common.logger import get_logger
from src.common.custom_exception import CustomException


# --------------------------------------------------------------
# Question Generator
# --------------------------------------------------------------
class QuestionGenerator:
    """
    Service for generating validated study questions via the Groq LLM.

    This class orchestrates:
    - Prompt templates
    - Groq Chat model
    - Pydantic output parsing
    - Retry logic
    - Logging

    Methods
    -------
    generate_mcq(topic, difficulty)
        Generate a structured multiple-choice question.
    generate_fill_blank(topic, difficulty)
        Generate a structured fill-in-the-blank question.
    """

    def __init__(self) -> None:
        """Initialise the generator with an LLM client and logger."""
        # Groq chat model client
        self.llm = get_groq_llm()

        # Module-level logger
        self.logger = get_logger(self.__class__.__name__)

    def _retry_and_parse(
        self,
        prompt,
        parser: PydanticOutputParser,
        topic: str,
        difficulty: str,
    ) -> Any:
        """
        Execute the LLM with retry logic and parse the output.

        Parameters
        ----------
        prompt
            LangChain PromptTemplate used to format the request.
        parser : PydanticOutputParser
            Output parser bound to the target Pydantic model.
        topic : str
            Topic for question generation.
        difficulty : str
            Difficulty level (e.g. 'easy', 'medium', 'hard').

        Returns
        -------
        Any
            Parsed Pydantic model instance.

        Raises
        ------
        CustomException
            If generation fails after the configured number of retries.
        """
        for attempt in range(settings.MAX_RETRIES):
            try:
                self.logger.info(
                    f"Generating question for topic='{topic}', "
                    f"difficulty='{difficulty}', attempt={attempt + 1}"
                )

                # Format the prompt and call the LLM
                formatted_prompt = prompt.format(
                    topic=topic,
                    difficulty=difficulty,
                )
                response = self.llm.invoke(formatted_prompt)

                # Parse LLM output into a Pydantic model
                parsed = parser.parse(response.content)

                self.logger.info("Successfully parsed the question.")
                return parsed

            except Exception as exc:
                self.logger.error(f"Question generation error: {exc}")
                # Last attempt -> raise custom exception
                if attempt == settings.MAX_RETRIES - 1:
                    raise CustomException(
                        f"Generation failed after {settings.MAX_RETRIES} attempts",
                        exc,
                    ) from exc

        # Should never reach here
        raise CustomException("Unexpected error in _retry_and_parse.", None)

    def generate_mcq(self, topic: str, difficulty: str = "medium") -> MCQQuestion:
        """
        Generate a multiple-choice question (MCQ).

        Parameters
        ----------
        topic : str
            Topic for the MCQ.
        difficulty : str, optional
            Difficulty level, by default "medium".

        Returns
        -------
        MCQQuestion
            Validated MCQ Pydantic model.

        Raises
        ------
        CustomException
            If generation or validation fails.
        """
        try:
            # Bind parser to MCQQuestion model
            parser = PydanticOutputParser(pydantic_object=MCQQuestion)

            # Call LLM, parse, and return the model
            question: MCQQuestion = self._retry_and_parse(
                mcq_prompt_template,
                parser,
                topic,
                difficulty,
            )

            # Structural validation
            if len(question.options) != 4 or question.correct_answer not in question.options:
                raise ValueError("Invalid MCQ structure: requires 4 options and a valid correct_answer.")

            self.logger.info("Generated a valid MCQ question.")
            return question

        except Exception as exc:
            self.logger.error(f"Failed to generate MCQ: {exc}")
            raise CustomException("MCQ generation failed.", exc) from exc

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
            Topic for the question.
        difficulty : str, optional
            Difficulty level, by default "medium".

        Returns
        -------
        FillBlankQuestion
            Validated fill-in-the-blank Pydantic model.

        Raises
        ------
        CustomException
            If generation or validation fails.
        """
        try:
            # Bind parser to FillBlankQuestion model
            parser = PydanticOutputParser(pydantic_object=FillBlankQuestion)

            # Call LLM, parse, and return the model
            question: FillBlankQuestion = self._retry_and_parse(
                fill_blank_prompt_template,
                parser,
                topic,
                difficulty,
            )

            # Ensure the placeholder is present
            if "___" not in question.question:
                raise ValueError("Fill-in-the-blank question must contain '___' placeholder.")

            self.logger.info("Generated a valid fill-in-the-blank question.")
            return question

        except Exception as exc:
            self.logger.error(f"Failed to generate fill-in-the-blank question: {exc}")
            raise CustomException("Fill-in-the-blank generation failed.", exc) from exc
