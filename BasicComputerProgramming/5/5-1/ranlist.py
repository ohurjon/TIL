import random


def make_nirand(n, begin=0, end=100):
    return [random.randint(begin, end) for i in range(0, 100)]


print(make_nirand(10, 99, 100))
