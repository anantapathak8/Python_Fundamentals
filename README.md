# Python Fundamentals Lab – Week 1

An independent, beginner-friendly portfolio project covering core Python programming concepts through practical real-world scenarios including student management, event registration, financial calculations, and algorithmic problem-solving.

Built with **Python 3.10+** syntax using only the Python standard library.

---

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Prerequisites & Setup](#prerequisites--setup)
- [Basics Modules Overview](#basics-modules-overview)
- [Practice Exercises Overview](#practice-exercises-overview)
- [How to Run Each Program](#how-to-run-each-program)
- [Automated Testing](#automated-testing)
- [Coding Standards & Design Principles](#coding-standards--design-principles)

---

## Overview

This repository is organized into two primary sections:
1. **`basics/`**: Six foundational modules demonstrating data types, string operations, lists, dictionaries, loops, and function design.
2. **`exercises/`**: Ten standalone practical programs tackling classic problems, mathematical calculations, string parsing, and interactive games with robust input validation.

---

## Project Structure

```text
Python_Basics_Week01/
├── .gitignore
├── README.md
├── test_suite.py
├── basics/
│   ├── variables_datatypes.py
│   ├── string_operations.py
│   ├── list_operations.py
│   ├── dictionary_operations.py
│   ├── for_and_while_loops.py
│   └── functions.py
└── exercises/
    ├── 01_word_analyzer.py
    ├── 02_fizzbuzz.py
    ├── 03_temperature_converter.py
    ├── 04_number_classifier.py
    ├── 05_palindrome_checker.py
    ├── 06_basic_calculator.py
    ├── 07_vowel_frequency.py
    ├── 08_number_guessing.py
    ├── 09_factorial_calculator.py
    └── 10_prime_number_checker.py
```

---

## Prerequisites & Setup

- **Python**: Version 3.10 or higher.
- **Dependencies**: None (pure standard library).

Check your installed Python version:
```bash
python --version
```

Clone or open the workspace folder in your terminal and you are ready to run any script immediately.

---

## Basics Modules Overview

Each file in `basics/` focuses on core fundamentals applied to practical scenarios:

| Module | Scenario / Focus | Key Concepts Demonstrated |
| :--- | :--- | :--- |
| [`basics/variables_datatypes.py`](file:///basics/variables_datatypes.py) | Student tuition calculation | `int`, `float`, `str`, `bool`, `NoneType`, explicit casting, truthiness, formatted f-strings. |
| [`basics/string_operations.py`](file:///basics/string_operations.py) | Event attendee badge creation | Slicing `[start:stop:step]`, `.strip()`, `.title()`, `.upper()`, `.replace()`, `.split()`, `.join()`. |
| [`basics/list_operations.py`](file:///basics/list_operations.py) | Workshop registration roster | `.append()`, `.insert()`, `.extend()`, `.pop()`, `.remove()`, sorting, slicing, list comprehensions, `min()`, `max()`, `sum()`. |
| [`basics/dictionary_operations.py`](file:///basics/dictionary_operations.py) | Student gradebook directory | Key-value mapping, safe `.get()` fallbacks, nested dictionaries, dictionary comprehensions, `.items()` iteration. |
| [`basics/for_and_while_loops.py`](file:///basics/for_and_while_loops.py) | Keynote schedule & ticketing queue | `for`, `while`, `range()`, `enumerate()`, `zip()`, `break`, `continue`, and loop `else` clauses. |
| [`basics/functions.py`](file:///basics/functions.py) | Course registration & billing engine | Positional & keyword arguments, default parameters, `*args`, `**kwargs`, multiple return values, type annotations. |

---

## Practice Exercises Overview

Every exercise script is self-contained, validates user inputs against bad data, handles potential exceptions gracefully, and features a dual mode:
- **Interactive Mode**: Prompts for custom input when run in an interactive terminal.
- **Automated Demo Mode**: Pressing Enter (or running without input) executes a comprehensive demonstration with sample inputs.

| Script | Title | Description & Capabilities |
| :--- | :--- | :--- |
| [`exercises/01_word_analyzer.py`](file:///exercises/01_word_analyzer.py) | Word & Text Analyzer | Computes word counts, character counts (with/without spaces), unique vocabulary, longest and shortest words, and average word length. |
| [`exercises/02_fizzbuzz.py`](file:///exercises/02_fizzbuzz.py) | FizzBuzz Generator | Classic interview test from 1 to $N$ with custom bounds, formatted grid output, and distribution metrics. |
| [`exercises/03_temperature_converter.py`](file:///exercises/03_temperature_converter.py) | Temperature Converter | Converts between Celsius, Fahrenheit, and Kelvin scales with strict validation against absolute zero. |
| [`exercises/04_number_classifier.py`](file:///exercises/04_number_classifier.py) | Number Classifier | Analyzes numeric values for sign (positive/negative/zero), parity (even/odd), data form (integer/float), magnitude, and divisibility. |
| [`exercises/05_palindrome_checker.py`](file:///exercises/05_palindrome_checker.py) | Palindrome Checker | Tests words and multi-word sentences for palindrome symmetry, stripping punctuation, symbols, and case. |
| [`exercises/06_basic_calculator.py`](file:///exercises/06_basic_calculator.py) | Basic Calculator | Executes operations (`+`, `-`, `*`, `/`, `//`, `%`, `**`), handling `ZeroDivisionError` and `ValueError` gracefully. |
| [`exercises/07_vowel_frequency.py`](file:///exercises/07_vowel_frequency.py) | Vowel Frequency Counter | Counts vowel occurrences (A, E, I, O, U), computes percentage shares, and renders an ASCII distribution bar. |
| [`exercises/08_number_guessing.py`](file:///exercises/08_number_guessing.py) | Number Guessing Game | Interactive guessing game with directional feedback and bounded attempts, plus an automated Binary Search AI solver. |
| [`exercises/09_factorial_calculator.py`](file:///exercises/09_factorial_calculator.py) | Factorial Calculator | Computes factorials using both iterative and recursive implementations, validates $n \ge 0$, and prints expanded formula strings. |
| [`exercises/10_prime_number_checker.py`](file:///exercises/10_prime_number_checker.py) | Prime Number Checker | Efficient $O(\sqrt{n})$ trial division primality tester, composite divisor identification, and prime sequence generator up to 100. |

---

## How to Run Each Program

Run any script directly from the workspace root using Python:

### Basics Scripts

```bash
# Variables and data types demo
python basics/variables_datatypes.py

# String operations and badge formatting
python basics/string_operations.py

# List operations and score analytics
python basics/list_operations.py

# Dictionary operations and nested gradebook
python basics/dictionary_operations.py

# For loops, while loops, enumerate, and zip
python basics/for_and_while_loops.py

# Functions, default arguments, *args, and **kwargs
python basics/functions.py
```

### Exercise Scripts

```bash
# 01 Word & Text Analyzer
python exercises/01_word_analyzer.py

# 02 FizzBuzz Generator
python exercises/02_fizzbuzz.py

# 03 Temperature Converter
python exercises/03_temperature_converter.py

# 04 Number Classifier
python exercises/04_number_classifier.py

# 05 Palindrome Checker
python exercises/05_palindrome_checker.py

# 06 Basic Calculator
python exercises/06_basic_calculator.py

# 07 Vowel Frequency Counter
python exercises/07_vowel_frequency.py

# 08 Number Guessing Game (Choose 1 for play, 2 for AI demo)
python exercises/08_number_guessing.py

# 09 Factorial Calculator
python exercises/09_factorial_calculator.py

# 10 Prime Number Checker & Generator
python exercises/10_prime_number_checker.py
```

---

## Automated Testing

An automated test suite is included in [`test_suite.py`](file:///test_suite.py). It validates:
1. Direct module imports and logic assertions for all `basics` modules.
2. Direct function calls and mathematical assertions for all 10 `exercises`.
3. Subprocess execution of all 16 files to ensure non-blocking exit codes (code `0`).

Run the test suite with:
```bash
python test_suite.py
```

Expected output:
```text
Testing 'basics' package modules...
  ✓ basics/variables_datatypes.py verified.
  ✓ basics/string_operations.py verified.
  ✓ basics/list_operations.py verified.
  ✓ basics/dictionary_operations.py verified.
  ✓ basics/for_and_while_loops.py verified.
  ✓ basics/functions.py verified.

Testing 'exercises' modules logic...
  ✓ exercises/01_word_analyzer.py verified.
  ✓ exercises/02_fizzbuzz.py verified.
  ✓ exercises/03_temperature_converter.py verified.
  ✓ exercises/04_number_classifier.py verified.
  ✓ exercises/05_palindrome_checker.py verified.
  ✓ exercises/06_basic_calculator.py verified.
  ✓ exercises/07_vowel_frequency.py verified.
  ✓ exercises/08_number_guessing.py verified.
  ✓ exercises/09_factorial_calculator.py verified.
  ✓ exercises/10_prime_number_checker.py verified.

Testing standalone execution of all 16 files via subprocess...
  ✓ Process Exit 0: basics/variables_datatypes.py
  ...
  ✓ Process Exit 0: exercises/10_prime_number_checker.py

============================================================
ALL 16 PYTHON PROGRAMS AND TESTS PASSED SUCCESSFULLY!
============================================================
```

---

## Coding Standards & Design Principles

- **PEP 8 Compliance**: Consistent formatting, descriptive snake_case naming, and clean indentation.
- **Python 3.10 Type Annotations**: Clear parameter and return type signatures (e.g. `tuple[bool, int | None]`).
- **Defensive Input Handling**: Safe handling of invalid types, numbers out of bounds, and zero-division cases.
- **Dual Execution Pattern**: Interactive CLI mode combined with default demo fallback for automated testing environments.
- **Pure Standard Library**: No external dependencies or packages required.

## Academic Context & Author Notes

This project is **Week 1** of a structured 4-week Python and Software Engineering learning program:

- **Week 1:** Python Fundamentals, Data Structures & Algorithmic Foundations *(This Project)*
- **Week 2:** Object-Oriented Programming (OOP), Modules, Exception Handling & File Management
- **Week 3:** **Git, GitHub, Version Control, Collaboration & Professional Engineering Practices** 
- **Week 4:** Capstone Project — Building a Python-based CLI Expense Tracker with JSON Persistence, Testing & Documentation

**Author:** B.Tech Computer Science Engineering Student, specializing in Robotics & Artificial Intelligence  
**Academic Focus:** Software Development, Robotics, Artificial Intelligence & Cybersecurity  
