count = 0

for i in range(0, 4):
    if i & (1 << 1) != 0:
        count += 1

print(count)
