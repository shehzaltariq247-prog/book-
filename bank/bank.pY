"""OOP in Python - simple Bank class."""

class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            print("Withdrawal successful. Balance is:", self.balance)
        else:
            print("Insufficient funds")

    def deposit(self, amount):
        self.balance += amount
        print("Deposited amount successfully. Balance is:", self.balance)


if __name__ == "__main__":
    # creating objects and testing methods
    b1 = Bank("zainab", 500000)
    b1.withdraw(2000)



