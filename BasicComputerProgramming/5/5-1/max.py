import random
def max(a, b):
    return b if a < b else a

data = [(random.randint(0,10),random.randint(0,10)) for _ in range(10)]

print(data)
print([max(a,b) for a,b in data])
