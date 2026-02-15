import pytest
import os
from services import ExpenseManager
from models import Expense

@pytest.fixture
def manager():
    test_file = "data/test_expenses.json"

    if os.path.exists(test_file):
        os.remove(test_file)

    mgr = ExpenseManager()
    mgr.storage.file_path = test_file
    mgr.expenses = []

    yield mgr
    if os.path.exists(test_file):
        os.remove(test_file)

def test_add_expenses_and_total(manager):
    manager.add_expense("coffee" , 5.0 , "food")
    manager.add_expense("bus", 1.0, "transport")

    assert len(manager.get_expenses()) == 2
    assert manager.get_total_spending() == 6.0

def test_delete_expenses(manager):
    exp = manager.add_expense("water" , 2.5 , "food")
    assert len(manager.get_expenses()) == 1

    result = manager.delete_expense(exp.id)
    assert result is True
    assert len(manager.get_expenses()) == 0
    assert manager.get_total_spending() == 0.0

def test_edit_expense_updates_total(manager):
    exp = manager.add_expense("apple" , 0.95 , "food")
    assert manager.get_total_spending() == 0.95

    manager.edit_expense(exp.id , amount= 1.78)
    assert manager.get_total_spending() == 1.78
    assert manager.get_expenses()[0].amount == 1.78

def test_category_summary(manager):
    manager.add_expense("Burger", 10.0, "Food")
    manager.add_expense("Coke", 2.0, "Food")
    manager.add_expense("Taxi", 15.0, "Transport")

    summary = manager.category_summary()
    assert summary["Food"] == 12.0
    assert summary["Transport"] == 15.0
    assert len(summary) == 2

def test_persistence(manager):
    manager.add_expense("Saved Item", 50.0, "Tech")
    new_manager = ExpenseManager()
    new_manager.storage.file_path = manager.storage.file_path
    new_manager.expenses = new_manager.storage.load_expenses()
    assert len(new_manager.get_expenses()) == 1
    assert new_manager.get_expenses()[0].title == "Saved Item"