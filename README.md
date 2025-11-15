# 🧠 **Question Generator — LLMOps StudyBuddy**

This branch introduces the **first high-level question-generation service** for the LLMOps StudyBuddy project.
It connects the entire workflow: prompt templates → LLM output → Pydantic parsing → validated study questions.

This service provides a unified interface for generating two structured question types:

* Multiple-choice questions (MCQs)
* Fill-in-the-blank questions

With built-in retries, logging, schema validation, and structured outputs, it forms a core intelligence layer for StudyBuddy.

## 🗂️ **Updated Project Structure**

Only the **new folder and file** introduced in this branch are annotated below:

```text
LLMOPS-STUDY-BUDDY/
├── .venv/
├── .env
├── .gitignore
├── .python-version
├── llmops_study_buddy.egg-info/
├── manifests/
├── pyproject.toml
├── requirements.txt
├── setup.py
├── uv.lock
├── src/
│   ├── common/
│   ├── config/
│   ├── models/
│   ├── prompts/
│   ├── llm/
│   └── generator/
│       └── question_generator.py     # 🧠 High-level generation service for MCQ + fill-blank questions
└── README.md
```

## 🧠 **What This Branch Adds**

### 🧠 `question_generator.py`

This module defines the `QuestionGenerator` class, which orchestrates:

* LangChain prompt templates
* The Groq Chat model
* Pydantic context-aware output parsing
* Retry logic across LLM failures
* Normalisation and validation of generated questions
* Logging for every attempt and error

It provides two primary methods:

### 1. `generate_mcq(topic, difficulty)`

Produces a fully validated `MCQQuestion` object using:

* the MCQ prompt template
* the `ChatGroq` model
* strict Pydantic parsing
* structural checks (4 options, correct_answer must be in options)

### 2. `generate_fill_blank(topic, difficulty)`

Produces a validated `FillBlankQuestion` object with:

* the fill-blank prompt
* Pydantic parsing
* strict placeholder validation (`___` required)

Together, these functions provide the building blocks for automated quizzes, tutoring systems, and curriculum generation.

## 🧪 **Example Usage**

```python
from generator.question_generator import QuestionGenerator

qg = QuestionGenerator()

mcq = qg.generate_mcq("machine learning", "medium")
print(mcq)

fill = qg.generate_fill_blank("calculus", "easy")
print(fill)
```

Each return value is a **typed Pydantic model**, not raw JSON — ready for:

* display
* storage
* analysis
* evaluation
* or transformation in future RAG components

## ✅ **In Summary**

This branch:

* Adds the **`generator/`** folder to the project
* Introduces the high-level **QuestionGenerator service**
* Provides robust retry, parsing, and logging for LLM outputs
* Validates question structure using strict Pydantic schemas
* Creates a unified API for generating educational content

This forms the **core engine** that later components — pipelines, agents, study planners, and evaluators — will build upon.
