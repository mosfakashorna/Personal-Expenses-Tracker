expenses = {}

print("""
1 Add expense
2 View total spending by category
3 Exit
""")

while True:

    choice = input("\nChoose option: ")
    print()

    if choice == "1":
        category = input("Enter category: ").capitalize()
        amount = float(input("Enter amount: $"))
        if category in expenses:
            expenses[category] += amount
        else:
            expenses[category] = amount

    elif choice == "2":
        if len(expenses) == 0:
            print("No expense has redored yet.")
        else:
            for category in expenses:
                print(f"{category:<14} = ${expenses[category]}")
            print("--------------------------")

            total_spent = 0
            for amount in expenses.values():
                total_spent += amount

            print(f"{"Total spent":<14} = ${total_spent}")

    elif choice == "3":
        print("Good bye.")
        break

    else:
        print("I do not understand. \nChoose between (1-4).")
