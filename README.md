# 🎨 **Prompt Templates — LLMOps StudyBuddy**

This branch introduces the **first prompt templates** for the **LLMOps StudyBuddy** project.
It adds structured **LangChain `PromptTemplate` objects** used to generate:

* Multiple-choice questions (MCQs)
* Fill-in-the-blank questions

These templates instruct the LLM to return **strict JSON output** compatible with the project’s Pydantic question schemas.

## 🗂️ **Updated Project Structure**

Only the **new folder and file** added in this branch are annotated:

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
│   └── prompts/
│       └── templates.py    # 🎨 Prompt templates for MCQ + fill-in-the-blank generation
└── README.md
```

## 🧠 **What This Branch Adds**

### 🎨 `templates.py`

This module defines two reusable `PromptTemplate` objects:

* `mcq_prompt_template`

  * Generates a structured MCQ about a given topic and difficulty
  * Returns JSON with: `"question"`, `"options"`, `"correct_answer"`
  * Ensures exactly 4 options
  * Fully aligned with the `MCQQuestion` Pydantic schema

* `fill_blank_prompt_template`

  * Generates a fill-in-the-blank question containing `"_____"`
  * Returns JSON with: `"question"` and `"answer"`
  * Compatible with the `FillBlankQuestion` schema

Both templates enforce **strict formatting**, enabling reliable downstream validation and processing.

## 🧪 **Example Usage**

```python
from prompts.templates import mcq_prompt_template, fill_blank_prompt_template

prompt = mcq_prompt_template.format(topic="machine learning", difficulty="medium")
print(prompt)

prompt2 = fill_blank_prompt_template.format(topic="calculus", difficulty="easy")
print(prompt2)
```

These templates can be passed directly into an LLM chain or wrapped by a higher-level service.

## ✅ **In Summary**

This branch:

* Adds a dedicated **`prompts/`** folder
* Provides **structured LangChain prompt templates** for MCQ and fill-blank generation
* Ensures all question generation follows a **strict JSON schema**
* Builds the foundation for future components such as LLM pipelines, tutoring agents, and evaluation modules