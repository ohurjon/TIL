n = int(input("n??"))

print(n - ((n >> 1) << 1) == 1)
print(n & 1 == 1)

