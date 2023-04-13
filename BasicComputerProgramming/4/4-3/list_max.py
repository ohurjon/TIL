lst = [18, 15, 4, 5, 3, 13, 7, 8, 9, 11]

for i in range(len(lst)):
    a = i
    for j in range(i, len(lst)):
        if lst[a] < lst[j]:
            a = j
    b = lst[a] - lst[i]
    lst[i] = lst[a]
    lst[a] = lst[a] - b
print(lst)
