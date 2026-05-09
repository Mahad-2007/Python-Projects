expenses = []
print("Welcome to this Restaurant")

while True:
    print("<<=== MENU ===>>")
    print("1. Add your expenses")
    print("2. View all expenses")
    print("3. Total expenses amount")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        date = input("Enter your date of expenses: ")
        category = input("Enter the category of expenses: ")
        description = input("Enter the description of expenses: ")
        amount = int(input("Enter the amount of expenses: "))

        dictionary = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(dictionary)

    elif choice == 2:
        count = 1
        for x in expenses:
            print(f"Expense no {count}: {x['date']}, {x['category']}, {x['description']}, {x['amount']}")
            count += 1

        print("These are your expenses!")

    elif choice == 3:
        if len(expenses) == 0:
            print("No expense")
        else:
            total = 0
            for x in expenses:
                total += x['amount']
            print("Total amount:", total)

    elif choice == 4:
        print("Exit this menu")
        break

    else:
        print("Invalid Number for menu")