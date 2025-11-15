"""
groq_client.py

Client module for initialising and returning a Groq LLM instance
used within the LLMOps StudyBuddy project.

This module provides a simple wrapper function for constructing a
`ChatGroq` client using globally defined settings. It ensures that
all model configuration (API key, model name, temperature) remains
centralised and consistent across the system.
"""

# --------------------------------------------------------------
# Imports
# --------------------------------------------------------------
from langchain_groq import ChatGroq
from src.config.settings import settings


# --------------------------------------------------------------
# Groq LLM Client Factory
# --------------------------------------------------------------
def get_groq_llm() -> ChatGroq:
    """
    Create and return a configured Groq LLM client.

    The client is initialised using project-wide configuration values
    defined in the `settings` object. This function provides a clean,
    reusable entry point for any module requiring LLM access.

    Returns
    -------
    ChatGroq
        An instance of the Groq language model client configured with
        the API key, model name, and temperature defined in settings.
    """

    # Construct and return the Groq LLM client using global settings
    return ChatGroq(
        api_key=settings.GROQ_API_KEY,
        model=settings.MODEL_NAME,
        temperature=settings.TEMPERATURE,
    )
