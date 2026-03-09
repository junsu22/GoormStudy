# Comprehension 문법
# 파이썬 고유의 아름다운 문법..?
# 반복문 (for~ in)과 조건문 그리고 변수에 대한 연산까지 
# 모두 갖춘 편리한 문법.

# comprehension 의 종류로는 list, set, dict 등이 존재


# 이라는 list를 만들어 주고 이 중 짝수만 출력 / 기존 방식
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in mylist:
    # 짝수 출력을 위한 조건문 생성
    if i % 2 == 0:
        print(i)


# mylist 이라는 list 에서 짝수만 따로 list로 만들어 주고 싶을 때는 ?
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 짝수를 만들기 위한 빈 리스트 생성
even = []

for i in mylist:
    if i % 2 == 0:
        # even 리스트에 값 추가
        even.append(i)
print(even)


# List Comprehension 방식으로 짝수 리스트 만들기
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = [i for i in mylist if i % 2 == 0]
even


# List Comprehension 기본 형태
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 반복문을 돌면서 i 값이 return 된다고 생각하고 그 변수를 list 에 다시 넣는 원리
even = [i for i in mylist]
even

# 조건 필터 추가

[i for i in mylist if i % 2 == 0]
# mylist 요소 중 짝수만 출력하여 list 로 만들어주는 리스트 컴프리핸션


even = [i for i in mylist if i % 2 == 0]
even

# 모든 값의 제곱  (i 변수에 제곱 연산을 추가 )
even = [i**2 for i in mylist if i % 2 == 0]
even 

# Set Comprehension
# 문법을 세트로 생성
# 괄호를 {} 로 생성하면 set comprehension 이 완성

set_even = {i**2 for i in mylist if i % 2 == 0}
set_even

# dict comprehension 은 comprehension 문법을 황용하여 딕셔너리 생성
# 괄호는 {}로 생성하고, key:value 형식을 반드시 지정합니다.
dict_even =  {i:i**2 for i in mylist if i % 2 == 0}
dict_even


