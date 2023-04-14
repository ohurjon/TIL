import random

dic = {"kor": [], "eng": [], "mat": []}

for key in dic.keys():
    for i in range(3):
        dic[key].append(random.randint(0, 100))

totalScore = 0
for key in dic.keys():
    sumScore = 0
    for value in dic[key]:
        sumScore += value
    totalScore += sumScore
    print(key, sumScore)
print(totalScore)
