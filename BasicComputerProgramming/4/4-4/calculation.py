text = '12 3 10 + *'

chars = text.split(" ")

lst = []

for char in chars:
    if char.isdigit():
        lst.append(int(char))
    else:
        a = lst.pop()
        b = lst.pop()
        lst.append(a+b if char =="+" else a*b)
print(lst[0])