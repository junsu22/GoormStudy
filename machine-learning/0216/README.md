# LLM 선행학습 Day 1: GPT-2 찍먹 🤖

## 📅 날짜
2026.02.16 (월)

## 🎯 목표
- GPT-2로 LLM API 구조 이해하기
- 모델의 한계 체감하기

## 🛠 환경 설정
```bash
pip install transformers torch
```

## 💻 실습 코드
```python
from transformers import pipeline

# GPT-2 모델 로딩
generator = pipeline("text-generation", model="gpt2")

# 테스트: 영어 질문
prompt = "Python is a programming language that"
result = generator(prompt, max_length=50)
print(result[0]['generated_text'])
```

## 📊 테스트 결과

### [테스트 1] 영어 질문
**질문:** Python is a programming language that

**답변:** Python is a programming language that allows you to work with data from your code, without needing to write any code.

**평가:**
- 시작은 그럴듯하지만 중간부터 이상한 답변
- 의미 없는 문장 생성

### [테스트 2] 코딩 질문
**질문:** To sort a list in Python, you can

**답변:** To sort a list in Python, you can use the SortBy keyword to sort a list.

**평가:**
- ❌ Python에 `SortBy` 라는 키워드 없음
- ❌ 틀린 정보를 자신 있게 말함
- ✅ 정답: `sorted()` 함수 또는 `.sort()` 메서드

### [테스트 3] 한국어 질문
**질문:** 파이썬은

**답변:** 파이썬은 나를에서 븄로 쟠구정페의 장고우이 저에광이했다.

**평가:**
- 알 수 없는 말.. 
- GPT-2는 한국어 학습이 거의 안 됨

## 느낀 점

**API 구조 이해**
- `pipeline`으로 모델 로드 → 프롬프트 입력 → 결과 생성
- 기본 패턴 이해 완료 ✅

**GPT-2의 한계**
- 기술의 명확한 한계
- 영어도 횡설수설, 잘못된 정보, 한국어는 사용 불가능
- 문장 완성은 가능하지만 의미 있는 답변은 불가능

**기술 발전에 대한 생각**
GPT-2를 직접 돌려보니, 
현재 우리가 편하게 사용하는 ChatGPT나 Claude 같은 모델들이 
나오기까지 얼마나 많은 기술 발전이 있었을지 실감했다. 

불과 4~5년 만에 이렇게 빠르게 발전했다는 것이 놀라웠고, 
당시엔 상상도 못 했을 기술을 지금 내가 배우고 있다는 게 신기하게 느껴졌다.

## 📝 배운 것

- LLM은 "문장 완성" 방식으로 동작한다
- API 호출 구조: 모델 로드 → 프롬프트 입력 → 결과 받기
- 2019년(GPT-2)과 현재 모델의 성능 차이가 엄청날 것 같다


---

