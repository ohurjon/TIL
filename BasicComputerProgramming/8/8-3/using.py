from util.bits.operation import setBitValue

from util.arth import statistics, basics

n = 0b0101

n = setBitValue(n, 1)

print(bin(n))

lst = [1, 2, 3, 4, 5]

total = basics.gettotal(lst)
avg = statistics.mean(lst)

print(total, avg)
