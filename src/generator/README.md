# `generator/` README — Question Generation Service

The `generator/` directory contains the **question-generation logic** used by the LLMOps StudyBuddy project.
This folder provides the service layer that ties together:

* LangChain prompt templates
* Pydantic schemas
* The Groq LLM client
* Retry logic and logging
* Structured, validated output

It acts as the **bridge** between prompts, the language model, and the typed data models used throughout StudyBuddy.

At this stage, the folder contains the main generator responsible for producing study questions.

## 📁 Folder Overview

```text
src/generator/
├── question_generator.py     # 🧠 High-level service for generating MCQ + fill-blank questions
└── README.md                 # 📚 Documentation for the generator module
```

## 🧠 `question_generator.py` — Question Generation Service

This module defines the `QuestionGenerator` class, which provides high-level methods for generating structured study questions.
It incorporates:

### Key Responsibilities

* Calling the Groq LLM using the centralised client
* Formatting prompts with topic and difficulty
* Parsing the LLM response using `PydanticOutputParser`
* Enforcing strict JSON schemas
* Applying validation rules (e.g., MCQ must have 4 options)
* Retrying failed generations up to `MAX_RETRIES`
* Logging all activity for observability and debugging

### Supported Question Types

* **MCQ (Multiple-Choice Questions)**
  Generated via `generate_mcq(topic, difficulty)`
  Parsed into the `MCQQuestion` Pydantic model.

* **Fill-in-the-Blank**
  Generated via `generate_fill_blank(topic, difficulty)`
  Parsed into the `FillBlankQuestion` Pydantic model.

### Example Usage

```python
from generator.question_generator import QuestionGenerator

generator = QuestionGenerator()

mcq = generator.generate_mcq("machine learning", "medium")
print(mcq)

fill = generator.generate_fill_blank("calculus", "easy")
print(fill)
```

The returned objects are fully typed, validated Pydantic models ready for downstream use.

## 🧩 How This Fits Into StudyBuddy

The `generator/` module serves as the **core question-production engine** powering future features such as:

* Study session agents
* Automated quiz builders
* RAG-driven question refinement
* Evaluation and grading pipelines
* Analytics about student performance

It standardises how questions are created, validated, and consumed across the system.

## ✅ Summary

The `generator/` folder provides:

* A high-level question generation service
* Integrated LLM → prompt → schema pipeline
* Structured, validated educational content
* A foundation for future tutoring and intelligent assessment components
