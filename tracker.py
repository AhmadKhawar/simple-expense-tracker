print("Welcome to Ahmad's Expense Tracker!")

def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category: ")
    with open("expenses.txt", "a") as f:
        f.write(f"{category}: {amount}\n")

def view_expenses():
    with open("expenses.txt", "r") as f:
        print(f.read())

print("1. Add Expense")
print("2. View Expenses")

choice = input("Choose: ")

if choice == "1":
    add_expense()
elif choice == "2":
    view_expenses()