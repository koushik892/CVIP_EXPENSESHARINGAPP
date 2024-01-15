class ExpenseTracker:
    def __init__(self):
        self.balances = {}
        self.transactions = {}

    def add_expense(self, amount, reason, num_participants):
        individual_share = amount / num_participants

        for i in range(1, num_participants + 1):
            participant = f"Participant {i}"
            if participant not in self.balances:
                self.balances[participant] = 0
            self.balances[participant] += individual_share

        transaction_details = {
            'amount': amount,
            'participants': [f"Participant {i}" for i in range(1, num_participants + 1)],
            'reason': reason
        }
        self.transactions[len(self.transactions) + 1] = transaction_details

    def display_balances(self):
        print("User Balances:")
        for user, balance in self.balances.items():
            print(f"{user}: ${balance:.2f}")

    def display_transactions(self):
        print("\nTransaction Details:")
        for transaction_id, transaction in self.transactions.items():
            print(f"\nTransaction ID: {transaction_id}")
            print(f"Amount: ${transaction['amount']:.2f}")
            print(f"Participants: {', '.join(transaction['participants'])}")
            print(f"Reason: {transaction['reason']}")


def main():
    expense_tracker = ExpenseTracker()

    while True:
        print("\nOptions:")
        print("1. Add Expense")
        print("2. View Balances")
        print("3. View Transactions")
        print("4. Exit")

        choice = input("Enter your choice: ").lower()

        if choice == "1":
            amount = float(input("Enter the expense amount: "))
            reason = input("Enter the reason for the transaction: ")
            num_participants = int(input("Enter the number of friends to split: "))
            expense_tracker.add_expense(amount, reason, num_participants)

        elif choice == "2":
            expense_tracker.display_balances()
        elif choice == "3":
            expense_tracker.display_transactions()
        elif choice == "4":
            print("Exiting the expense tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
