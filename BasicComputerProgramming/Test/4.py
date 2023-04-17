import random  # 모듈 임포트


def findeven(lst):  # 형식 매개 변수
    idxs = []  # 짝수 데이터의 인덱스 저장을 위한 빈 리스트
    for i in range(len(lst)):  # 형식 매개 변수에 저장된 데이터 수 만큼 반복
        if lst[i] % 2 == 0:  # 데이터가 짝수인지 검사
            idxs.append(i)  # 짝수이면 리스트에 인덱스 저장
    return idxs  # 인덱스 저장한 리스트 반환


data = list()
for _ in range(10):
    data.append(random.randint(0, 20))  # 정수 난수 생성하여 리스트에 저장
idxs = findeven(data)
total = 0
for idx in idxs:
    total = total + data[idx]  # 짝수의 합을 계산
print(total, total / len(idxs))  # 짝수의 합과 평균 출력
