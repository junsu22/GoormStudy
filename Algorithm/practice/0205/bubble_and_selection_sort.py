# ===============================
# Bubble Sort (버블정렬)
# ===============================


# 버블정렬 구현
def bubble_sort(arr):
    n = len(arr)  # 배열의 길이를 정함.
    for i in range(n):  # n번 반복
        for j in range(0, n - i - 1):  # 정렬이 안된부분을 비교한다.
            if arr[j] > arr[j + 1]:  # j와 j+1 번째 원소를 비교한다.
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # 값이 크다면 뒤로 보내준다.
    return arr


# 예시 배열
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array is : ", arr)

# ---------------------------------------------


# ===============================
# Selection Sort (선택정렬)
# ===============================


# 예시 배열
def selection_sort(arr):
    """선택 정렬: 매번 최솟값을 찾아 앞으로 이동"""
    n = len(arr)
    for i in range(n):  # i번째 위치에 올 값 찾기
        min_idx = i  # 현재 위치를 최솟값으로 가정
        for j in range(i + 1, n):  # i 이후 구간에서 최솟값 탐색
            if arr[j] < arr[min_idx]:  # 더 작은 값 발견
                min_idx = j  # 최솟값 인덱스 갱신
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # 최솟값을 i번째로 이동
    return arr
    
# 예시 배열
# arr = [64, 34, 25, 12, 22, 11, 90]
# selection_sort(arr)
# print("Sorted array is : ", arr)


# Sorted array is :  [11, 12, 22, 25, 34, 64, 90]
