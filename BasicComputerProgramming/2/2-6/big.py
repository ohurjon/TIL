big = -1


def numberGetter(s):
    a = int(input(s + "number ? : "))
    if a < 0:
        return numberGetter(s)
    return a


for i in range(1, 6):
    d = numberGetter(str(i))

    if d >= big:
        big = d

print(big)
