# 파이썬 - 문자열 포맷팅
# C언어 스타일의 문자열 포맷팅과 파이썬 스타일의 문자열 포맷팅

name = " minsu"
score = 90
print("%s의 점수는 %d 점 입니다." % (name, score))

 # minsu의 점수는 90 점 입니다.



# 파이썬3 부터 지원하는 문자열 클래스 format 메서드

name = "minsu"
score = 90
print("{}의 점수는 {} 점입니다.".format(name, score))

# minsu의 점수는 90 점입니다.

# 파이썬 3.6부터 지원하는 f-String사용
name = "minsu"
score = 90
print (f"{name}의 점수는 {score}점 입니다.")

# minsu의 점수는 90점 입니다.

# 파이썬 - 특문 출력
# Format 메소드를 활용한 특수문자출력

data = 3
fmt = "{{ {} }}".format(data)
print(fmt)

#f-string에서도 동일하다.
data = 3
fmt = f"{{ {data} }}"
print(fmt)

# { 3 }
# { 3 }

# 파이썬 - 자릿수 채우기
# 계좌번호 채우기, 금융/회계 계열에서 주로 사용

a = 3
mystr = f"{a:02d}"
print(mystr)

symbol = "BTCUSDT"
print(f"{symbol:10}")

# 03
# BTCUSDT   

# 파이썬 - 실수(float)
a = 3.141592
mystr = f"{a: 6.2f}" #mystr = " 3.14"
print(mystr)

# 3.14


# 파이썬 - Immutable 과 Mutable
# 메모리 값이 출력된다.a = "hello"
b = {"hello", "python"}

id(a)
id(b)

# 133775840434816 

# 파이썬 - Immutable 과 Mutable
# 수정가능 / 수정불가능 타입
a = "python2"
id(a)

a = "python3"
id(a)

# 10699680


# 리스트에 대한 수정. a 라는 변수를 리스트 객체에 바인딩.
# 리스트에 값을 추가하더라도 리스트 객체의 시작 주소값은 변하지 않는다.

a = ["python2", "python3"]
id(a)
a.append("python4")
a
# ['python2', 'python3', 'python4']

id(a[0])
# 133775840196224

id(a[1])
# 133775840196224

id(a[2])
# 133775847945056



# 비교연산자

a = 1000
b = 1000
a == b
# True

a is b
# False

id(a), id(b)
# (133775841789584, 133775841796976)


# 더 작은 정수 값을 바인딩.
# ==와 is 연산자 모두 True를 리턴
# a,b 는 동일객체를 바인딩하는것.
# 파이썬은 정수 256 까지에 대해 이미 해당값이 존재한다면, 기존객체를 바인딩.
# 동일 값을 메모리에 여러번 할당함으로써 메모리 낭비를 줄이기 위함이다.

a = 3
b = 3
id(a), id(b)
# (11654440, 11654440)

a == b
# True

a is b
# True


#제곱값

pow2_nums = [i*i for i in range(10)]




# 튜플 패킹
a = 1, 2
b = (1, 2)

print(a, type(a))
print(b, type(b))

# (1, 2) <class 'tuple'>
# (1, 2) <class 'tuple'>


# 튜플 언패킹
# 튜플의 왼쪽에 각 튜플의 원소를 바인딩할 변수를적어주면
# 각 변수가 튜블의 원소를 바인딩 (튜플 언패킹)

data = {1, 2, 3}
n1, n2, n3 =data
print(n1, n2, n3)

# 1 2 3

# n1 =data[0]
# n1 =data[1]
# n1 =data[2]

# 처럼 인덱싱 할 필요가 없어 편리하다.



# 가장 낮은 값과 가장 높은 값은 각각 high, low 로 바인딩하고
# 나머지는 other 로 바인딩
# *을 붙여주면 된다

scores = {1, 2, 3, 4, 5, 6}
low, *others, high = scores
print(others)


# 1 2 3
# [2, 3, 4, 5]



# 튜플심화(함수호출)
# hap 함수에서 리턴 할때 패킹
# 4개의 수를 입력받아 모두 더한 값을 리턴하는 hap 함수가 있다.
# 이 함수를 사용하면 4개의 데이터를 다음과 같이 전달해야한다.

# def hap (num1, num2, num3, num4):
#   return num1+num2+num3+num4

#  scores = {1, 2 ,3 ,4}
#  result = hap(scores[0], scores[1],scores[2],scores[3])
#  print(result)

# 간소화

def hap(num1, num2, num3, num4):
  return num1+num2+num3+num4
  scores = {1,2,3,4}
  result = hap(*scores) #함수 호출시 튜플 언패킹
  print(result)


# zip 두개의 리스트를 서로 묶어줄때 사용
name = ['merona','gugucon']
price =  [500,1000]

z = zip(name, price)
print(list(z))

# [('merona', 500), ('gugucon', 1000)]




# zip 을 이용해 하나의 for문 사용

name = ['merona','gugucon']
price =  [500,1000]

for n, p in zip(name, price):
  print(n, p)

# merona 500
# gugucon 1000


# 파이썬 -ZIp 과 dictonary
# 딕셔너리 생성했었을때
# 아이스크림1 = {"메로나": 500. "구구콘":1000}

# 키가 문자열인 경우 딕셔너리 생성
아이스크림2 = dict(메로나 = 500, 구구콘 = 1000)

# 키와 값을 하나의 튜플로 지정
아이스크림3 = dict([("메로나, 500"), ("구구콘", 1000)])



# 딕셔너리에서의 zip 활용
# 아이스크림이름이 key, 가격을 value

name = ['merona', 'gugucon']
price = [500, 1000]

icecream = dict(zip(name, price))
print(icecream)

# {'merona': 500, 'gugucon': 1000}


# setdefault 메소드
# 딕셔너리에 key 를 추가하면서 초깃값을 설정할때, setdefault 메소드를 사용할 수 있다.

data = {}

ret = data.setdefault('a', 0) # key로 'a'를 추가할 value 0을 설정함, setdefault는 현재 value값을 리턴
print(ret, data)

ret = data.setdefault('0', 1) # 이미 key가 있는 경우 setdefault 현재 value 값을 리턴
print(ret, data)

# 0 {'a': 0}
# 1 {'a': 0, '0': 1}


# 딕셔너리 원소개수 
# 리스트에 데이터가 있을 때 각 데이터가 몇 번씩 있는지?

data = ["BTC", "BTC", "XRP", "ETH", "ETH"]

for k in set (data):
             count = data.count(k)
             print(k, count)

# XRP 1
# BTC 2
# ETH 2


# 파이썬- 딕셔너리 컴프리헨션
name = ['merona', 'gugucon']
price = [500,1000]
    
icecream = {k:v for k, v in zip(name, price)}
print(icecream)

# {'merona': 500, 'gugucon': 1000}


name = {'merona', 'gugucon', 'bibibig'}
price = [500, 1000, 600]
     
icecream = {k:v for k, v in zip(name, price) if v < 1000}
print(icecream)
# {'gugucon': 500, 'bibibig': 600}


# 파이썬- 네임드튜플
# 책의 제목과 가격을 저장하는 BOOK 클래스를 만듥 Book 클래스로부터 객체를 생성
class Book:
  def __init__(self, title, price):
    self.title = title
    self.price = price
mybook = Book("파이썬을 이용한 비트코인 자동매매", 27000)
print(mybook.title, mybook.price)
# 파이썬을 이용한 비트코인 자동매매 27000


from collections import namedtuple

Book = namedtuple('Book', ['title', 'price'])
mybook3 = Book("파이썬을 이용한 비트코인 자동매매", 27000)
print(mybook3.title, mybook3.price)
# 파이썬을 이용한 비트코인 자동매매 27000

def print_book(title, price):
  print(title, price)

print_book(*mybook3)
# 파이썬을 이용한 비트코인 자동매매 27000



