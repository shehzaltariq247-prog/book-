class bank:
    def __init__(self, holder_name, account_number, balance):
        self.holder_name = holder_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f" deposit successful. new balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal successful. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount.")


if __name__ == "__main__":
    account = bank("shehzal", 123456789, 5000)
    account.deposit(1000)
    account.withdraw(2000)
