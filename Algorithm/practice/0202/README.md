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

처음에는 개념이 추상적으로 느껴졌지만, 직접 구현하고 문제를 풀어보니  이해가 됐습니다. 
스택과 큐가 실제 문제 해결에 어떻게 쓰이는지 체감할 수 있었습니다.

---

