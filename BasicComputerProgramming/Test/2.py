fns = {}  # 빈 딕셔너리를 생성


def gettotal(*data):  # 형식 매개 변수
    total = 0
    for v in data:  # 형식 매개변수에 저장된 데이터 수 만큼 반복
        total += v  # 합을 구함
    return total


def getaverage(*data):  # 위 1번과 동일, 이름은 달라도 됨.
    total = 0
    for v in data:  # 형식 매개변수에 저장된 데이터 수 만큼 반복
        total += v  # 합을 구함
    return total / len(data)  # 평균을 반환


fns['sum'] = gettotal  # 딕셔너리 fns에 ‘sum’을 키로 하여 gettotal() 함수 저장
fns['avg'] = getaverage  # 딕셔너리 fns에 ‘avg’를 키로 하여 getaverage() 함수 저장
print(fns['sum'](1, 2, 3, 4, 5))  # 1, 2, 3, 4, 5를 실인자로 하여 fns 딕셔너리에저장된 ‘sum’ 함수 호출
print((fns['avg'](1, 3, 5)))  # 1, 3, 5를 실인자로 하여 fns 딕셔너리에 저장된 ‘avg’함수 호출
