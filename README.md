# 💰 Professional Expense Tracker CLI

A robust, object-oriented Command Line Interface (CLI) application built with Python to manage personal finances. This project demonstrates clean code principles, data persistence using JSON, and automated unit testing.



## 🚀 Features

* **Full CRUD Lifecycle**: Create, Read, Update, and Delete expenses with ease.
* **Smart Search**: Find and modify expenses using short ID snippets (UUID-based).
* **Financial Insights**: View total spending and a detailed breakdown by category.
* **Data Persistence**: All data is automatically saved to and loaded from a JSON database.
* **Robust Validation**: Integrated error handling for numeric inputs and empty fields.
* **Quality Assurance**: Comprehensive test suite powered by `pytest` ensuring 100% logic reliability.

## 📁 Project Structure

```text
expense_tracker/
├── data/               # Persistent JSON storage
├── src/                # Source code
│   ├── main.py         # Entry point (Presentation Layer)
│   ├── models.py       # Data structures (Data Layer)
│   ├── services.py     # Business logic (Service Layer)
│   └── storage.py      # File I/O handling (Infrastructure Layer)
├── tests/              # Automated test suite
│   └── test_expenses.py
├── conftest.py         # Pytest configuration
├── requirements.txt    # Project dependencies
└── README.md
## 🛠️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/aref9571/expense-tracker.git](https://github.com/aref9571/expense-tracker.git)
   cd expense-tracker