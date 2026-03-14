class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount

    def show_expenses(self):
        if len(self.expenses) == 0:
            print("No expenses has been recorded yet!")
        else:
            for category in self.expenses:
                print(f"{category:<14} = ${self.expenses[category]}")
            print("-----------------------")
                      
            total_spent= 0
            for amount in self.expenses.values():
                total_spent += amount
            print(f"{"Total spent":<14} = ${total_spent}")

tracker = ExpenseTracker()

while True:
    print("""
1 Add expense
2 View total spending by category
3 Exit
    """)
    
    choice = input("\nChoose option: ")

    if choice == "1":
        category = input("Enter category: ").capitalize()
        amount = float(input("Enter amount: $"))
        tracker.add_expense(category, amount)
        
    elif choice == "2":
           tracker.show_expenses()

    elif choice == "3":
        print("Good bye.")
        break

    else:
        print("I do not understand. \nChoose between 1-3.")
