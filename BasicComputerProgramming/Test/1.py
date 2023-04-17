year = int(input(" input year : "))
# 윤년 여부를 결정하기 위한 조건식
if (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0):
    print('not leap year ')  # 윤년 아님
else:
    print('leap year ')  # 윤년
