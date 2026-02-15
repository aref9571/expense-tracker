import uuid
from dataclasses import dataclass , field
from datetime import datetime

@dataclass
class Expense:

    title : str
    amount : float
    category : str
    id : str = field(default_factory= lambda : str(uuid.uuid4()))
    created_at : str = field(default_factory= lambda : (datetime.now().isoformat()))

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "id" : self.id,
            "amount" : self.amount,
            "category": self.category,
            "created_at" : self.created_at
        }

    @classmethod
    def from_dict(cls , data : dict) -> 'Expense':
        return cls (
            title=data["title"],
            id = data["id"],
            amount=data["amount"],
            category=data["category"],
            created_at=data["created_at"]
        )
