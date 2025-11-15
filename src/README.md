# `src/` README — Core Source Code Structure

The `src/` directory contains the **primary source code** for the LLMOps StudyBuddy project.
It includes the foundational modules responsible for configuration, logging, error handling, and now the structured Pydantic schemas used throughout the system.
As the project expands, this directory will grow to include pipelines, agent logic, LLM services, and workflow orchestration.

At this stage, the `src/` directory includes:

* `common/` — shared reliability utilities
* `config/` — global configuration and environment loading
* `models/` — Pydantic schemas for validated study-question structures

Future folders (pipelines, agents, retrieval modules, dataset loaders, evaluators) will be added as development continues.

## 📁 Folder Overview

```text
src/
├─ common/      # Core utilities for reliability (exceptions, logging)
├─ config/      # Global project configuration (environment + settings)
└─ models/      # Typed data schemas for study questions and future objects
```

# 📦 `common/` — Shared Reliability Utilities

The `common/` folder provides the foundational tools required for stable system behaviour.
It includes reusable modules for consistent debugging, exception handling, and logging.

### Contains

```text
src/common/
├─ __init__.py
├─ custom_exception.py   # Detailed, standardised error handling
└─ logger.py             # Centralised, timestamped logging system
```

### Functionality

* **`custom_exception.py`**
  Defines a `CustomException` with enhanced debugging context such as file name, line, and traceback.

* **`logger.py`**
  Provides a unified logging setup that writes timestamped logs to daily rotating files.

These modules ensure reliability and consistency across all StudyBuddy components.

# ⚙️ `config/` — Global Configuration Layer

The `config/` directory manages project-wide settings, environment variables, and global model parameters.
It keeps sensitive credentials out of the codebase and exposes structured configuration through a `Settings` class.

### Contains

```text
src/config/
├─ __init__.py
└─ settings.py     # Loads environment variables and defines global runtime parameters
```

### Functionality

* Loads environment variables using `dotenv`.

* Exposes a strongly typed `Settings` class that defines:

  * `GROQ_API_KEY`
  * `MODEL_NAME`
  * `TEMPERATURE`
  * `MAX_RETRIES`

* Provides a global `settings` instance for easy import across modules.

### Example

```python
from config.settings import settings

print(settings.MODEL_NAME)
```

# 🧠 `models/` — Typed Question Schemas

The `models/` folder defines **Pydantic models** that structure and validate question formats used in StudyBuddy’s learning and evaluation workflows.

### Contains

```text
src/models/
├─ __init__.py
└─ question_schemas.py     # MCQ and fill-in-the-blank question models
```

### Functionality

* **`MCQQuestion`**
  Represents a multiple-choice question with options, a correct answer, and question text normalisation.

* **`FillBlankQuestion`**
  Represents a fill-in-the-blank format with an expected answer and normalised text field.

These schemas provide a reliable, type-safe structure for future components such as:

* Question generators
* Evaluation pipelines
* Interactive study sessions
* RAG-based question transformation
* Dataset ingestion and validation

# ✅ Summary

* `src/` contains the backbone of the StudyBuddy application.
* `common/` provides consistent error handling and logging utilities.
* `config/` centralises environment and model settings.
* `models/` introduces validated, structured data schemas for question handling.
* The directory is now ready to expand into pipelines, LLM modules, agents, and workflow orchestration layers.