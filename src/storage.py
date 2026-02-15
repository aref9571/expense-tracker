import json
import os
from typing import List
from models import Expense

class StorageHandler:
    def __init__(self, file_path: str = "data/expenses.json"):
        self.file_path = file_path
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

    def save_expenses(self, expenses: List[Expense]) -> None:
        data_to_save = [i.to_dict() for i in expenses]
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(data_to_save, f, indent=4)

    def load_expenses(self) -> List[Expense]:
        if not os.path.exists(self.file_path):
            return []

        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [Expense.from_dict(i) for i in data]
        except (json.JSONDecodeError, KeyError):
            return []