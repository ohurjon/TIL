def findminpos(lst):
    idx = 0  # 가장 작은 값의 인덱스를 0이라고 하자.
    for i in range(len(lst)):  # 형식 매개변수를 통해 전달받은 리스트에 대해 반복
        if lst[idx] > lst[i]:  # 인덱스 idx의 데이터 값보다 더 작은 값인지 검사
            idx = i  # 인덱스 idx의 데이터 값보다 더 작은 값이면 i가 새로운 idx
    return idx


def swap(lst, idx1, idx2):  # 매개변수는 하나의 리스트와 두 개의 인덱스
    tmp = lst[idx1]
    lst[idx1] = lst[idx2]
    lst[idx2] = tmp  # 리스트의 인덱스 idx1의 값과 idx2의 값을 교환


data = [29, 57, 64, 23, 40, 79, 86, 38, 5, 15]
print(data)
idx = findminpos(data)  # 리스트 전체에서 가장 작은 값의 인덱스 찾기
swap(data, 0, idx)  # 리스트의 첫 번째 값과 idx의 위치에 저장된 값을 교환
print(data)
idx = findminpos(data[1:])  # 리스트의 두 번째 데이터부터 끝까지를 대상으로
# 그 중에 가장 작은 값의 인덱스 찾기
swap(data, 1, idx + 1)  # 리스트에서 두 번째로 큰 값과 인덱스 1의 값을 교환
print(data)
