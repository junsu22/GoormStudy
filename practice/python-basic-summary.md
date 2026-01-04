# Python 기초 학습 총정리

## 1. 변수와 자료형
변수는 값을 담는 이름이다.  
파이썬은 자료형을 자동으로 판단한다.

```python
x = 10
name = "준수"

```
## 2. 리스트 (List)

리스트는 여러 값을 순서대로 저장하며, 값을 수정할 수 있다.
```python
numbers = [1, 2, 3, 4, 5]
numbers[0] = 10
```

## 3. 튜플 (Tuple)

튜플은 여러 값을 묶지만 수정할 수 없다.
변하면 안 되는 데이터를 저장할 때 사용한다.

```python
nums = (1, 2, 3)
```

## 4. 딕셔너리 (Dictionary)

딕셔너리는 key와 value 형태로 데이터를 저장한다.

```python
config = {
    "host": "localhost",
    "port": 8080,
    "debug": True
}

print(config["port"])
```

## 5. 조건문 (if / elif / else)

```python
x = 10

if x > 10:
    print("큼")
elif x == 10:
    print("같음")
else:
    print("작음")

```
## 6. 반복문
``` python
numbers = [1, 2, 3]

for number in numbers:
    print(number)

```
## 7. range()

```python
for i in range(5):
    print(i)

for i in range(1, 10, 2):
    print(i)

```

    print(i)

## 8. 누적 합과 개수 세기
합계 구하기
```python
numbers = [3, 7, 2, 9, 1, 10, 4]

total = 0
for number in numbers:
    total += number

print(total)
```
조건에 맞는 개수 세기

```python

count = 0
for number in numbers:
    if number > 5:
        count += 1

print(count)

```
## 9. 함수 (Function)
```python
def add(a, b):
    return a + b

result = add(3, 7)
print(result)

```
##10. 함수 + 반복문 활용
```python

numbers = [3, 7, 2, 9, 1, 10, 4]

def count_above(numbers, threshold):
    count = 0
    for number in numbers:
        if number > threshold:
            count += 1
    return count

result = count_above(numbers, 5)
print(result)

```


## 11. 클래스와 객체
클래스는 변수와 함수를 묶어 놓은 설계도이다.
객체는 클래스로 만든 실제 사용 대상이다.

## 12. 클래스 기본 예제
```python
class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("안녕하세요,", self.name)
```

## 13. 객체 생성과 사용
```python
p1 = Person("준수")
p2 = Person("민수")

p1.say_hi()
p2.say_hi()
```
## 14. 객체지향 프로그래밍 (OOP)
객체지향 프로그래밍은 데이터와 기능을 객체 단위로 묶어 관리하는 방식이다.
코드 재사용성과 유지보수성이 좋아진다.

클래스는 설계도이고, 객체는 그 설계도로 만든 실제 대상이다.






