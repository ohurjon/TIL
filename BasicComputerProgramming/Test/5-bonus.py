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

for i in range(len(data)):
    idx = findminpos(data[i:])
    swap(data, i, idx + i)
print(data)
