import csv
from datetime import datetime

FILENAME = 'expenses.csv'
FIELDS = ['Date', 'Category', 'Amount', 'Description']

def add_expense():
    date = datetime.now().strftime('%Y-%m-%d')
    category = input("Category: ")
    amount = input("Amount: ")
    description = input("Description (optional): ")
    
    with open(FILENAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    
    print("✅ Expense added!")

def view_summary():
    totals = {}
    with open(FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cat = row['Category']
            amt = float(row['Amount'])
            totals[cat] = totals.get(cat, 0) + amt
    
    print("\n💰 Summary by Category:")
    for cat, amt in totals.items():
        print(f"{cat}: ${amt:.2f}")

def menu():
    print("\n--- Budget Tracker ---")
    print("1. Add Expense")
    print("2. View Summary")
    print("3. Exit")
    
    choice = input("Choose: ")
    if choice == '1':
        add_expense()
    elif choice == '2':
        view_summary()
    elif choice == '3':
        exit()
    else:
        print("Invalid choice.")

if __name__ == '__main__':
    # Create file with headers if it doesn't exist
    try:
        with open(FILENAME, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(FIELDS)
    except FileExistsError:
        pass

    while True:
        menu()
