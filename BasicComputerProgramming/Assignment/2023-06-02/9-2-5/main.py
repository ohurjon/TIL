from utility.account import IdentifiedAccount

file = open("account.dat", "r")

data = file.readline().split(" ")

account = IdentifiedAccount(id=data[0], money=data[1])

print("id " + account.get_id())
print("money " + account.get_balance())
