number = int(input("number?"))


for i in range(0, 8):
    if i & (1 << number):
        print(i)
