print("Welcome to Ahmad's Expense Tracker!")
print("Hello from Umair!")

def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category: ")
    with open("expenses.txt", "a") as f:
        f.write(f"{category}: {amount}\n")

def view_expenses():
    with open("expenses.txt", "r") as f:
        print(f.read())

def delete_expenses():
    open("expenses.txt", "w").close()
    print("All expenses deleted.")

print("1. Add Expense")
print("2. View Expenses")
print("3. Delete All Expenses")

choice = input("Choose: ")

if choice == "1":
    add_expense()
elif choice == "2":
    view_expenses()
elif choice == "3":
    delete_expenses()
    print("Thanks for using our expense tracker!")
