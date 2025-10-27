from datetime import date

def get_last_expense_id():
    try:
        with open("expenses.txt", "r") as f:
            lines = f.readlines()
            if not lines:
                return 0
            last_line = lines[-1]
            last_id = int(last_line.split(",")[0])
            return last_id
    except FileNotFoundError:
        return 0

def add_expense(amount, description, category):
    today = date.today()

    with open("expenses.txt", "a") as f:
        formatted_date = today.strftime("%Y-%m-%d")
        last_id = get_last_expense_id()
        new_id = last_id + 1
        f.write(f"{new_id},{formatted_date},{category},{description},{amount}\n")

    print(f"Expense added with ID: {new_id}")

def list_expenses():
    try:
        with open("expenses.txt", "r") as f:
            lines = f.readlines()
            if not lines:
                print("No expenses recorded.")
                return
            print("ID | Date       | Category | Description | Amount")
            print("-" * 50)
            for line in lines:
                expense_id, date_str, category, description, amount = line.strip().split(",")
                print(f"{expense_id} | {date_str} | {category} | {description} | R{amount}")
    except FileNotFoundError:
        print("No expenses recorded.")


def delete_expense(expense_id):
    try:
        with open("expenses.txt", "r") as f:
            lines = f.readlines()

        with open("expenses.txt", "w") as f:
            found = False
            for line in lines:
                current_id = line.split(",")[0]
                if current_id != str(expense_id):
                    f.write(line)
                else:
                    found = True

        if found:
            print(f"Expense with ID {expense_id} deleted.")
        else:
            print(f"No expense found with ID {expense_id}.")
    except FileNotFoundError:
        print("No expenses recorded.")


def summarize_expenses(month):
    if month is None:
        try:
            with open("expenses.txt", "r") as f:
                lines = f.readlines()
                total = 0.0
                for line in lines:
                    expense_id, date_str, category, description, amount = line.strip().split(",")
                    total += float(amount)
                print(f"Total expenses: R{total}")
        except FileNotFoundError:
            print("No expenses recorded.")
            return
    else:
        try:
            with open("expenses.txt", "r") as f:
                lines = f.readlines()
                total = 0.0
                for line in lines:
                    expense_id, date_str, category, description, amount = line.strip().split(",")
                    expense_month = int(date_str.split("-")[1])
                    if expense_month == month:
                        total += float(amount)
                print(f"Total expenses for month {month}: R{total}")
        except FileNotFoundError:
            print("No expenses recorded.")


