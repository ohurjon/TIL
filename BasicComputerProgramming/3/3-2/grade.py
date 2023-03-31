while True :
    grade = int(input("성적을 입력하세요."))
    if range(0,101) in grade:
        print(grade / 10)
        break