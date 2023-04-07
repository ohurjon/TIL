list = [9,15,4,5,3,13,7,8,18,11]

max = list[0]
min = list[0]
odd = 0

for i in list:
    if max < i:
        max = i
    if min > i:
        min = i
    if i%2 != 0:
        odd += 1

print(max,min,odd)