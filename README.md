# Expense Tracker CLI

A command-line application for recording personal expenses, written in Python. Expenses are kept in a JSON file, so they are still there the next time the program starts.

## Features

- Add, list, edit and delete expenses, each with a title, amount and category
- Select an expense by the first characters of its ID instead of typing the full UUID
- Total spending and a breakdown by category
- Input validation: empty titles and categories are rejected, and amounts must be positive numbers
- Unit tests for the business logic with pytest

## Tech stack

- Python 3.13
- pytest
- JSON file storage

## Project structure

```text
expense-tracker/
├── src/
│   ├── main.py        Command-line menu and input handling
│   ├── models.py      Expense data class and JSON conversion
│   ├── services.py    ExpenseManager with the business logic
│   └── storage.py     Reading and writing data/expenses.json
├── tests/
│   └── expenses_test.py
├── conftest.py        Adds src/ to the import path for the tests
└── requirements.txt
```

The code is split into layers: `main.py` only talks to the user, `ExpenseManager` holds the rules, and `StorageHandler` is the only part that touches the file system.

## Getting started

```bash
git clone https://github.com/aref9571/expense-tracker.git
cd expense-tracker
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Run the application from the repository root:

```bash
python src/main.py
```

Expenses are saved to `data/expenses.json`, which is created on first use and is not tracked by Git.

## Running tests

```bash
pytest
```

The tests cover adding expenses and the total, deleting, editing, the category summary and saving and loading from the JSON file. GitHub Actions runs them on every push to `main`.

## Limitations

- Amounts are stored as floating-point numbers, so totals can show small rounding errors; a real finance application would use `Decimal` or integer cents.
- There is one currency and no dates in the menu, even though each expense records when it was created.
