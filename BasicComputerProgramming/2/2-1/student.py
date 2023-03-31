data = [["아무개", "31"], ["뭐시기", "92"]]

for i in data:
    print(i[0], ":", "*" * (int(i[1]) // 10))


