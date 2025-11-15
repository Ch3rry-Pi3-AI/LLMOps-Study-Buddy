# `src/` README — Core Source Code Structure

The `src/` directory contains the **primary source code** for the LLMOps StudyBuddy project.
This folder holds the foundational modules responsible for configuration, error handling, logging, and (as the project grows) the core logic, pipelines, and application components.

At this early stage of the project, the `src/` directory includes:

* `common/` — shared utilities for exceptions and logging
* `config/` — centralised configuration and settings management

Further folders (pipelines, agents, data access layers, API services, etc.) will be added as the project evolves.

## 📁 Folder Overview

```text
src/
├─ common/      # Core utilities for reliability (exceptions, logging)
└─ config/      # Global project configuration (environment + settings)
```



# 📦 `common/` — Shared Reliability Utilities

The `common/` folder provides the foundational building blocks for robust system behaviour.
It includes reusable components that support consistent debugging, error reporting, and logging across the entire codebase.

### Contains

```text
src/common/
├─ __init__.py
├─ custom_exception.py   # Detailed, standardised error handling
└─ logger.py             # Centralised, timestamped logging system
```

### Functionality

* **`custom_exception.py`**
  Supplies a `CustomException` class that enriches errors with context (file, line, traceback), ensuring clear debugging.

* **`logger.py`**
  Offers a unified logging setup that outputs timestamped logs to rotating daily log files.

These utilities ensure all future StudyBuddy modules share the same reliable error-handling and logging mechanisms.



# ⚙️ `config/` — Global Configuration Layer

The `config/` directory manages all settings required across the StudyBuddy system.
It keeps sensitive values externalised and provides a structured interface to global parameters.

### Contains

```text
src/config/
├─ __init__.py
└─ settings.py     # Loads environment variables and defines model + runtime parameters
```

### Functionality

* Loads environment variables using `dotenv`.
* Exposes a `Settings` class with attributes such as:

  * `GROQ_API_KEY`
  * `MODEL_NAME`
  * `TEMPERATURE`
  * `MAX_RETRIES`
* Defines a global `settings` instance for easy import across modules.

### Example

```python
from config.settings import settings

print(settings.MODEL_NAME)
```



# ✅ Summary

* `src/` contains the backbone of the StudyBuddy application.
* `common/` supplies essential reliability utilities (exception handling + logging).
* `config/` provides centralised, environment-driven configuration management.
* This structure lays the foundation for upcoming folders such as pipelines, agent logic, data modules, evaluation tools, and deployment layers.
