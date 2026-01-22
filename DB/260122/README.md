



---

## ✅ 오늘의 목표
- Python으로 MapReduce 구현해보기 (예시 데이터: python-mapreduce-examples)
- 고급정규화(BCNF / 4NF / 5NF) 조사
- 1·2·3차 정규화 개념 이해 및 작성
- 도서관리 시스템 ERD 작성 (또는 자유주제)
- ERD를 위한 개념적/논리적/물리적 모델링 정리


---

# 1) MapReduce 실습 — Word Count

## 1-1. 예제 레포 찾기 & 들어가기
수업에서 안내된 예제 레포를 확인했다.

- 예제 레포: `python-mapreduce-examples` (GitHub)
- 확인한 내용: **"This repository was archived by the owner on Sep 22, 2025. It is now read-only."**
  - archived라서 읽기 전용이지만, **clone해서 로컬에서 실습하는 건 문제 없음**

레포 안에서 오늘 진행한 폴더는:
- `word_frequencies/` (Word Count 예제)
- 참고로 같은 레포에 `count_and_sum/`, `max_value_by_store/` 같은 예제 폴더도 존재했다.

---

## 1-2. 폴더 진입 / 경로 확인 
처음에는 `cd word_frequencies`가 안 돼서 헷갈렸다.
그래서 **내가 지금 어디에 있는지**, **클론한 파일이 내 로컬에 어디 저장되는지**를 다시 확인했다.

실제로 Git Bash에서 보인 경로:
- `~/python-mapreduce-examples/word_frequencies`  

파일 목록 확인도 했다:
- `ls -a` 결과에 `README.md`, `data/`, `mapper.py`, `reducer.py`가 보였고,
- “아, 지금 여기 진짜 로컬 폴더에서 실행하고 있구나”가 확정됐다.

![](https://velog.velcdn.com/images/junsu22/post/7a82e93f-b94f-451e-b3c3-3cf40fe1d0b6/image.png)

![](https://velog.velcdn.com/images/junsu22/post/f78f7368-3d93-4edb-b8d4-03031498c538/image.png)


---

## 1-3. MapReduce 파이프라인 실행
README에 나온 명령어 그대로 실행했다.

```bash
cat data/text_a.txt | python mapper.py | sort | python reducer.py
```

### 이해한 흐름 
- **Mapper**: 데이터를 잘게 쪼개서 `(key, value)` 형태로 내보냄  
- **Sort**: 같은 key끼리 모아줌 (중간 과정, 우리가 안 짬)  
- **Reducer**: 모인 값들을 계산해서 최종 결과 만듦  

---

# 2) 트러블슈팅 

## 2-1. Python 버전 확인
```bash
python --version
```
출력:
- `Python 3.13.9`

즉, 예제 코드가 Python2 기준이면 깨질 가능성이 매우 높다.

---

## 2-2. 첫 실행 에러 — print 문법 (Python2 → Python3)
처음 실행했을 때 바로 나온 에러:

```text
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
```
- `mapper.py`의 `print "{0}\t1".format(word)`
- `reducer.py`의 `print old_word, "\t", count`

✅ 해결
- Python3 방식으로 `print(...)` 형태로 수정



---

## 2-3. 두 번째 에러 — string.maketrans (Python2 전용)
print를 고치고 다시 실행했더니 다음 에러가 발생:

```text
AttributeError: module 'string' has no attribute 'maketrans'
```
원인:
- `mapper.py`에서 `string.maketrans` 사용 (Python3에서 없음)

✅ 해결
- `string.maketrans` → `str.maketrans`로 변경

수정 포인트(핵심 한 줄):
```python
return s.translate(str.maketrans("", "", string.punctuation))
```





---

# 3) ✅ 최종 성공 로그 

드디어 성공:

```bash
cat data/text_a.txt | python mapper.py | sort | python reducer.py
```

출력:
![](https://velog.velcdn.com/images/junsu22/post/73ce1490-263e-4b69-b7c4-3597ce4923cf/image.png)


📌 이 출력 화면이 보여주는 것
- Map(단어를 쪼개서 1씩 내보냄) → Sort(같은 단어끼리 모아줌) → Reduce(합산) 흐름이 **정상 동작**
- 로컬에서 MapReduce 파이프라인을 직접 실행해 **Word Count 결과를 검증**


---

# 4) ERD — 도서관리 시스템 (설계 & 구현)

## 4-1. 내가 처음 잡은 핵심
“도서관 관리 데이터에서 관리해야 하는 것”을 먼저 정리했다.

- 관리 대상(엔티티): **회원 / 도서 / 대출**
- 속성(예시):
  - 회원: 회원번호, 이름, 전화번호
  - 도서: 도서번호, 제목, ISBN
  - 대출: 대출번호, 대출일, 반납일

엔티티별로 분리해서 속성 으로 정리하는 흐름으로 넘어갔다.

![](https://velog.velcdn.com/images/junsu22/post/a55fe81c-b7d6-4018-9c22-9d913857c1a8/image.jpg)

- 손그림으로 엔티티/속성/PK/FK 적어가며 이해

---

## 4-2. PK / FK 이해 포인트 (내가 적어둔 메모)
- PK = 고유값(번호)
- FK = “빌려온 것”(다른 테이블의 PK를 참조)
- FK가 없으면 “이 대출이 누구의 대출인지 / 어떤 책인지” 연결이 안 된다


내가 적었던 결론:
- `대출.member_id`
- `대출.book_id`

---

## 4-3. dbdiagram.io로 ERD 구현
손그림 기반으로 dbdiagram.io에서 ERD를 실제로 만들었다.

구성(최종):
- **Member**
  - member_id (PK)
  - name
  - phone
- **Book**
  - book_id (PK)
  - title
  - isbn
- **Loan**
  - loan_id (PK)
  - loan_date
  - return_date
  - member_id (FK → Member.member_id)
  - book_id (FK → Book.book_id)

의미:
- Member(1) : Loan(N)
- Book(1) : Loan(N)
- Member ↔ Book의 M:N 관계를 **Loan(대출)**로 풀어낸 구조

![](https://velog.velcdn.com/images/junsu22/post/55ecf2ce-63c0-43b9-93b3-95094c719a1d/image.png)



---

# 5) 정규화 정리 (기본 + 고급)

## 5-1. 1NF / 2NF / 3NF (기본 단계)
- **1NF**: 컬럼은 원자값만 가진다.
(ex.한 컬럼에 책 제목을 여러 개 적는 건 안 된다.)

- **2NF**: 컬럼은 테이블의 주 키 전체에 의존해야 한다.
(ex. 대출 테이블에서 회원 이름이 회원 ID 일부에만 의존한다면,
회원 정보는 별도의 테이블로 분리해야 한다.)

- **3NF**: 이행 함수 종속 제거 (키 → A → B 형태 종속 제거)
컬럼이 다른 컬럼에 의존하지 않도록 한다.
(ex. 회원 ID → 학과 ID → 학과 이름처럼
키를 거쳐 다른 정보를 설명하는 구조는 분리한다.)

---

## 5-2. BCNF / 4NF / 5NF (고급 정규화)
 “BCNF / 4NF / 5NF” 적어두고, 정리했다.

- **BCNF**
  - 3NF로도 중복이 남는 특수한 경우를 보강하기 위한 규칙
  - Boyce–Codd의 사람 이름에서 따온 정규형이라
1NF, 2NF처럼 숫자가 붙지 않는다
- **4NF**
 - 서로 관련 없는 여러 값이 한 테이블에 섞여 있지 않도록 한다.
(ex. 한 테이블에 ‘회원–취미’와 ‘회원–자격증’이 함께 있으면
불필요한 조합이 계속 늘어날 수 있어 분리한다.)

- **5NF**
  - 테이블을 나눴다가 다시 합칠 때
잘못된 조합이 생기지 않도록 한다.
(ex. 분해 후 조인했을 때 원래 없던 데이터 조합이 생기면 문제가 된다.)
사용되는 겅우가 드물다. 

- 헷갈렸던 용어 :
		다치 종속 (Multi-valued Dependency)
		문서를 읽다가 다치 종속이라는 용어를 발견했다.
		개념이 궁금해 검색해보았지만, 수학적 기호와 형식적인 정의가 함께 등장하면서
		“지금 너무 깊게 파고 있는 건 아닐까?”라는 생각이 들었다. 현재 학습 목표는 정규화의 수학적 증명이 아니라
	왜 이런 개념이 등장했고, 어떤 문제를 해결하려는지 이해하는 것이었기 때문에
	정규화의 필요한 개념만 간단히 정리하는 방향으로 더 알아보지 않기로 했다.

---

# 6) 모델링 3단계 (개념/논리/물리)

- **개념적 모델링**
  - “무엇을 관리할 것인가?”를 정의
  - 회원 / 도서 / 대출

- **논리적 모델링**
  - 엔티티의 속성 정의
  - PK/FK 및 관계(카디널리티) 결정
  - Member-Book 관계를 Loan으로 풀어냄

- **물리적 모델링**
  - 실제 DB 테이블로 구현 가능한 형태로 타입/제약조건 구체화
  - dbdiagram.io에서 스키마 형태로 구현

---
# ✍️ 마무리
막히는 지점에서 왜 안 되는지를 하나씩 확인하며 넘어가는 과정이 더 많이 남은 하루였다.

MapReduce 실습에서는
Python2 기준 예제 코드를 Python3 환경에서 실행하면서
문법 차이로 인한 오류를 직접 겪었고,
에러 메시지를 하나씩 확인하며 수정해 나가는 경험을 했다.

출력 결과를 통해 Map → Sort → Reduce 흐름이 실제로 동작하는 것을 확인하면서
“이론으로만 보던 구조가 이렇게 이어지는구나”라는 감각을 얻을 수 있었다.

ERD와 정규화 파트에서는
정의 자체를 외우기보다는왜 테이블을 나누는지, 왜 이런 개념이 등장했는지에 초점을 맞추려고 했다.
특히 다치 종속처럼 깊게 들어가면 수식과 이론으로 빠질 수 있는 부분에서는
현재 학습 단계에 맞게 개념 이해 수준에서 멈추는 선택을 했다.

완벽함보다는  
지금의 이해 수준을 스스로 확인하는 것을 목표로 삼았다.
