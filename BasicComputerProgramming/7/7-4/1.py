class Account:
    MAX_AMOUNT_PER_TRANSACTION = 10000

    def __init__(self, money=0):
        self.__balance = money

    def __str__(self):
        return f'current balance : {self.__balance}'

    def get_balance(self):
        return self.__balance

    def deposit(self, money):
        if money < Account.MAX_AMOUNT_PER_TRANSACTION:
            self.__balance += money
        else:
            print("Error")

    def withdraw(self, money):
        if money < Account.MAX_AMOUNT_PER_TRANSACTION:
            self.__balance -= money
        else:
            print("Error")


class IdentifiedAccount(Account):
    def __init__(self, *, id):
        super().__init__()
        self.__id = id

    def get_id(self):
        return self.__id


class MinusAccount(Account):

    def __init__(self, contracted_balance=0, contracted_balance_withdrawal=0):
        super().__init__(contracted_balance)
        self.__contracted_balance = contracted_balance
        self.__contracted_balance_withdrawal = contracted_balance_withdrawal

    def get_available_balance(self):
        return super().get_balance() + (self.__contracted_balance - self.__contracted_balance_withdrawal)

    def deposit(self, money):
        pass
    def withdraw(self, money):
        pass

user = Account(10000)
user.withdraw(100)

print(str(user))
