# `prompts/` README — Prompt Templates for StudyBuddy

The `prompts/` directory contains the **LLM prompt templates** used by the LLMOps StudyBuddy system.
These templates define the structured instructions given to the model so it can generate consistent, validated study questions that match the project’s Pydantic schemas.

This folder ensures that question generation behaves predictably and produces well-formed JSON ready for downstream processing.

## 📁 Folder Overview

```text
src/prompts/
├── templates.py      # 🎨 Prompt templates for MCQ + fill-in-the-blank generation
└── README.md         # 📚 Documentation for prompt templates
```

## 🎨 `templates.py` — Prompt Templates

This module defines two LangChain `PromptTemplate` objects:

### ❓ Multiple-Choice Question (MCQ) Template

Instructs the LLM to:

* generate a question at a specified difficulty
* produce exactly 4 answer options
* identify the correct option
* return a **strict JSON object** with the required fields

It is designed to match the `MCQQuestion` Pydantic schema in `models/question_schemas.py`.

### ✏️ Fill-in-the-Blank Template

Instructs the LLM to:

* generate a sentence with a `_____` placeholder
* provide the correct missing word or phrase
* return a clean JSON object with the fields required by the `FillBlankQuestion` schema

Both templates ensure compatibility with downstream parsing and validation logic.

## 🧩 How These Templates Fit Into StudyBuddy

The prompt templates in this folder form the backbone of the system’s question-generation capabilities.
They enable:

* reliable, schema-compatible LLM outputs
* consistent formatting across difficulty levels and topics
* smooth integration with evaluation modules, datasets, and agents

Future templates can be added here, such as:

* true/false questions
* short-answer prompts
* coding questions
* multi-step reasoning tasks

## ✅ Summary

The `prompts/` folder defines the reusable prompt templates that guide the LLM in producing structured study questions.
These templates ensure predictable output formats and seamless compatibility with StudyBuddy’s Pydantic models and evaluation pipeline.
