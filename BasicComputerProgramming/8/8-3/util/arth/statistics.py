from util.arth.basics import gettotal


def mean(lst):
    total = gettotal(lst)
    return total / len(lst)


print(__name__)
