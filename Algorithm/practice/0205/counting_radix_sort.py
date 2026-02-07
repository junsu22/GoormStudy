# 계수 정렬 CountingSort
# 기수정렬 RadixSort


# 계수정렬
def counting_sort(arr, exp1):  #  특정 자리수를 기준을 정렬하는 함수
    n = len(arr)  # 배열의 길이
    output = [0] * n  # 정렬된 결과를 저장 할 배열
    count = [0] * (10)  # 0 ~ 9 까지 각 숫자의 개수를 세는 배열
    # 현재의 자릿수의 숫자 빈도를 계산
    for i in range(0, n):
        index = arr[i] // exp1  # 인덱스를 exp1로 나눠서 해당 자릿수 추출
        count[index % 10] += 1  # 현재 숫자 0~ 9 개수 증가
    # 횟수를 누적합 으로    (정럴 후 위치 계산)
    for i in range(1, 10):  # 0 ~ 9 까지
        count[i] += count[i - 1]
    # 뒤에서 부터 순회하며 output 배열에 안정 정렬
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1  # 인덱스를 exp1로 나눠서 해당 자릿수 추출
        output[count[index % 10] - 1] = arr[i]  # 올바른 위치에 배치
        count[index % 10] -= 1  # 해당 숫자의 카욵트가 감소함
        i -= 1

    # 정렬된 결과를 원본 배열에 복사
    for i in range(0, len(arr)):
        arr[i] = output[i]


# 기수 정렬
def radix_sort(arr):
    max1 = max(arr)  # 배열의 최댓값
    exp = 1  # 1의 자리부터 시작
    # 최댓값의 자릿수 만큼 반복
    while max1 // exp > 0:
        counting_sort(arr, exp)  # 현재 자릿수를 기준으로 정렬
        exp *= 10  # 10의 자리로 이동   1,10,100


arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print(arr)


# [2, 24, 45, 66, 75, 90, 170, 802]
