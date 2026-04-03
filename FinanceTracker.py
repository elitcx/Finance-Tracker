def get_balance():
    global balance
    try:
        with open(r"FinanceTracker.txt", "r") as file:
            lines = file.readlines()
            for line in reversed(lines):
                if line.startswith("Balance: "):
                    balance = float(line.strip().split(": ")[1])
                    return balance
            balance = 0.0  # If no balance line found
    except FileNotFoundError:
        balance = 0.0
    except ValueError:
        print("Error reading balance from file. Setting balance to 0.0.")
        balance = 0.0
    return balance

def menu():
    while True:
        print("Welcome to the Finance Tracker!")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. Exit")
        choice = input("Please select an option (1-4): ")
        if choice in ["1", "2", "3", "4"]:
            return choice
        else:
            print("Invalid choice. Please select a valid option (1-4).")

def get_date():
    while True:
        date = input("Enter the date (DD/MM/YY): ")
        dates = date.split("/")
        if len(dates) != 3:
            raise ValueError("Invalid date format. Please use DD/MM/YY.")
        try:
            day = int(dates[0])
            month = int(dates[1])
            year = int(dates[2])
            if not (1 <= day <= 31 and 1 <= month <= 12 and year > 0):
                raise ValueError("Invalid date. Please enter a valid date.")
            return f"{day:02}/{month:02}/{year:02}"
        except ValueError:
            print("Invalid date. Please enter a valid date.")

def add_income():
    while True:
        income = input("Enter the income amount: ")
        reason = input("Enter the reason for income: ")
        try:
            income = float(income)
            global balance
            balance += income
            if income < 0:
                raise ValueError("Income cannot be negative.")
            return income, reason, balance
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def add_expense():
    while True:
        expense = input("Enter the expense amount: ")
        reason = input("Enter the reason for expense: ")
        try:
            expense = float(expense)
            global balance
            balance -= expense
            if expense < 0:
                raise ValueError("Income cannot be negative.")
            return expense, reason, balance
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    global balance
    balance = get_balance()
    file.write(get_date() + ("\n" * 2))
    
    # Initialize income and expense to avoid UnboundLocalError
    income = 0.0
    expense = 0.0

    while True:
        menu_choice = menu()
        if menu_choice == "1":
            income, reason, balance = add_income()
            file.write(f"Income: {income}\n")
            file.write(f"Reason of income: {reason}\n")
        if menu_choice == "2":
            expense, reason, balance = add_expense()
            file.write(f"Expense: {expense}\n")
            file.write(f"Reason of expense: {reason}\n")
        if menu_choice == "3":
            file.seek(0)
            print('\n' + file.read())
        if menu_choice == "4":
            break

    file.write(f"Net income: {income - expense}\n")
    file.write(f"Balance: {balance}\n\n")
    print(f"Your current balance is: {balance}")

while True:
    balance = get_balance()
    file = open(r"FinanceTracker.txt", "a+")
    main()
    again = input("Do you want to continue? (yes/no): ").strip().lower()
    if again not in ['yes','y','yea','again', 'try again','continue','sure','go']:
        print("Exiting the Program. Goodbye!")
        break
file.close()