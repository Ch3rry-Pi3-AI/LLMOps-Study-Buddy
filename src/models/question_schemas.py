"""
question_schemas.py

Pydantic models for representing question schemas in the LLMOps StudyBuddy project.

This module defines structured data models for different question types used
by the StudyBuddy system, such as multiple-choice questions (MCQs) and
fill-in-the-blank questions. The models provide validation and light
normalisation of question text to ensure consistent handling across the
application.
"""

# --------------------------------------------------------------
# Imports
# --------------------------------------------------------------
from __future__ import annotations

# Standard library typing tools
from typing import List

# Pydantic base model and field utilities
from pydantic import BaseModel, Field, validator


# --------------------------------------------------------------
# Multiple-Choice Question Schema
# --------------------------------------------------------------
class MCQQuestion(BaseModel):
    """
    Schema for a multiple-choice question (MCQ).

    This model captures the text of the question, a fixed-size list of options,
    and the correct answer. It also includes light normalisation to handle
    cases where the question text may be provided as a dictionary.

    Attributes
    ----------
    question : str
        The question text being asked.
    options : list of str
        A list containing the available answer options (typically 4).
    correct_answer : str
        The correct answer, which must be one of the provided options.
    """

    # The question text to present to the learner
    question: str = Field(description="The question text")

    # List of possible answer options
    options: List[str] = Field(description="List of 4 options")

    # Correct answer, expected to match one of the options
    correct_answer: str = Field(
        description="The correct answer from the options"
    )

    # Normalises question input when it is provided as a dictionary
    @validator("question", pre=True)
    def clean_question(cls, v: object) -> str:
        """
        Normalise the question field when initialised.

        If the incoming question value is a dictionary, it attempts to extract
        a 'description' field; otherwise, it converts the value to a string.

        Parameters
        ----------
        cls : type[MCQQuestion]
            The model class.
        v : object
            The raw value provided for the question field.

        Returns
        -------
        str
            The normalised question text.
        """
        if isinstance(v, dict):
            return v.get("description", str(v))
        return str(v)


# --------------------------------------------------------------
# Fill-in-the-Blank Question Schema
# --------------------------------------------------------------
class FillBlankQuestion(BaseModel):
    """
    Schema for a fill-in-the-blank question.

    This model represents a question where one or more words are omitted from
    the text and represented by '___'. It stores both the question text and
    the correct answer used to fill the blank.

    Attributes
    ----------
    question : str
        The question text containing '___' to mark the blank.
    answer : str
        The correct word or phrase that fills the blank.
    """

    # Question text with a placeholder '___' for the blank
    question: str = Field(
        description="The question text with '___' for the blank"
    )

    # Correct answer that should fill the blank
    answer: str = Field(
        description="The correct word or phrase for the blank"
    )

    # Normalises question input when it is provided as a dictionary
    @validator("question", pre=True)
    def clean_question(cls, v: object) -> str:
        """
        Normalise the question field when initialised.

        If the incoming question value is a dictionary, it attempts to extract
        a 'description' field; otherwise, it converts the value to a string.

        Parameters
        ----------
        cls : type[FillBlankQuestion]
            The model class.
        v : object
            The raw value provided for the question field.

        Returns
        -------
        str
            The normalised question text.
        """
        if isinstance(v, dict):
            return v.get("description", str(v))
        return str(v)
