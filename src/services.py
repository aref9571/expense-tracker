from models_expense_tracker import Expense
from typing import List , Optional
from storage import StorageHandler

class ExpenseManager:
    def __init__(self):
        self.storage = StorageHandler()
        self.expenses : List[Expense] = self.storage.laod_expenses()

    def add_expense(self ,title : str ,amount: float , category: str) -> Expense:
        new_expense = Expense(title= title , amount= amount , category=category)
        self.expenses.append(new_expense)
        self.storage.save_expenses(self.expenses)
        return new_expense

    def get_expense(self) -> List[Expense]:
        return self.expenses

    def get_total_spending(self) -> float:
        all_expenses = self.get_expense()
        if not all_expenses:
            return 0.0
        return sum([i.amount for i in all_expenses])