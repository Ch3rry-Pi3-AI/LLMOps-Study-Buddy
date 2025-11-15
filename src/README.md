# `src/` README — Core Source Code Structure

The `src/` directory contains the **primary source code** for the LLMOps StudyBuddy project.
It includes the foundational modules responsible for configuration, logging, error handling, structured Pydantic schemas, and now prompt templates for question generation.
As the project grows, this directory will expand to include pipelines, agent logic, LLM services, retrieval workflows, and orchestration layers.

At this stage, the `src/` directory includes:

* `common/` — shared reliability utilities
* `config/` — global configuration and environment loading
* `models/` — Pydantic schemas for validated study-question structures
* `prompts/` — LangChain prompt templates for generating structured questions

Future modules (pipelines, agents, retrieval systems, evaluators, data loaders) will be added as development continues.

## 📁 Folder Overview

```text
src/
├─ common/      # Core utilities for reliability (exceptions, logging)
├─ config/      # Global project configuration (environment + settings)
├─ models/      # Typed data schemas for study questions and future objects
└─ prompts/     # Prompt templates for LLM-driven question generation
```

# 📦 `common/` — Shared Reliability Utilities

The `common/` folder provides the foundational tools required for stable system behaviour.
Its reusable modules support consistent exception handling and logging across all parts of the project.

### Contains

```text
src/common/
├─ __init__.py
├─ custom_exception.py   # Detailed, standardised error handling
└─ logger.py             # Centralised, timestamped logging system
```

### Functionality

* **`custom_exception.py`**
  Implements a detailed `CustomException` that enriches errors with file name, line number, and traceback context.

* **`logger.py`**
  Provides a unified daily-rotating logging system with timestamped entries.

These utilities establish consistent error-reporting and observability across all StudyBuddy components.

# ⚙️ `config/` — Global Configuration Layer

The `config/` directory manages project-wide configuration, keeps sensitive values externalised, and defines all environment-driven parameters.

### Contains

```text
src/config/
├─ __init__.py
└─ settings.py     # Loads environment variables and defines global runtime parameters
```

### Functionality

* Loads environment variables via `dotenv`.

* Exposes a strongly typed `Settings` class containing:

  * `GROQ_API_KEY`
  * `MODEL_NAME`
  * `TEMPERATURE`
  * `MAX_RETRIES`

* Provides a global `settings` instance that any module can import.

### Example

```python
from config.settings import settings

print(settings.MODEL_NAME)
```

# 🧠 `models/` — Typed Question Schemas

The `models/` directory defines **Pydantic models** used to structure and validate question data across the system.

### Contains

```text
src/models/
├─ __init__.py
└─ question_schemas.py     # MCQ and fill-in-the-blank question models
```

### Functionality

* **`MCQQuestion`**
  Represents a structured multiple-choice question with options, correct-answer validation, and question normalisation.

* **`FillBlankQuestion`**
  Represents a fill-in-the-blank question with a placeholder and expected answer field.

These schemas support future components such as:

* Question generators
* Study workloads and interactive sessions
* Evaluation or grading pipelines
* RAG-based question transformation
* Dataset ingestion and parsing

# 🎨 `prompts/` — LLM Prompt Templates

The `prompts/` directory contains reusable LangChain `PromptTemplate` objects used to instruct the LLM in generating structured JSON output compatible with the Pydantic schemas.

### Contains

```text
src/prompts/
├─ __init__.py
└─ templates.py      # Prompt templates for MCQ + fill-in-the-blank questions
```

### Functionality

* Provides templates that enforce strict JSON response structure
* Ensures compatibility with `MCQQuestion` and `FillBlankQuestion` schemas
* Defines reusable patterns for question-generation workflows

These templates are central to generating high-quality, model-consistent educational content.

# ✅ Summary

* `src/` contains the backbone infrastructure for the StudyBuddy application.
* `common/` provides reliable error handling and logging mechanisms.
* `config/` centralises environment settings and global configuration.
* `models/` defines validated data structures for question types.
* `prompts/` contains question-generation templates for use with LLMs.

The directory is now prepared for upcoming components such as pipelines, LLM orchestration, agent logic, and RAG-based study assistance.
