# 🐍 파이썬 개인 학습 노트

> 파이썬 기초 문법을 학습하며 정리한 개인 학습 자료

---

## 1. 출력문 (print)
파이썬에서 **화면에 값을 출력**할 때 사용하는 함수

🔹 예제  
<code>print("Hello, Python!")</code>

---

## 2. 변수
값을 저장하기 위한 공간  
파이썬은 **변수 선언 시 자료형을 미리 지정하지 않음**

🔹 예제  
<code>x = 10</code>  
<code>name = "Alice"</code>

---

## 3. 데이터 타입
- <code>int</code> : 정수  
- <code>float</code> : 실수  
- <code>str</code> : 문자열  

🔹 예제  
<code>a = 10</code>  
<code>b = 3.14</code>  
<code>c = "python"</code>

---

## 4. 연산자
- <code>+</code> : 덧셈  
- <code>-</code> : 뺄셈  
- <code>*</code> : 곱셈  
- <code>/</code> : 나눗셈  
- <code>%</code> : 나머지  

🔹 예제  
<code>print(10 + 3)</code>  
<code>print(10 % 3)</code>

---

## 5. 조건문 (if / elif / else)
조건에 따라 **실행되는 코드가 달라짐**

🔹 예제  
<code>score = 85</code>  

<code>if score >= 90:</code>  
<code>&nbsp;&nbsp;&nbsp;&nbsp;print("A")</code>  
<code>elif score >= 80:</code>  
<code>&nbsp;&nbsp;&nbsp;&nbsp;print("B")</code>  
<code>else:</code>  
<code>&nbsp;&nbsp;&nbsp;&nbsp;print("C")</code>

---

## 6. 반복문
같은 작업을 **여러 번 수행**할 때 사용

🔹 for 문  
<code>for i in range(3):</code>  
<code>&nbsp;&nbsp;&nbsp;&nbsp;print(i)</code>

🔹 while 문  
<code>i = 0</code>  
<code>while i &lt; 3:</code>  
<code>&nbsp;&nbsp;&nbsp;&nbsp;print(i)</code>  
<code>&nbsp;&nbsp;&nbsp;&nbsp;i += 1</code>

---

## 7. 리스트 (List)
여러 개의 값을 **순서대로 저장**  
대괄호 <code>[ ]</code> 사용

🔹 예제  
<code>fruits = ["apple", "banana", "orange"]</code>  
<code>print(fruits[2])</code>

🔹 값 추가  
<code>fruits.append("mango")</code>  
<code>print(fruits)</code>

---

## 8. 문자열 다루기
문자열도 **인덱싱 / 슬라이싱 가능**

🔹 예제  
<code>text = "python"</code>  

<code>print(text[0])</code>  
<code>print(text[0:3])</code>  
<code>print(text + " is fun")</code>

---

## 9. 함수 (Function)
코드를 **재사용**하기 위해 사용

🔹 예제  
<code>def add(a, b):</code>  
<code>&nbsp;&nbsp;&nbsp;&nbsp;return a + b</code>  

<code>result = add(3, 5)</code>  
<code>print(result)</code>

---

## 10. 모듈 (Module)
다른 사람이 만든 기능을 **가져와 사용**

🔹 예제  
<code>import math</code>  
<code>print(math.sqrt(16))</code>

---

## 11. AI를 활용한 학습 방법

🔹 예시 프롬프트  
<code>너는 1타 강사야.</code>  
<code>print() 함수에 대해 아주 쉽게 설명해줘.</code>  
<code>예제도 3개 만들어줘.</code>

---

## 12. 튜플 (Tuple)
리스트와 비슷하지만 **수정 불가능**  
소괄호 <code>( )</code> 사용

🔹 예제  
<code>t = (1, 2, 3)</code>  
<code>print(t[0])</code>

---

## 13. 딕셔너리 (Dictionary)
키(key)와 값(value)을 연결하여 저장  
중괄호 <code>{ }</code> 사용

🔹 예제  
<code>student = {</code>  
<code>&nbsp;&nbsp;&nbsp;&nbsp;"name": "Alice",</code>  
<code>&nbsp;&nbsp;&nbsp;&nbsp;"age": 15,</code>  
<code>&nbsp;&nbsp;&nbsp;&nbsp;"grade": "A"</code>  
<code>}</code>

🔹 값 수정  
<code>student["age"] = 16</code>

🔹 키 / 값 출력  
<code>print(student.keys())</code>  
<code>print(student.values())</code>  
<code>print(student)</code>

---

### 📊 학생 점수 관리 예제

<code>student_scores = {</code>  
<code>&nbsp;&nbsp;&nbsp;&nbsp;"Alice": 95,</code>  
<code>&nbsp;&nbsp;&nbsp;&nbsp;"Bob": 87,</code>  
<code>&nbsp;&nbsp;&nbsp;&nbsp;"Charlie": 92</code>  
<code>}</code>

<code>print("Alice의 점수 :", student_scores["Alice"])</code>

---

## 14. 집합 (Set)
중복을 허용하지 않는 자료형

🔹 예제  
<code>numbers = {1, 2, 3, 3}</code>  
<code>print(numbers)</code>

---

## ✅ 정리
> 출력 → 변수 → 자료형 → 조건문 → 반복문 → 자료구조 → 함수 → 모듈  
> 이 순서로 학습하면 파이썬 기초를 안정적으로 익힐 수 있다.
