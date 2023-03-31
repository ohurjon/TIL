a1 = input("name1 ?")
b1 = int(input("score1 ?"))
a2 = input("name2 ?")
b2 = int(input("score2 ?"))

print(f"{a1:>10} : {'*'*(b1//10)}({b1})")
print(f"{a2:>10} : {'*'*(b2//10)}({b2})")
