# 📌 LangChain Prompt & Streaming Practice

## 🚀 프로젝트 개요

본 실습은 LangChain을 활용하여 LLM 호출, 프롬프트 설계, 체인 구조 구성,<br>
그리고 스트리밍 방식의 응답 처리까지 전체 흐름을 이해하기 위해 진행되었습니다.

단순한 API 호출을 넘어,
**Prompt → Chain → LLM → Streaming Output** 구조를 직접 구현하는 데 초점을 두었습니다.

---

## 🧠 주요 기능

### 1. LLM 기본 호출

* `ChatOpenAI`를 활용한 질의 응답
* `invoke()` 기반 응답 처리

### 2. 스트리밍 출력

* `stream()`을 활용한 토큰 단위 실시간 출력
* 사용자 경험(UX) 개선 가능

### 3. 프롬프트 설계

* `ChatPromptTemplate` 사용
* 변수 기반 템플릿 구성

### 4. 체인 구조 (LCEL)

* `prompt | llm` 형태의 파이프라인 구성
* LangChain의 핵심 구조 이해

### 5. System / User 역할 분리

* system: AI 역할 정의
* user: 사용자 질문
* 역할 기반 프롬프트 설계 적용

### 6. 프롬프트 캐싱 개념 이해

* 반복 프롬프트 최적화 개념 학습
* 토큰 사용량 기반 캐싱 확인

---

## ⚙️ 사용 기술

* Python
* LangChain
* OpenAI API
* Google Colab

---

## 📂 프로젝트 구조

```text
llm/
 └── langchain/
      ├── langchain_prompt_stream_gpt54.ipynb
      ├── langchain_prompt_stream_gpt54.py
      └── langchain_basic_prompt_stream.md
```

---

## 💡 핵심 학습 포인트

* LangChain은 단순 호출이 아닌 **구조 기반 설계 도구**이다
* 프롬프트 설계가 결과 품질에 직접적인 영향을 준다
* 스트리밍 출력은 실제 서비스에서 중요한 UX 요소이다
* 체인 구조를 통해 확장 가능한 LLM 파이프라인을 구성할 수 있다

---

## ✨ 느낀 점

LangChain을 활용하면서 단순한 모델 호출이 아닌
프롬프트 설계와 체인 구조의 중요성을 체감할 수 있었다.

특히 스트리밍 방식의 응답 처리는
실제 서비스에서 사용자 경험을 개선하는 핵심 요소라고 느꼈다.

이번 실습을 통해 향후 RAG, 에이전트 구조로 확장할 수 있는
기초를 다질 수 있었다.

---
