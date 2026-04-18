# Jessica's Weekly Expenses

# Function to check if input is a valid number (without using isdigit)
def is_number(value):
    if value == "":
        return False
    allowed = "0123456789."
    dot_count = 0
    for ch in value:
        if ch not in allowed:
            return False
        if ch == ".":
            dot_count += 1
            if dot_count > 1:
                return False
    return True


# Get user's name (retry if empty)
while True:
    name = input("Enter your name: ").strip()
    if name == "":
        print("Error, invalid name. Please try again.")
    else:
        break

# Get weekly budget (retry if invalid)
while True:
    budget_input = input("Enter your weekly budget: ").strip()
    if not is_number(budget_input):
        print("Error, invalid budget. Please enter a valid number.")
    else:
        budget = float(budget_input)
        break

# Categories
categories = [
    "Food & Drinks",
    "Transportation",
    "Mobile / Internet",
    "School Supplies",
    "Entertainment"
]

# Display categories using loop
print("\nExpense Categories:")
for i in range(len(categories)):
    print(f"{i+1}. {categories[i]}")
print("0. Skip")

entries = []
total_spent = 0

# Accept 4 entries
count = 0
while count < 4:
    print(f"\nEntry {count + 1}")
    
    choice_input = input("Choose category (0-5): ").strip()
    
    # Validate choice input
    if not is_number(choice_input):
        print("Error, invalid option.")
        continue
    
    choice = int(float(choice_input))
    
    if choice < 0 or choice > 5:
        print("Error, invalid option. Please retry.")
        continue
    
    if choice == 0:
        print("Skipped.")
        count += 1
        continue
    
    category = categories[choice - 1]
    
    # Get item description
    while True:
        item = input("Enter item description: ").strip()
        if item == "":
            print("Error, description cannot be empty.")
        else:
            break
    
    # Get amount spent
    while True:
        amount_input = input("Enter amount spent: ").strip()
        if not is_number(amount_input):
            print("Error, invalid amount.")
        else:
            amount = float(amount_input)
            break
    
    # Check for high expense
    alert = ""
    if amount >= (0.25 * budget):
        alert = " ! High Expense Alert!"
    
    entries.append((category, item, amount, alert))
    total_spent += amount
    count += 1

# Compute status
status = ""
if total_spent > budget:
    status = "Over Budget"
elif total_spent == budget:
    status = "On Budget"
else:
    status = "Under Budget"

# Display report
print("\n--- Weekly Expense Report ---")
print(f"Name: {name}")
print(f"Budget: {budget}")
print("\nEntries:")

for entry in entries:
    print(f"{entry[0]} - {entry[1]}: {entry[2]}{entry[3]}")

print(f"\nTotal Spent: {total_spent}")
print(f"Status: {status}")