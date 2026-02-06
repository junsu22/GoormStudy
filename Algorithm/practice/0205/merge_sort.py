# 병합정렬
# [38, 27, 43, 3, 9, 82, 10]


# 함수 객체 생성.
def merge_sort(arr):
    # merge_sort라는 이름이 객체를 가리킨다.

    if len(arr) > 1:  # arr 길이가 1보다 크면 (더 나눌 수 있음)

        mid = len(arr) // 2  # 배열을 반으로 나누기 위한 중간 인덱스 계산
        L = arr[:mid]  # 왼쪽 절반
        R = arr[mid:]  # 오른쪽 절반

        # 재귀 호출 (자기 자신을 다시 호출)
        merge_sort(L)  # 왼쪽 계속 쪼개며 정렬
        merge_sort(R)  # 오른쪽 계속 쪼개며 정렬

        i = j = k = 0
        # i : L에서 비교할 위치
        # j : R에서 비교할 위치
        # k : arr에 값을 넣을 위치

        while i < len(L) and j < len(R):  # 둘 다 남아있을 때까지 반복
            if L[i] < R[j]:  # L이 더 작으면
                arr[k] = L[i]  # 작은 값을 arr에 넣기
                i += 1  # L 다음으로 이동
            else:
                arr[k] = R[j]  # R 값이 더 작으면 arr에 넣기
                j += 1  # R 다음으로 이동
            k += 1  # arr 다음 위치로 이동
        # L에 남은 값이 있다면
        while i < len(L):
            arr[k] = L[i]  # 남은값 복사
            i += 1  # L 다음위치
            k += 1  # arr다음위치

        # R에 남은 값이 있다면
        while j < len(R):
            arr[k] = R[j]  # 남은 값 복사
            j += 1  # R 다음 위치
            k += 1  # arr 다음위치

    return arr  # 정렬된 arr 를 반환


# 예시 데이터를 사용한 정렬
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)

# [3, 9, 10, 27, 38, 43, 82]
