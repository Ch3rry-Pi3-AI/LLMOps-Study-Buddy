# `models/` README — Question Schemas for StudyBuddy

The `models/` directory contains the **Pydantic data models** used across the **LLMOps StudyBuddy** project.
These models define the structured formats for different question types, ensuring that all question-related data is validated, type-safe, and consistent throughout the system.

At this stage, the folder includes schemas for:

* Multiple-choice questions
* Fill-in-the-blank questions

Additional schemas (e.g., flashcards, step-by-step reasoning objects, study plans, embeddings records, etc.) can be added as the project expands.

## 📁 Folder Overview

```text
src/models/
├── question_schemas.py     # Pydantic models for MCQ and fill-in-the-blank questions
└── README.md               # Documentation for the models module
```

## 🧠 `question_schemas.py` — Question Data Models

This module defines two core Pydantic models used by StudyBuddy’s question-generation and evaluation components.

### MCQQuestion

Represents a multiple-choice question, including:

* Question text
* A list of answer options
* The correct option
* Built-in validation and normalisation for question values

This model guarantees consistent formatting for all MCQs generated or processed by StudyBuddy.

### FillBlankQuestion

Represents a fill-in-the-blank question with:

* A question containing a `___` placeholder
* The correct answer
* Input normalisation that handles alternative formats

This structure is useful for vocabulary exercises, conceptual blanks, and memory-based questions.

## 🧩 How These Schemas Are Used

These models support the StudyBuddy system by:

* Validating incoming or generated questions
* Enforcing consistent structure across LLM outputs
* Providing a reliable schema for downstream evaluation
* Acting as typed data objects passed between pipelines and components

As StudyBuddy evolves, new schemas can be added here to support more complex study interactions such as:

* Multi-step reasoning tasks
* Short-answer questions
* Concept summaries
* Lesson-plan segments

## ✅ Summary

The `models/` folder defines the **typed, validated data structures** that underpin question handling in the StudyBuddy project.
These schemas ensure reliability and consistency across all components that generate, transform, or evaluate study questions.
