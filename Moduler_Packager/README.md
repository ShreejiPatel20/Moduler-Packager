# 🛠️ Multi-Utility Toolkit

A modular Python command-line application that bundles everyday utility functions into a clean, interactive console interface. The project demonstrates the usage of Python standard libraries (`datetime`, `time`, `math`, `random`, `uuid`) alongside custom packages for mathematical operations and file manipulation.

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Project Architecture](#-project-architecture)
- [Installation & Setup](#-installation--setup)
- [Usage](#-usage)
- [Console Interaction Flow](#-console-interaction-flow)
- [Error Handling](#-error-handling)
- [License](#-license)

---

## 📌 Overview

The **Multi-Utility Toolkit** is designed as a centralized terminal utility. It allows users to execute common operations—from date-time manipulation and compound interest calculation to secure UUID and password generation—through numbered interactive menus.

---

## 🚀 Key Features

### 1. 🕒 Datetime & Time Operations
- **Current Timestamp**: Displays current system date and time in `YYYY-MM-DD HH:MM:SS` format.
- **Date Difference**: Calculates elapsed days between two ISO dates (`YYYY-MM-DD`).
- **Custom Formatting**: Formats inputs via custom `strftime` format directives.
- **Stopwatch**: Precision execution timer using `time.perf_counter()`.
- **Countdown Timer**: Real-time terminal second countdown.

### 2. 🧮 Mathematical Operations
- **Factorial**: Recursive/iterative factorial computation.
- **Compound Interest**: Computes accrued amount and interest given principal, rate, and duration.
- **Trigonometric Functions**: Calculates `sin`, `cos`, and `tan` for angles entered in degrees.
- **Geometric Area**: Calculates area for circles, rectangles, and triangles.

### 3. 🎲 Random Data Generation
- **Random Integers**: Generates a random number within custom ranges.
- **Random Lists**: Creates populated integer lists based on user-defined length and bounds.
- **Secure Password Generator**: Generates mixed-character alphanumeric and symbolic passwords.
- **Numeric OTP**: Generates numeric one-time-passwords between 4 and 10 digits.

### 4. 🔑 Unique Identifiers (UUID)
- **UUID4 Generation**: Generates standard cryptographically strong UUID4 tokens.
- **Bulk Generation**: Generates lists of consecutive distinct UUIDs.

### 5. 📁 File Operations (Custom Module)
- **Create**: Initializes new files via `utility_package.file_utils`.
- **Write**: Overwrites or writes structured content to specified paths.
- **Read**: Reads and outputs file contents directly into the terminal.
- **Append**: Appends new data to existing files without overwriting existing content.

### 6. 🔍 Dynamic Module Exploration
- Inspects accessible namespace attributes and methods for standard and custom modules using Python's `dir()` introspector.

---

## 📂 Project Architecture

```text
multi-utility-toolkit/
├── main.py                     # Main execution file & menu orchestration
├── README.md                   # Project documentation
└── utility_package/            # Custom reusable module package
    ├── __init__.py             # Package initializer
    ├── file_utils.py           # File handling routines (create, read
