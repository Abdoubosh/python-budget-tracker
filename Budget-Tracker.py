import json
try:
    with open ("expenses.json", "r") as file:
        expenses = json.load(file)
except FileNotFoundError:
    expenses = []


def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)


while True:
    print("\n1-Add expense")
    print("2-View expenses")
    print("3-Show total")
    print("4-Delete expenses")
    print("5-Delete all expenses")  
    print("6-Exit")

    choice = input("Choose an option:")

    if choice == "1":
        name = input("Enter expense name: ").strip()
        try:
            amount = float(input("Enter expense amount: "))
        except ValueError:
            print("The amount can only be a number")
            continue
        if name:
            expense = {
                "name": name, 
                "amount": amount 
            }
            expenses.append(expense)
            save_expenses()
            print("Expense added successfully")
        else:
            print("Name cannot be empty")

    elif choice == "2":
        if not expenses:
            print("There are no expenses yet")
        else:
            for i, expense in enumerate(expenses, 1):
                print (i, "-", expense["name"], ":", expense["amount"], "$")

    elif choice == "3":
        total = 0
        for expense in expenses:
            total += expense["amount"]
        print("Total spent:", total, "$")

    elif choice == "4":
        if not expenses:
            print("There are no expenses to delete")
        else:
            for i, expense in enumerate(expenses, 1):
                print(i, "-", expense["name"], ":", expense["amount"], "$")
            deletion_choice = input("Choose an expense number to delete or type 'exit' to exit: ").strip().lower()
            if deletion_choice == "exit":
                continue
            try:
                expense_number = int(deletion_choice)
                if 1 <= expense_number <= len(expenses):
                    expenses.pop(expense_number -1)
                    save_expenses()
                    print("Expense deleted successfully")
                    if not expenses:
                        print("No expense left")
                    else:
                        for i, expense in enumerate(expenses, 1):
                            print(i, "-", expense["name"], ":", expense["amount"], "$")
                else:
                    print("Invalid expense number")    
            except ValueError:
                print("Please Enter a valid number")      

    elif choice == "5":
        if not expenses:
            print("There are no expenses to delete")
        else:
            for i, expense in enumerate(expenses, 1):
                print(i, "-", expense["name"], ":", expense["amount"], "$")
            confirmation = input("Type 'confirm' to confirm").strip().lower()
            if confirmation == "confirm":
                expenses.clear()
                save_expenses()
                print("All expenses have been deleted successfully")
            else:
                print("Deletion cancelled")

    elif choice == "6":
        break
    else:
        print("Invalid choice")
    