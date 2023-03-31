
year = int(input('년도 입력 : '))


def leaf(i):
    return i % 4 != 0 or (i % 100 == 0 and i % 400 != 0)


if leaf(year):
    print('평년')
else:
    print('윤년')

