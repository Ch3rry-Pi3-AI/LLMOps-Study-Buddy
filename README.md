# 🧰 **Utilities & Quiz Management — LLMOps StudyBuddy**

This branch introduces the **utils layer** for the LLMOps StudyBuddy project.
It provides helper functions and the full **QuizManager**, which together enable interactive quiz workflows inside the Streamlit application.

These utilities connect the question-generation engine to the user-facing quiz interface, handling quiz state, answer collection, scoring, result formatting, and saving outputs to CSV.

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
│   ├── generator/
│   └── utils/
│       └── helpers.py        # 🧰 Streamlit helpers + QuizManager implementation
└── README.md
```

## 🧠 **What This Branch Adds**

### 🧰 `helpers.py`

This module provides two key additions:



### 1. 🔄 `rerun()`

A small Streamlit helper that toggles a session-state flag to force the UI to refresh.
Useful for interactive controls, resetting forms, and managing dynamic quiz behaviour.



### 2. 🧠 `QuizManager`

The central quiz-handling class responsible for:

#### **Question Generation**

* Uses the `QuestionGenerator` to create MCQs or fill-in-the-blank questions
* Accepts topic, difficulty, and number of questions
* Stores questions in a serialisable JSON-friendly format

#### **Quiz Interaction**

* Renders questions via Streamlit widgets:

  * `st.radio` for MCQs
  * `st.text_input` for fill-in-the-blank
* Collects answers in the correct order

#### **Evaluation**

* Compares user answers to correct answers
* Normalises casing/whitespace for fill blanks
* Records per-question performance

#### **Results Export**

* Produces a pandas DataFrame of results
* Saves timestamped CSV files to `results/`
* Displays success or error messages in the Streamlit UI

Taken together, `QuizManager` forms the **full quiz workflow** that bridges LLM-generated questions and the StudyBuddy UI.

## 🧪 **Example Usage**

```python
from utils.helpers import QuizManager
from generator.question_generator import QuestionGenerator

quiz = QuizManager()
qg = QuestionGenerator()

if quiz.generate_questions(qg, "statistics", "Multiple Choice", "medium", 5):
    quiz.attempt_quiz()
    quiz.evaluate_quiz()
    df = quiz.generate_result_dataframe()
```

The returned DataFrame and CSV outputs make it easy to store, analyse, or review completed quizzes.

## ✅ **In Summary**

This branch:

* Adds the **`utils/`** folder to the project
* Introduces the **QuizManager**, the interactive quiz engine of StudyBuddy
* Adds a simple `rerun()` helper for Streamlit app control
* Enables:

  * question generation → interaction → evaluation → export
  * smooth integration with the existing `QuestionGenerator`
  * future extensions such as review sessions, scoring analytics, and personalised feedback

This layer is essential for turning raw LLM output into a usable, interactive study experience.
