from services import ExpenseManager
import sys


def print_menu():
    print("\n--- 💰 PROFESSIONAL EXPENSE TRACKER ---")
    print("1. Add Expense")
    print("2. List All Expenses")
    print("3. Delete Expense")
    print("4. Total Spending")
    print("5. Edit Expense")
    print("6. Exit")
    print("---------------------------------------")


def amount_validation(prompt):
    while True:
        try:
            a = float(input(prompt))
            if a > 0.0:
                return a
            print("Invalid input. The amount must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    manager = ExpenseManager()

    while True:
        print_menu()
        choice = input("Select an option (1-6): ")

        if choice == "1":
            title = input("Enter the title: ").strip().title()
            categ = input("Enter the category: ").strip().title()
            if title and categ:
                amount = amount_validation("Enter the amount: ")
                manager.add_expense(title, amount, categ)
                print("✅ Expense added successfully!")
            else:
                print("❌ Title and category must not be empty!")

        elif choice == "2":
            all_expenses = manager.get_expenses()
            if not all_expenses:
                print("No expenses recorded.")
            else:
                print("\n--- Expense List ---")
                for i, exp in enumerate(all_expenses, 1):
                    print(f"{i}. {exp.title} | ${exp.amount:.2f} | {exp.category} | ID: {exp.id[:8]}")

        elif choice == "3":
            expense_id_snipp = input("Enter Expense ID (first 8 chars): ").strip()
            found = False
            for i in manager.get_expenses():
                if i.id.startswith(expense_id_snipp):
                    manager.delete_expense(i.id)
                    print(f"✅ '{i.title}' deleted successfully.")
                    found = True
                    break
            if not found:
                print("❌ The expense cannot be found.")

        elif choice == "4":
            total = manager.get_total_spending()
            print(f"\n💵 Current Total Spending: ${total:.2f}")

            summary = manager.category_summary()
            if summary:
                print("\n--- Spending by Category ---")
                for cat, amt in summary.items():
                    print(f" > {cat}: ${amt:.2f}")
            else:
                print("No expenses exist yet.")

        elif choice == "5":
            snippet = input("Enter Expense ID snippet to edit: ").strip()
            found_expense = None

            for i in manager.get_expenses():
                if i.id.startswith(snippet):
                    found_expense = i
                    break

            if not found_expense:
                print("❌ Expense not found.")
                continue

            print(f"\nEditing: {found_expense.title} (${found_expense.amount})")
            print("Leave blank to keep current value.")

            new_title = input(f"New title [{found_expense.title}]: ").strip().title()
            if not new_title:
                new_title = found_expense.title

            new_cat = input(f"New category [{found_expense.category}]: ").strip().title()
            if not new_cat:
                new_cat = found_expense.category

            new_amount = found_expense.amount
            raw_amount = input(f"New amount [{found_expense.amount}]: ").strip()

            if raw_amount:
                try:
                    val = float(raw_amount)
                    if val > 0:
                        new_amount = val
                    else:
                        print("Amount must be positive. Keeping original.")
                except ValueError:
                    print("Invalid number. Keeping original amount.")

            manager.edit_expense(found_expense.id, new_title, new_amount, new_cat)
            print("✅ Expense updated successfully!")

        elif choice == "6":
            print("Goodbye!")
            sys.exit(0)

        else:
            print("Invalid option! Please choose 1-6.")


if __name__ == "__main__":
    main()