# 내장함수 
# 파이썬에는 이미 만들어진 내장함수가 존내 
# 이미 사용하고 있는 print(), type()이 파이썬의 대표적인 내장함수 


# 문법 : map(function, iterable)
# map 은 함수 (f)와 순회 가능한 (iterable) 자료형으로 입력 받음
# map 은 입력받은 자료형의 각 요소를 함수(function)가 수행한 결과를 묶어서 돌려줍니다.

sample_data = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10]


# map 만 실행시 요소의 내용이 바로 출력되지 않는다 . 
map(str, sample_data)


# list()로 변환하여 요소를 출력 
list(map(str,sample_data))

# map 에 lambda 적용


result = map(lambda x: x*2, sample_data)
list(result)

# map에 다중인수를 지정
sample_data = [1 ,2 ,3, 4, 5, 6, 7, 8, 9, 10]
sample_data2 = [1 ,2 ,3,5, 8, 13, 21, 34, 55]
list(map(lambda x, y: x+y, sample_data, sample_data2))


# ====================================

# fulter(function, iterable)
# filter 내장함수는 값을 filter 할 때 사용합니다.
# True인 값을 가지는 요소만 filter 

sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# lambda 함수를 지정한 경우
result = filter(lambda x : True if (x % 2 == 1 ) else False.sample_data)
list

# 함수로 선언하여 함수명으로 지정한 경우

def three_multiple(x):
    if x % 3 == 0:
        return True
    else:
        return False
    
# zip 
    # 문법 : zip (*iterable)
    # 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 한다.

    sample_data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sample_data2 = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    sample_data3 = [5, 6, 7]

# sample_data1, sample_data2 을 zip 으로 묶어준 경우
result = zip(sample_data1, sample_data2)
list(result)

list(zip(sample_data1, sample_data2, sample_data3))

# zip 의 활용
number - [1, 2, 3, 4]
name = ['홍길동', '김철수', 'John','Paul']

number_name = list(zip(number,name))
number_name


eunmerate(iterable, start = 0)
# 순서가 있는 자료형을 입력 받아 index를 포함하는 객체로 return 합니다. 

# 일반 range()

for value in range(1, 10, 2):
    print(value)


# enumerate()함수를 사용하여 index를 return 받은 경우
for idx, value in enumerate(range(1, 10, 2), start=100):
    print(f'index : {idx}, value: {value}')





