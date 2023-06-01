import random

def max(x,y):
    return x if x>y else y

data = [(random.randint(0,10), random.randint(0,10)) for _ in range(10)]

print(data)

large_value = [max(x,y) for x,y in data]

print(large_value)