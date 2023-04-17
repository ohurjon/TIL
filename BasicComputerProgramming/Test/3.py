def partion(lst):
    target = lst[0]  # 리스트의 첫 번째 원소가 비교 대상
    gidx = 0  # 비교를 시작할 첫 번째 원소의 인덱스
    while gidx < len(lst):
        if lst[gidx] > target:  # target보다 큰 값의 리스트 원소를 찾은 경우
            break  # 반복문을 중단하고 빠져 나감.
        gidx += 1
    lidx = len(lst) - 1  # 비교를 시작할 가장 마지막 원소의 인덱스
    while lidx > 0:
        if lst[lidx] < target:  # target보다 작은 값의 리스트 원소를 찾은 경우
            break  # 반복문을 중단하고 빠져 나감.
        lidx -= 1
    return gidx, lidx  # gidx와 lidx를 반환


data = [93, 17, 95, 48, 86, 15, 10, 3, 42, 64]
print(partion(data))
