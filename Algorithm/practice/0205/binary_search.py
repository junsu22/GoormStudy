# 이진 탐색 알고리즘 구현


# 재귀적 방법
def binary_search_recursive(arr, target, left, right):
    if left > right:  # 탐색범위가 유효하지 않으면 (정확한 값 보장 못함)
        return False
    mid = (left + right) // 2  # 중간의 인덱스 계산(정수 나눗셈으로 중간 구하는 것)
    if arr[mid] == target:  # 중간값과 타겟 의 값이 같다면
        return True  # True 를 반환

    elif arr[mid] < target:  # 중간값이 타게보다 작으면 오른쪽 1
        return binary_search_recursive(arr, target, mid + 1, right)
        # 오른쪽 절반에서 재귀 탐색
    else:  # 중간값이 타겟보다 크면 왼쪽으로 1
        return binary_search_recursive(arr, target, left, mid - 1)
        # 왼쪽 절반에서 재귀 탐색


# 반복적 방법
def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1  # 시작과 끝 인덱스 초기화

    while left <= right:  # 탐색범위가 유효할 동안 순회할 반복문
        mid = (left + right) // 2  # 중간 인덱스 계산
        if arr[mid] == target:  # 중간값과 타겟값이 같다면
            return True  # True 를 반환
        elif arr[mid] < target:  # 중간값이 타겟보다 작으면
            left = mid + 1  # left를 오른쪽으로 이동(오른쪽으로 범위좁히기)
        else:
            right = mid - 1  # right 를 왼쪽으로 이동(왼쪽으로 범위 좁히기)

    return False
