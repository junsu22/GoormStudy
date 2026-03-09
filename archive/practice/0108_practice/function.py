# 함수 function 
# 자주 사용되는 코드 및 반복되는 코드를 모아 하나의 기능으로 만들고 이름 붙인 것. 
# 함수의 가장 중요한 기능은 코드재사용성

# # 기본구조
# def 키워드로 시작, 함수명을 기입
# ()안에 매개변수를 지정, 생략도 가능
# 끝은 : 로 끝남
# 함수의 범위 안에서는 들여쓰기를 한다. 
# 들여쓰기가 끝난 지점이 함수의 범위가 끝나는 지점


# 입력의 형태
def add_function(a, b):
    result = a + b
    return result

# 입력 매개변수가 없는 형태
def sample_function():
    a = 1 
    b = 2 
    result = a + b 
    return result


# return 이 없는 형태

def sample_function(a, b ):
    result = a + b
    print(f'result : {result}')


# 입력 매개변수, return 이 없는 형태 
def sample_function():
    print('Hello World !')


def sample_function():
    print("함수가 호출 되었습니다.")

# 함수 이름만 호출
sample_function

# 호출 : 이름과 함께 () 실행
sample_function()

# 함수를 변수에 대입 후 변수에 ()를 함께 실행

a = sample_function
a()

# return 이 존재하는 경우
def sample_function():
    print('함수가 호출 되었습니다!')
    return 123
result = sample_function()
print(result) # 123

# return 이 없는 경우
def sample_function():
    print("함수가 호출 되었습니다.! ")
result =sample_function()
print(result) # 아무 결과를 반환하지 않는다면 None


# docsttring 함수에 대한 설명을 기록

def sample_function():
    """
    함수에 대한 설명을 기록.
    sample_function 은 함수를 설명하기 위한 예제 함수.
    (ex. 호출의 예)
    """
print("함수가 호출 되었습니다!!")


sample_function() # 함수명 __.doc__로 docstring 을 출력할 수 있음.

print(sample_function.__doc__) # 사용법
