"""
templates.py

Prompt templates for generating structured study questions in the
LLMOps StudyBuddy project.

This module defines LangChain `PromptTemplate` objects for creating
multiple-choice questions (MCQs) and fill-in-the-blank questions. Each
template instructs the LLM to return strictly formatted JSON compatible
with the project's Pydantic schemas, while avoiding overused examples.
"""

# --------------------------------------------------------------
# Imports
# --------------------------------------------------------------
from langchain_core.prompts import PromptTemplate


# --------------------------------------------------------------
# Multiple-Choice Question Prompt Template
# --------------------------------------------------------------
mcq_prompt_template: PromptTemplate = PromptTemplate(
    template=(
        "You are helping to build a quiz. Generate a {difficulty} multiple-choice "
        "question about the topic: {topic}.\n\n"
        "Requirements:\n"
        "- The question must be about a specific fact, event, person, idea or concept.\n"
        "- It must be different from typical textbook cliches.\n"
        "- Do NOT ask about Machu Picchu, the Incas, the Terracotta Army, "
        "the Qin dynasty, or other overused examples unless they are explicitly "
        "mentioned in the topic text.\n"
        "- Make this question feel distinct and interesting.\n\n"
        "Return ONLY a JSON object with these exact fields:\n"
        "- 'question': A clear, specific question\n"
        "- 'options': An array of exactly 4 possible answers\n"
        "- 'correct_answer': One of the options that is the correct answer\n\n"
        "Example format:\n"
        '{{\n'
        '    \"question\": \"What is the capital of France?\",\n'
        '    \"options\": [\"London\", \"Berlin\", \"Paris\", \"Madrid\"],\n'
        '    \"correct_answer\": \"Paris\"\n'
        '}}\n\n'
        "Your response:"
    ),
    input_variables=["topic", "difficulty"],
)


# --------------------------------------------------------------
# Fill-in-the-Blank Question Prompt Template
# --------------------------------------------------------------
fill_blank_prompt_template: PromptTemplate = PromptTemplate(
    template=(
        "You are helping to build a quiz. Generate a {difficulty} fill-in-the-blank "
        "question about the topic: {topic}.\n\n"
        "Requirements:\n"
        "- The sentence should test a specific historical fact, person, date or concept.\n"
        "- It must be different from typical textbook cliches.\n"
        "- Do NOT ask about Machu Picchu, the Incas, the Terracotta Army, "
        "the Qin dynasty, or other overused examples unless they are explicitly "
        "mentioned in the topic text.\n"
        "- Make this question feel distinct and interesting.\n\n"
        "Return ONLY a JSON object with these exact fields:\n"
        "- 'question': A sentence with '_____' marking where the blank should be\n"
        "- 'answer': The correct word or phrase that belongs in the blank\n\n"
        "Example format:\n"
        '{{\n'
        '    \"question\": \"The capital of France is _____.\",\n'
        '    \"answer\": \"Paris\"\n'
        '}}\n\n'
        "Your response:"
    ),
    input_variables=["topic", "difficulty"],
)
