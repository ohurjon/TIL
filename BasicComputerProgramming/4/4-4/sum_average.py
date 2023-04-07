lst = []

while True:
    a = int(input("integer(-1 for stop) ? "))
    if a < 0:
        break
    lst.append(a)

sum = 0

for i in lst:
    sum += i

print(f'Total = {sum:<10}', f'Average = {sum / len(lst):<10.2f}')
