class Account:
    MAX_AMOUNT_PER_TRANSACTION = 10000
    balance = 0
    name = ""

    def __init__(self, money):
        self.balance = money

    def __str__(self):
        return f'current balance : {self.balance}'

    def get_balance(self):
        return self.balance

    def deposit(self, money):
        if money < Account.MAX_AMOUNT_PER_TRANSACTION:
            self.balance += money
        else:
            print("Error")

    def withdraw(self, money):
        if money < Account.MAX_AMOUNT_PER_TRANSACTION:
            self.balance -= money
        else:
            print("Error")


user = Account(10000)
user.withdraw(100215123)

print(str(user))
