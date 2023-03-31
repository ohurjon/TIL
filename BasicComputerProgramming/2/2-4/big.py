n1 = int(input("n1??"))
n2 = int(input("n2??"))
n3 = int(input("n3??"))

print(n1 if n1 >= n2 and n1 >= n3 else n2 if n2 >= n3 else n3)
