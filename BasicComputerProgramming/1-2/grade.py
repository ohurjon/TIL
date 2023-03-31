credit = [3, 2, 3]
point = [4.5, 3.5, 4.0]

total = 0
credit_total = 0
for i in range(0, 3):
    total += credit[i] * point[i]
    credit_total += credit[i]

average = total/credit_total

print(average)