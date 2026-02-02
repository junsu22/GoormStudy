# 스택(Stack)과 큐(Queue) 구현 및 실습

## 📚 개요

오늘은 자료구조의 기본인 **스택(Stack)**과 **큐(Queue)**를 직접 구현하고, 문제를 풀어봤습니다.

- **스택**: 후입선출(LIFO) - 책 쌓기
- **큐**: 선입선출(FIFO) - 파이프

---

## 🔗 링크드 리스트 (Linked List)

스택과 큐를 구현하기 전에, 먼저 링크드 리스트 구조를 이해했습니다.

### 노드 클래스 정의

```python
class Node:
  def __init__(self, data):
    self.data = data  # 데이터 저장
    self.next = None  # 다음 노드 가리키기
```

### 기본 구현

```python
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

# 연결리스트 출력
node = head
while node:
    print(node.data, end=" ")
    node = node.next
# 출력: 1 2 3
```

### 노드 추가하기

```python
# 끝에 노드 추가
node = head
while node.next:
  node = node.next
node.next = Node(4)

# 맨 앞에 노드 추가
node = Node(0)
node.next = head
head = node
# 결과: 0 -> 1 -> 2 -> 3 -> 4
```

**핵심**: head를 잃어버리면 전체 리스트를 잃어버림!

---

## 📚 스택 (Stack) 구현

### 클래스 구현

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        """스택에 데이터 추가"""
        if self.top is None:
            self.top = Node(data)
        else:
            node = Node(data)
            node.next = self.top
            self.top = node

    def pop(self):
        """스택에서 데이터 제거"""
        if self.top is None:
            return None
        node = self.top
        self.top = self.top.next
        return node.data

    def peek(self):
        """스택의 맨 위 데이터 확인"""
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self):
        """스택이 비어있는지 확인"""
        return self.top is None
```

### 테스트 결과

```
Push data = A
Push data = B
Push data = C

Pop data = C
Pop data = B
Pop data = A

Peek data = None
```

---

## 📝 스택 응용 문제

### 1. 문자 거꾸로 출력하기

```python
def reverse_word(word: str) -> str:
  answer: str = ""
  s = Stack()
  for w in word:
    s.push(w)
  while not s.is_empty():
    answer += s.pop()
  return answer

print(reverse_word("aircraft"))
# 출력: tfarcria
```

### 2. 괄호 짝 맞추기 (기본)

```python
def check_bracket(expression: str) -> bool:
    s = Stack()
    
    for exp in expression:
        if exp == "(":
            s.push(exp)
        elif exp == ")":
            if s.is_empty():
                return False
            s.pop()
    
    return s.is_empty()

print(check_bracket("((a * (b + c)) -d) / e"))  # True
print(check_bracket("(((a* (b + c)) -d) / e"))  # False
```

### 트러블 슈팅

처음에 여러 줄 주석을 위해 `'''`를 사용했는데, 이게 실제로는 문자열 객체라서 들여쓰기 에러가 발생했습니다.

**해결**: `#` 주석으로 변경

### 3. 괄호 짝 맞추기 (응용 - 여러 종류)

```python
def check_bracket2(expression: str) -> bool:
    brackets: dict[str, str] = {")": "(", "}": "{", "]": "["}
    s = Stack()
    
    for exp in expression:
        if exp in brackets.values():  # 여는 괄호
            s.push(exp)
        elif exp in brackets:  # 닫는 괄호
            if s.is_empty():  # 안전성 체크
                return False
            pop_bracket = s.pop()
            if pop_bracket != brackets[exp]:
                return False
    
    return s.is_empty()

print(check_bracket2("[{a * (b + c)} - d ]/ e"))  # True
print(check_bracket2("[{a * (b + c)] - d ] / e"))  # False
```

**개선 포인트**: pop 전에 `is_empty()` 확인으로 안전성 향상

---

## 📦 큐 (Queue) 구현

### 클래스 구현

```python
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Queue:
  def __init__(self):
    self.front = None  # 큐의 맨 앞
    self.rear = None   # 큐의 맨 뒤

  def enqueue(self, data):
    """큐에 데이터 추가"""
    if self.front is None:
      self.front = self.rear = Node(data)
    else:
      node = Node(data)
      self.rear.next = node
      self.rear = node

  def dequeue(self):
    """큐에서 데이터 제거"""
    if self.front is None:
      return None
    node = self.front
    if self.front == self.rear:
      self.front = self.rear = None
    else:
      self.front = self.front.next
    return node.data

  def is_empty(self):
    """큐가 비어있는지 확인"""
    return self.front is None
```

### 테스트 결과

```
Enqueue data = A
Enqueue data = B
Enqueue data = C

Dequeue Data = A
Dequeue Data = B
Dequeue Data = C
```

---

## 🔢 큐 응용 문제: 이진수 만들기

### 문제

1부터 n까지의 숫자를 이진수로 변환하여 출력

### 풀이

```python
def generate_binary2(n: int) -> None:
    q = Queue()
    q.enqueue("1")  # 시작값
    
    for _ in range(n):
        i = q.dequeue()  # 큐에서 이진수 꺼내기
        q.enqueue(i + "0")  # 뒤에 "0" 붙여서 추가
        q.enqueue(i + "1")  # 뒤에 "1" 붙여서 추가
        print(i)

generate_binary2(10)
```

### 실행 결과

```
1
10
11
100
101
110
111
1000
1001
1010
```

### 원리

1. "1"부터 시작
2. 큐에서 하나 꺼내서 출력
3. 뒤에 "0"과 "1"을 붙여서 다시 큐에 추가
4. 반복

---

## 💡 핵심 개념 정리

### K-NN (K-Nearest Neighbors)

- **개념**: 주변 K개 이웃을 보고 분류
- **비유**: 친구 레벨 보고 판단 ("유유상종")
- **거리 측정**: 유클리드, 맨해튼, 마할라노비스

### 결정트리 (Decision Tree)

- **개념**: 스무고개 방식으로 분류
- **종류**: CART, ID3, C4.5
- **장점**: 해석이 쉬움
- **단점**: 과적합 가능 (가지치기로 해결)

---

## 🎯 학습 정리

### 배운 것

1. **링크드 리스트**: 노드 추가/삭제, head 관리의 중요성
2. **스택**: 후입선출 구조, 괄호 검사 활용
3. **큐**: 선입선출 구조, 이진수 생성 활용

### 트러블 슈팅

- `'''` 주석 문제 → `#` 주석으로 해결
- `is_empty()` 체크로 안전성 향상

### 느낀 점

처음에는 개념이 추상적으로 느껴졌지만, 직접 구현하고 문제를 풀어보니 이해가 됐습니다. 
특히 스택과 큐가 실제 문제 해결에 어떻게 쓰이는지 체감할 수 있었습니다.

---

## 🔥 스택 심화 문제

### 4. 후위표기법 (중위 → 후위 변환)

**문제**: 중위 표기식(3+5*2)을 후위 표기식(352*+)으로 변환

```python
def to_postfix(expression: str) -> str:
    op: dict[str, int] = {"+": 1, "-": 1, "*": 2, "/": 2}
    # value가 클수록 우선순위 높음 (2 > 1)
    res: str = ""
    s = Stack()
    
    for exp in expression:
        if exp.isnumeric():  # 숫자면
            res += exp
        elif exp in op:  # 연산자면
            # 스택 top의 우선순위가 같거나 높으면 pop
            if not s.is_empty() and (op[exp] <= op[s.peek()]):
                res += s.pop()
            s.push(exp)
    
    while not s.is_empty():  # 남은 연산자 처리
        res += s.pop()
    
    return res

# 테스트
print(to_postfix("3+5*2"))  # 352*+
print(to_postfix("3*5+2"))  # 35*2+
```

**핵심**: 연산자 우선순위를 value로 판단 (기호 자체와 무관)

### 5. 후위표기법 (괄호 처리)

**문제**: 괄호가 포함된 중위 표기식 변환

```python
def to_postfix2(expression: str) -> str:
    op: dict[str, int] = {"+": 1, "-": 1, "*": 2, "/": 2}
    res: str = ""
    s: list[str] = []  # 파이썬 리스트 사용
    
    for exp in expression:
        if exp.isnumeric():
            res += exp
        elif exp == "(":
            s.append(exp)  # 여는 괄호는 스택에 push
        elif exp == ")":
            while s[-1] != "(":  # "(" 만날 때까지
                res += s.pop()
            s.pop()  # "(" 제거
        elif exp in op:
            # 괄호 안에서는 우선순위 비교 안 함
            if s and s[-1] != "(" and (op[exp] <= op[s[-1]]):
                res += s.pop()
            s.append(exp)
    
    while s:
        res += s.pop()
    
    return res

# 테스트
print(to_postfix2("(3+5)*2"))  # 35+2*
```

**개선 포인트**: `s[-1] != "("` 조건으로 괄호 내부 독립적 처리

### 6. 후위표기법 계산

**문제**: 후위 표기식을 계산해서 결과 반환

```python
def eval_postfix(expression: str) -> int:
    s: list[int] = []
    
    for exp in expression:
        if exp.isnumeric():  # 숫자면
            s.append(int(exp))
        elif exp != " ":  # 연산자면
            n2 = s.pop()  # 두 번째 피연산자
            n1 = s.pop()  # 첫 번째 피연산자
            
            if exp == "+":
                res = n1 + n2
            elif exp == "-":
                res = n1 - n2
            elif exp == "*":
                res = n1 * n2
            else:
                res = n1 / n2
            
            s.append(res)
    
    return s[0]

# 테스트
print(eval_postfix("352*+"))  # 13
```

**주의**: 피연산자 순서 중요! (n1 연산자 n2)

### 7. NGE (Next Greater Element)

**문제**: 각 원소의 오른쪽에서 가장 가까운 큰 값 찾기

**방법 1: 이중 for문 (비효율)**
```python
def find_nge_bruteforce(arr: list[int]) -> None:
    n = len(arr)
    for i in range(n):
        nge = -1
        for j in range(i+1, n):
            if arr[j] > arr[i]:
                nge = arr[j]
                break
        print(f"{arr[i]} --> {nge}")
```
- 시간 복잡도: O(n²)
- 직관적이지만 느림

**방법 2: 스택 (효율적 O(n))**
```python
def find_nge(arr: list[int]) -> None:
    n = len(arr)
    s: list[int] = []  # 오른쪽 큰 값 후보들
    res: list[int] = [-1] * n
    
    for i in range(n-1, -1, -1):  # 오른쪽에서 왼쪽으로
        while s:
            if s[-1] > arr[i]:  # 나보다 큰 값 찾음
                res[i] = s[-1]
                break
            else:
                s.pop()  # 작은 값은 버림
        s.append(arr[i])
    
    for i in range(n):
        print(f"{arr[i]} --> {res[i]}")

# 테스트
find_nge([4, 5, 2, 25])
# 4 --> 5
# 5 --> 25
# 2 --> 25
# 25 --> -1
```

**핵심**: 오른쪽에서 왼쪽으로 가면서 스택에 "나보다 큰 후보들" 저장

---

## 🔥 큐 심화 문제

### 2. 요세푸스 순열

**문제**: N명이 원형으로 앉아 K번째마다 제거. 제거 순서는?

**방법 1: 리스트 (직관적)**
```python
def josephus(n: int, k: int) -> list[int]:
    res: list[int] = []
    line: list[int] = [1 for _ in range(n)]  # 1=제거대상
    i: int = -1
    
    for _ in range(n-1):
        count = 0
        while count < k:
            i = (i + 1) % n  # 순환
            if line[i]:
                count += 1
        line[i] = 0
        res.append(i+1)
    
    res.append(line.index(1)+1)
    return res

print(josephus(7, 3))  # [3, 6, 2, 7, 5, 1, 4]
```

**방법 2: 큐 (원형 표현)**
```python
def josephus_q(n: int, k: int) -> list[int]:
    res: list[int] = []
    q = Queue()
    
    for i in range(n):
        q.enqueue(i + 1)
    
    while q.front.next:  # 끝에서 두 번째까지
        for _ in range(k - 1):  # k-1번 회전
            q.enqueue(q.dequeue())  # 맨 앞을 맨 뒤로
        res.append(q.dequeue())
    
    res.append(q.dequeue())  # 마지막 원소
    return res

print(josephus_q(10, 7))
```

**비교**: 
- 리스트: 직관적, 인덱스 계속 순회
- 큐: 원형 큐 자연스럽게 표현

### 3. 큐 뒤집기

**방법 1: 스택 사용**
```python
def reverse_queue(q: Queue) -> None:
    s = []
    while not q.is_empty():
        s.append(q.dequeue())  # 큐 → 스택
    while s:
        q.enqueue(s.pop())  # 스택 → 큐 (역순)

# 큐 출력 함수
def display(q: Queue) -> None:
    node = q.front
    while node:
        print(node.data, end=" ")
        node = node.next
    print()

# 테스트
q = Queue()
for i in range(5):
    q.enqueue(i)
display(q)  # 0 1 2 3 4

reverse_queue(q)
display(q)  # 4 3 2 1 0
```

**방법 2: 재귀 사용**
```python
def reverse_queue_recursive(q: Queue) -> None:
    if not q.is_empty():
        data = q.dequeue()  # 하나 꺼내고
        reverse_queue_recursive(q)  # 나머지 뒤집기
        q.enqueue(data)  # 맨 뒤에 추가

# 테스트
q = Queue()
for i in range(5):
    q.enqueue(i)
display(q)  # 0 1 2 3 4

reverse_queue_recursive(q)
display(q)  # 4 3 2 1 0
```

**동작 과정**:
1. 큐에서 모든 데이터를 재귀로 꺼냄
2. 재귀에서 돌아오면서 역순으로 다시 넣음

---

## 📊 최종 학습 성과

### 스택 문제 (8개)
1. ✅ 스택 구현
2. ✅ 문자 뒤집기
3. ✅ 괄호 검사 (기본)
4. ✅ 괄호 검사 (응용)
5. ✅ 후위표기법 (변환)
6. ✅ 후위표기법 (괄호)
7. ✅ 후위표기법 (계산)
8. ✅ NGE

### 큐 문제 (6개)
1. ✅ 큐 구현
2. ✅ 이진수 만들기
3. ✅ 요세푸스 (리스트)
4. ✅ 요세푸스 (큐)
5. ✅ 큐 뒤집기 (스택)
6. ✅ 큐 뒤집기 (재귀)

---
👉 **[실습코드](https://github.com/junsu22/GoormStudy/tree/main/Algorithm/practice/0202)**

