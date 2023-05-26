import account as act
import random as rnd
import math


def to_radian(number):
    return number * math.pi / 180


n = 45

r = to_radian(n)

print(math.sin(r), math.cos(r), math.tan(r))

print(math.sin(r)*math.sin(r) + math.cos(r)*math.cos(r))
