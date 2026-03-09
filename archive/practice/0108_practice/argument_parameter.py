#  인수 argument : 값, 변수 , 참조 등을 전달 하는 값,
# 매개변수 parameter : 함수 등에서 사용되는 전달된 값을 받는 변수


# 10, 20 > 인수
# a, b 는 매개변수

def some_function(a, b):
    result = a + b
    return result

some_function(10, 20)



# 위치 인수
# 가장 보편적인 인수
# 변수명을 인수로 지정
# 위차가 중요하다
# a,b,c를 위치인수로 지정한 경우
def add_function(a, b, c ):
    result = a + b + c 
    print(f'a:{a}, b: {b}, c: {c}')
    print(f'sum: {result}')
    return result

add_function(1, 3, 5)

# add function(1, 3) #  a, b , c 개수 맞춰서 넣어야 함.부족하거나 너 많이 넣으면 오류. 



# 키워드 인수 
# 위치 인수의 위치를 정확하게 기억하지 못하고 혼란을 야기할 수 있기 때문에 인수명에 값을 직접 지정
def add_function(a, b, c):
    result = a + b + c
    print(f'sum: {result}')
    return result


# 기본 매개변수
# 매개변수에 기본 값을 지정할 수 있다.
# 기본 값을 지정시 인수에 값을 생략 가능
# 단 기본 값이 지정된 인수는 위치 인수보다 다음에 위치해야한다.

def add_function(a, b, c):
    result = a + b + c
    print(f'a : {a}, b : {b}, c : {c}')
    print(f'sum: {result}')
    return result


add_function(1, 3, 5)
# a = 1, b = 3, c =5
# sum : 9

# 기본 매개변수가 위치 인수보다 앞쪽에 위치한 경우 error


# tuple 인수
# 여러개의 인수를 전달 받을 수 있음
# 여러개으이 인수를 전달 받은 *args 에는 튜플 형식으로 데이터가 저장됨
# args 로 받은 인수는 반복문으로 처리하는게 일반적
# 대체적으로 *args 변수가 많이 사용 됨

def add_function(*args):
    result = 0 
    print(f' args 의 타입 : {type(args)}')
    for arg in args:
        print(arg)
        result += arg
    print('==='* 5)
    print(f'sun : {result}')

#아무런 값을 전달하지 않은 경우 생략가능 
add_function()
# 1개의 값을 전달 한 경우
add_function(1)
# 복수의 값을 전달 한 경우
add_function(1, 2, 3, 4, 5)



# 위치 매개변수와 tuple 매개변수의 혼용
# *tuple 매개변수는 위치 매개변수의 뒤에 위치해야 한다.
def add_function(a, args):
    print(f'a : {a}')
    print('===' * 5)
    result = 0
    for arg in args:
        print(arg)
        result += arg
    print('===',* 5)
    print(f'sum : {result}')

# 아무런 값을 지정하지 않은경우 위치 매개변수 미지정으로 인한 에러 발생
# add_function()

# 단일값 지정
# add_function(1)

#복수의 값을 지정한 경우
# add_function(1, 2, 3, 4, 5)



# dict 인수 
# 여러개의 인수를 전달 받을 수 있다.
# 여러개의 인수를 전달 받은 **kwargs에는 dict 형식으로 데이터 저장
# **kwargs 로 받은 인수 역시 반복문으로 처리하는 것이 일반적
# 대체적으로 **kwargs 변수 많이 사용

def add_function(**kwargs):
    total_age = 0
    for name, age in kwargs.items():
        print(f' 이름 : {name}, 나이 : {age}')
        total_age +=age
    print('==='*5)
    print(f'전체 나이의 합계 : {total_age}')

