from expense import Expense

def main():
    print("🎯 Running expenses tracker!\n")
    expenses_file_path = r'C:\Users\loure\Desktop\Projetos programação\Python\Expense tracker\expenses.csv'

    #Get user input
    expense = get_user_expense()

    #Save expense to file
    save_expense_to_file(expense, expenses_file_path)

    #Summarize expenses
    summarize_expense(expenses_file_path) 

def get_user_expense():
    print("🎯 Getting user expense\n")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    expense_categories = ["Home", "Food", "Subscriptions", "Fun", "Clothes", "Others"]
    
    while True:
        print("Select the expense category: ")
        for i, category_name in enumerate(expense_categories):
            print(f" {i+1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        category_index = int(input(f"Select a category {value_range}: ")) - 1

        if category_index in range(0, len(expense_categories)):
            selected_category = expense_categories[category_index]
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        else:
            print("Invalid category.\n")

def save_expense_to_file(expense : Expense, file_path):
    print(f"\n🎯 Saving to file: {expense}\n")
    with open(file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")

def summarize_expense(file_path):
    print("🎯 Summarizing expenses\n")
    expenses = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(',')
            line_expense = Expense(name=expense_name, amount = float(expense_amount), category=expense_category)
            expenses.append(line_expense)

    #Create expenses amount by caregory dictionary
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("📊 Expenses By Category")
    for key, amount in amount_by_category.items():
        print(f"{key}: €{amount:.2f}")

if __name__ == "__main__":
    main()