n1 = int(input("n1 ??"))
n2 = int(input("n2 ??"))
n3 = int(input("n3 ??"))

size = 0

size += n1 % 2
size += n2 % 2
size += n3 % 2

print(3-size)
