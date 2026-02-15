from models import Expense
from typing import List
from storage import StorageHandler

class ExpenseManager:
    def __init__(self):
        self.storage = StorageHandler()
        self.expenses: List[Expense] = self.storage.load_expenses()

    def add_expense(self, title: str, amount: float, category: str) -> Expense:
        new_expense = Expense(title=title, amount=amount, category=category)
        self.expenses.append(new_expense)
        self.storage.save_expenses(self.expenses)
        return new_expense


    def get_expenses(self) -> List[Expense]:
        return self.expenses

    def get_total_spending(self) -> float:
        all_expenses = self.get_expenses()
        if not all_expenses:
            return 0.0
        return sum([i.amount for i in all_expenses])

    def delete_expense(self, expense_id: str) -> bool:
        initial_length = len(self.expenses)
        self.expenses = [i for i in self.expenses if i.id != expense_id]
        self.storage.save_expenses(self.expenses)
        return len(self.expenses) < initial_length

    def category_summary(self) -> dict:
        summary = {}
        for i in self.expenses:
            summary[i.category] = summary.get(i.category, 0.0) + i.amount
        return summary

    def edit_expense(self, expense_id: str, title: str = None, amount: float = None, category: str = None) -> bool:
        for e in self.expenses:
            if e.id == expense_id:
                if title:
                    e.title = title
                if amount:
                    e.amount = amount
                if category:
                    e.category = category

                self.storage.save_expenses(self.expenses)
                return True
        return False