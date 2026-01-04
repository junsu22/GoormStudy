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










