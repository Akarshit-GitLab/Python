# Copilot Instructions for This Codebase

## Overview
This repository is a collection of Python practice scripts, each focused on a specific topic or concept. There is no single application or service; instead, the codebase is organized as a set of standalone files for learning and experimentation.

## Structure & Patterns
- Each `.py` file is self-contained and typically explores a single Python concept (e.g., functions, loops, file I/O, OOP, recursion, data structures).
- There are no shared modules, imports, or cross-file dependencies. Each script can be run independently.
- File naming follows the pattern `<topic>_practice[<number>].py` (e.g., `function_practice2.py`, `oops_practice3.py`).
- No external packages or requirements are used; all code relies on the Python standard library.

## Developer Workflows
- **Run any script:** Open a terminal in the project directory and execute `python <filename>.py`.
- **No build or test system:** There are no automated tests, build steps, or CI/CD workflows.
- **Debugging:** Use print statements or a Python debugger (e.g., VS Code's built-in debugger) as needed.

## Conventions
- Scripts are intended for experimentation and learning, not production use.
- Code style and structure may vary between files, reflecting different practice exercises or topics.
- There are no project-wide docstrings, type hints, or linting rules enforced.

## Examples
- `file_io_practice.py` demonstrates reading/writing files.
- `oops_practice2.py` explores object-oriented programming basics.
- `recursion_practice.py` contains recursive function examples.

## Guidance for AI Agents
- Treat each `.py` file as an isolated script.
- Do not assume shared state, configuration, or dependencies between files.
- When adding new scripts, follow the existing naming convention and keep them self-contained.
- If asked to refactor or combine scripts, clarify the intended integration approach with the user.

---
If any section is unclear or incomplete, please provide feedback for further refinement.
