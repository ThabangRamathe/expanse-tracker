import argparse
import expense_process

def add(description, amount):
    expense_process.add_expense(amount, description, "Unknown")

def list():
    expense_process.list_expenses()

def delete(id):
    expense_process.delete_expense(id)

def summary(month):
    expense_process.summarize_expenses(month)

def check_positive(value):
    try:
        ivalue = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"{value} is not a valid number")
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(f"{value} is not a positive number")
    return ivalue

parser = argparse.ArgumentParser(description="An expanse tracker CLI")
sub_parser = parser.add_subparsers(dest="subcommands")

add_parser = sub_parser.add_parser("add")
add_parser.add_argument("--description", "-d", type=str, required=True)
add_parser.add_argument("--amount", type=check_positive, required=True)
add_parser.set_defaults(func=add)

list_parser = sub_parser.add_parser("list")
list_parser.set_defaults(func=list)

del_parser = sub_parser.add_parser("delete")
del_parser.add_argument("--id", type=int, required=True)
del_parser.set_defaults(func=delete)

summary_parser = sub_parser.add_parser("summary")
summary_parser.add_argument("--month", type=int, choices=range(1, 13))
summary_parser.set_defaults(func=summary)


args = parser.parse_args()
if hasattr(args, "func"):
    kwargs = {k: v for k, v in vars(args).items() if k not in ("subcommands", "func")}
    args.func(**kwargs)
else:
    parser.print_help()
# print(args.func())
