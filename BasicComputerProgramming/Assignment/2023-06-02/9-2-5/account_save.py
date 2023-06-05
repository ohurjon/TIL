from utility.account import IdentifiedAccount

account = IdentifiedAccount(id=123, money=1000)

account.deposit(500)

file = open("account.dat", "w")

file.write(str(account.get_id()) + " ")
file.write(str(account.get_balance()))

file.close()
