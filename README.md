"# expanse-tracker" 
## Description
The Expense Tracker CLI is a Python-based command-line tool designed to help users track their expenses.

My attempt at the [Expense Tracker](https://roadmap.sh/projects/expense-tracker) project featured on [roadmap.sh](https://roadmap.sh/)
## Features
- Add Expenses: Easily add new expenses with details such as amount, category, and description.
- Delete Expenses: Delete an expense based on its ID.
- View Expenses: Display a list of all recorded expenses.
- Categorize Expenses: Organize expenses into different categories for better tracking.
- Generate Reports: Create summary reports of expenses over a specified period.

## Prerequisites
- Python 3.6+

## Usage
Default usage
```bash
python expense-tracker.py -h # Show help
python expense-tracker.py add --description "Lunch" --amount 20 # Add an expense
python expense-tracker.py add --description "Dinner" --amount 10 # Add another expense
python expense-tracker.py list # List all expenses 
python expense-tracker.py summary # Show summary of expenses
python expense-tracker.py delete --id 2 # Delete an expense by ID
python expense-teacker.py summary --month 8 # Show summary of expenses for specific month
```
Windows (custom command)
```bash
expense-tracker -h # Show help
expense-tracker add --description "Lunch" --amount 20 # Add an expense
expense-tracker add --description "Dinner" --amount 10 # Add another expense
expense-tracker list # List all expenses 
expense-tracker summary # Show summary of expenses
expense-tracker delete --id 2 # Delete an expense by ID
expense-teacker summary --month 8 # Show summary of expenses for specific month
```
