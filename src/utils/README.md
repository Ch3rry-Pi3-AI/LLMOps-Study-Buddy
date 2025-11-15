# `utils/` README — Utility Functions & Quiz Management

The `utils/` directory provides **supporting utilities** used throughout the LLMOps StudyBuddy project.
This folder contains lightweight helper tools that improve usability, manage quiz flow, and support the Streamlit frontend.

At this stage, the folder contains:

* A Streamlit rerun helper
* The complete quiz management system (`QuizManager`) used to generate, render, evaluate, and export quizzes

As the project expands, additional utility modules (formatters, caching helpers, validators, routing helpers) may be added here.

## 📁 Folder Overview

```text
src/utils/
├── helpers.py      # 🧰 QuizManager + Streamlit helpers
└── README.md       # 📚 Documentation for the utils module
```

## 🧰 `helpers.py` — Streamlit Helpers & Quiz Management

This module provides two key components:

### 🔄 `rerun()`

A small helper that toggles a Streamlit session-state key to trigger a UI rerun.
Useful for buttons and callback logic where a fresh render is required.

### 🧠 `QuizManager`

The core utility class that manages every part of the quiz lifecycle:

* **Generation**

  * Uses `QuestionGenerator` to create MCQs or fill-in-the-blank questions
  * Handles topic, difficulty, and question count
  * Stores a simple serialisable representation of each question

* **Interaction**

  * Renders MCQs and fill-blank questions through Streamlit widgets
  * Safely stores user answers

* **Evaluation**

  * Compares user answers against correct answers
  * Performs case-insensitive matching for fill-blank questions
  * Builds a detailed record for each question

* **Export**

  * Converts results into a pandas DataFrame
  * Saves timestamped CSV files in a `results/` directory

### Example Usage

```python
from utils.helpers import QuizManager
from generator.question_generator import QuestionGenerator

quiz = QuizManager()
qg = QuestionGenerator()

if quiz.generate_questions(qg, "calculus", "Multiple Choice", "medium", 5):
    quiz.attempt_quiz()
    quiz.evaluate_quiz()
    df = quiz.generate_result_dataframe()
```

## 🧩 How This Fits Into StudyBuddy

The utilities in this folder serve as **glue components** connecting the LLM question-generation engine to the Streamlit application layer.
They ensure that users can:

* interact smoothly with generated quizzes
* receive consistent evaluation
* export results for revision or record-keeping

Future enhancements (session tracking, scoring analytics, personalised feedback) will likely build on the structures defined here.

## ✅ Summary

The `utils/` folder provides:

* Streamlit-friendly helper functions
* A flexible, fully featured quiz manager
* A foundation for future UI and workflow-related tools

This module acts as a lightweight but essential support layer for the StudyBuddy system.
