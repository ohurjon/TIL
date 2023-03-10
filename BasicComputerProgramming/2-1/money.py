money = int(input("money?\n"))

print(money - money % 1000)

print("50,000 :", money//50000)
print("10,000 :", (money % 50000) // 10000)
print("5,000 :", ((money % 50000) % 10000) // 5000)
print("1,000 :", (((money % 50000) % 10000) % 5000)//1000)
