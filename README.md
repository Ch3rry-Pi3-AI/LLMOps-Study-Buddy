# 🎨 **Streamlit Application — LLMOps StudyBuddy**

This branch introduces the **interactive user interface** for the LLMOps StudyBuddy project.
The new `app.py` file provides a full Streamlit-powered quiz experience that allows users to:

* Select a topic, difficulty, and question type
* Generate multiple-choice or fill-in-the-blank questions
* Attempt the quiz interactively
* View detailed results
* Save and download a CSV of completed quiz attempts

The Streamlit interface sits on top of the existing LLM-powered generation pipeline and delivers a clean, responsive, and user-friendly quiz workflow.

## 🎥 **Application Demonstrations**

Below are two demonstrations of the Streamlit StudyBuddy app in action.

### **Multiple-Choice Question Demo**

<p align="center">
  <img src="img/streamlit/streamlit_app1.gif" alt="StudyBuddy Multiple Choice Demo" width="100%">
</p>

### **Fill-in-the-Blank Question Demo**

<p align="center">
  <img src="img/streamlit/streamlit_app2.gif" alt="StudyBuddy Fill in the Blank Demo" width="100%">
</p>

## 🗂️ **Updated Project Structure**

Only the **new file** added in this branch is annotated below:

```text
LLMOPS-STUDY-BUDDY/
├── .venv/
├── .env
├── .gitignore
├── .python-version
├── app.py                      # 🎨 Streamlit application for StudyBuddy
├── img/
│   └── streamlit/
│       ├── streamlit_app1.gif
│       └── streamlit_app2.gif
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
└── README.md
```

## 🚀 **What This Branch Adds**

### 🎨 `app.py`

The new `app.py` file implements the complete Streamlit interface for StudyBuddy.

It includes:

* Sidebar configuration for question type, topic, difficulty, and number of questions
* A clean quiz generation workflow
* Interactive question display with radio buttons or text inputs
* A results page with correctness feedback and scoring
* CSV export functionality
* Session-state-driven reruns for smooth user experience

This marks the first end-user–facing interface layer of the StudyBuddy system.

## ▶️ **How to Run the Streamlit App**

From the project root, execute:

```bash
streamlit run app.py
```

This launches the interactive StudyBuddy interface in your browser.

## ✅ **In Summary**

This branch:

* Adds the interactive **Streamlit application layer**
* Introduces the root-level `app.py` file
* Provides live demos via full-width GIF animations
* Connects the LLM generation pipeline with a polished UI
* Enables full quiz creation, attempt, evaluation, and export

Your StudyBuddy system now has a complete user interface ready for demonstrations, testing, and future enhancement.
