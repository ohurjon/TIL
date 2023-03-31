a = input("das")
s = 0
c = a.split(",")
for b in c:
    s += int(b)
print(s,"avg",s/len(c))