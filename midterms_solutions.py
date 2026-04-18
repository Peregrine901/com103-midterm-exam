# Jessica's Weekly Expenses Tracker

# Ask for name
while True:
    name = input("Enter your name: ").strip()
    if name != "":
        break
    else:
        print("Name cannot be empty. Please try again.")

# Ask for weekly budget
while True:
    budget_input = input("Enter your weekly budget: ").strip()
    if budget_input != "" and all(c in "0123456789." for c in budget_input):
        budget = float(budget_input)
        break
    else:
        print("Error, invalid budget. Please enter a number.")

# Expense categories
categories = [
    "Food & Drinks       [e.g. Lunch, snacks, coffee]",
    "Transportation      [e.g. Bus, jeepney, ride-share]",
    "Mobile / Internet   [e.g. Load, data plan, WiFi top-up]",
    "School Supplies     [e.g. Notebook, pen, bond paper]",
    "Entertainment       [e.g. Games, movies, hangout]"
]

# Display categories
print("\nExpense Categories:")
for idx, cat in enumerate(categories, 1):
    print(f"{idx}. {cat}")

# Record expenses
expenses = []
entry_count = 0
while entry_count < 4:
    option_input = input(f"\nSelect a category (1-5) or 0 to skip: ").strip()
    if option_input == "0":
        entry_count += 1
        continue
    elif option_input in ["1", "2", "3", "4", "5"]:
        category_index = int(option_input) - 1
        category_name = categories[category_index].split("       ")[0]

        # Get item description
        while True:
            item = input(f"Enter short description for {category_name}: ").strip()
            if item != "":
                break
            else:
                print("Description cannot be empty.")

        # Get amount spent
        while True:
            amount_input = input(f"Enter amount spent for {item}: ").strip()
            if amount_input != "" and all(c in "0123456789." for c in amount_input):
                amount = float(amount_input)
                break
            else:
                print("Error, invalid amount. Please enter a number.")

        expenses.append((category_name, item, amount))
        entry_count += 1
    else:
        print("Error, invalid option. Please select a valid category (0-5).")

# Print expense report
print("\n--- Jessica's Weekly Expense Report ---")
total_spent = 0
for cat, item, amount in expenses:
    high_alert = ""
    if amount >= 0.25 * budget:
        high_alert = "! High Expense Alert!"
    print(f"{cat}: {item} - ${amount:.2f} {high_alert}")
    total_spent += amount

# Print summary
print(f"\nTotal spent: ${total_spent:.2f}")
if total_spent > budget:
    print("Status: Over budget!")
else:
    print("Status: Within budget")