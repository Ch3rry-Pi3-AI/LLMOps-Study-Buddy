# ❓ **Question Schemas — LLMOps StudyBuddy**

This branch introduces the **first data models** for the **LLMOps StudyBuddy** project.
It adds **Pydantic-based question schemas** to represent:

* Multiple-choice questions (MCQs)
* Fill-in-the-blank questions

These schemas provide a **typed, validated structure** for question data that future components (generators, evaluators, agents, RAG pipelines) can rely on.

## 🗂️ **Updated Project Structure**

Only the **new file and its folder** are annotated below:

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
│   └── models/
│       └── question_schemas.py    # 📘 Pydantic schemas for MCQ and fill-in-the-blank questions
└── README.md
```

## 🧠 **What This Branch Adds**

### 📘 `question_schemas.py`

This module defines two core Pydantic models:

* `MCQQuestion`

  * `question`: the question text
  * `options`: list of answer options
  * `correct_answer`: correct option from the list
  * A `clean_question` validator that normalises the question field (e.g. when it arrives as a dict with `description`).

* `FillBlankQuestion`

  * `question`: text containing `___` where the blank should appear
  * `answer`: the correct word or phrase
  * A `clean_question` validator with the same normalisation behaviour.

These models enforce **consistent structure** and **light cleaning** of question text, which will be important when working with LLM outputs and external data sources.

## 🧪 **Example Usage**

```python
from models.question_schemas import MCQQuestion, FillBlankQuestion

mcq = MCQQuestion(
    question="What is the time complexity of binary search?",
    options=["O(n)", "O(log n)", "O(n log n)", "O(1)"],
    correct_answer="O(log n)"
)

fill = FillBlankQuestion(
    question="The derivative of sin(x) is ___.",
    answer="cos(x)"
)
```

These objects can now be passed between services, stored, validated, or used as the target schema for LLM responses.

## ✅ **In Summary**

This branch:

* Adds a dedicated **`models/` layer** for structured data
* Introduces **Pydantic schemas** for MCQ and fill-in-the-blank questions
* Normalises question text to handle less structured inputs
* Lays the groundwork for future components that will **generate, transform, and assess** study questions
