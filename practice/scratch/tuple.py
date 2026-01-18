
# 예제 혼자 코딩해보면서 이유 설명해보기

# 딕셔너리는 중괄호 {}로 묶는다.
# config는 딕셔너리를 담는 변수다.
# "port"는 key이고, 8080은 value다.

# value는 변경할 수 있고,
# key는 의미를 나타내기 때문에 보통 고정해서 사용한다.

# config["port"]를 통해
# "port" 키에 해당하는 값 8080을 호출한다.


config  = {
    "host" : "localhost",
    "port" : 8080,
    "debug" : True
}

print(config["port"])







# # 예제 1 설명 (길이 구하기)
# fruits = ("사과", "바나나", "오렌지")
# print(len(fruits)) # 길이를 셈 0,1,2 세 개의 데이터로 총 길이는 3

# # 예제2 설명 (인덱싱)
# numbers = (10, 20, 30)
# print(numbers[0]) # 10 0번째 데이터를 출력
# print(numbers[-1]) # 30  음수는 반대로 되돌아간다 . 

# nums = (1, 2, 3, 4, 5)

# print(nums[1:4]) # 2, 3, 4 1번째 데이터 부터 4번째 데이터 전까지 출력. 결과도 튜플임



