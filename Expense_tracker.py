import json
DATA_FILE = "expenses.json"
def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    try:
        amount = float(input("Enter amount spent: "))
        category = input("Enter category (e.g., food, transport, entertainment): ").lower()
        description = input("Enter a brief description: ")
        expenses.append({"amount": amount, "category": category, "description": description})
        save_data(expenses)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input. Please enter a valid amount.")

def view_summary(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    total_expense = sum(exp["amount"] for exp in expenses)
    print(f"\nTotal Expenses: ${total_expense:.2f}\n")

  
    categories = {}
    for exp in expenses:
        categories[exp["category"]] = categories.get(exp["category"], 0) + exp["amount"]

    print("Category-wise Expenses:")
    for category, total in categories.items():
        print(f"  {category.capitalize()}: ${total:.2f}")

def main():
    print("\nExpense Tracker")
    expenses = load_data()

    while True:
        print("\nOptions:")
        print("1. Add Expense")
        print("2. View Expense Summary")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_summary(expenses)
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
