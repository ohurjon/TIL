import random

tup = ()
a = 0
for i in range(100):
    tup += (random.randint(0,100),)

for v in tup:
    if v & 1 == 1:
        a += 1
print(tup, a, sep="\n")