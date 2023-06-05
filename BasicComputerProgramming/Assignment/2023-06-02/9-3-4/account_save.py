from utility.account import IdentifiedAccount

account = IdentifiedAccount(id=123, money=1000)

account.deposit(500)

file = open("account.bin", "wb")

file.write((str(account.get_id())+" ").encode())

file.write(str(account.get_balance()).encode())

file.close()
