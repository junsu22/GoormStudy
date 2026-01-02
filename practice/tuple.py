"""
tuple.py
튜플(Tuple) 기초 실습 파일

- 튜플은 소괄호 () 로 만든다.
- 리스트([])와 비슷하지만, 튜플은 값을 수정할 수 없다(불변, immutable).
- 인덱싱, 슬라이싱, len() 같은 조회는 가능하다.
"""

# 1) 튜플 만들기
fruits = ("사과", "바나나", "오렌지")

# 튜플 길이 구하기
print("len(fruits) =", len(fruits))  # 3

# 2) 인덱싱(indexing): 특정 위치의 값 꺼내기
numbers = (10, 20, 30)
print("numbers[0] =", numbers[0])    # 10
print("numbers[-1] =", numbers[-1])  # 30 (음수 인덱스는 뒤에서부터)

# 3) 슬라이싱(slicing): 범위로 값 꺼내기
nums = (1, 2, 3, 4, 5)
print("nums[1:4] =", nums[1:4])      # (2, 3, 4)
# 슬라이싱 결과도 튜플이다.

# 4) 튜플은 수정이 불가능하다 (이게 핵심 차이)
# 아래 코드는 에러가 난다. (TypeError: 'tuple' object does not support item assignment)
# fruits[0] = "포도"

# 5) 튜플 활용 예시: '변하면 안 되는 값 묶음'에 사용
# 예: (가로, 세로)처럼 한 쌍을 고정으로 다룰 때
resolution = (1920, 1080)
print("resolution =", resolution)

# 6) 튜플 언패킹(unpacking): 여러 값 한 번에 받기
width, height = resolution
print("width =", width)
print("height =", height)

# 7) 튜플 안에 리스트가 들어가면? (주의 포인트)
# 튜플 자체는 바꿀 수 없지만, 안에 들어있는 '리스트'는 바뀔 수 있다.
mix = (1, [2, 3], 4)
mix[1].append(99)
print("mix =", mix)  # (1, [2, 3, 99], 4)
