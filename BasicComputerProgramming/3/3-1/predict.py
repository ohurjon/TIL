number = 0
for i in range(0, 4):
    for n in range(1, 16):
        if n & 1 << i:
            print(n, end=" ")
    if str(input("존재합니까? y/n ")) == "y":
        number |= 1 << i
print("정답은!", number)