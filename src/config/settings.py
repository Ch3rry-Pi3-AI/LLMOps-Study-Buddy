"""
settings.py

Configuration module for the LLMOps StudyBuddy project.

This file loads environment variables and defines project-wide settings 
such as API keys, model configuration, retry limits, and other parameters 
required across pipelines, utilities, and application layers.
"""

# --------------------------------------------------------------
# Imports
# --------------------------------------------------------------
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()


class Settings:
    """
    A configuration container holding global settings for the StudyBuddy project.

    This class centralises all parameters related to model configuration,
    API authentication, and operational defaults. Values are sourced from
    environment variables where appropriate to keep sensitive information 
    secure and externalised.

    Attributes
    ----------
    GROQ_API_KEY : str | None
        API key for authenticating requests to the Groq LLM service.
    MODEL_NAME : str
        Name of the language model used for StudyBuddy interactions.
    TEMPERATURE : float
        Sampling temperature controlling creativity and variability 
        in generated outputs.
    MAX_RETRIES : int
        Maximum number of retry attempts when calling external services.
    """

    # ----------------------------------------------------------
    # External API keys and sensitive credentials
    # ----------------------------------------------------------

    # Groq API key used for accessing the hosted LLM endpoint
    GROQ_API_KEY: str | None = os.getenv("GROQ_API_KEY")

    # ----------------------------------------------------------
    # Model configuration parameters
    # ----------------------------------------------------------

    # Name of the model deployed for conversational reasoning
    MODEL_NAME: str = "llama-3.3-70b-versatile"

    # Degree of randomness in the model's output generation
    TEMPERATURE: float = 0.9

    # ----------------------------------------------------------
    # Operational parameters
    # ----------------------------------------------------------

    # Number of retry attempts before raising a failure
    MAX_RETRIES: int = 3


# Instantiate a global settings object for project-wide use
settings = Settings()
