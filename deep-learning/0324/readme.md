# 🧠 LangChain 기본 구조 정리

## 📌 개요
LangChain은 여러 단계를 연결하여  
LLM 기반의 처리 흐름을 구성하는 프레임워크입니다.

---

## 🔗 1. 체인 구조 (Chain)

기본 흐름:

Prompt → LLM → Output

LangChain에서는 이를 다음과 같이 표현합니다:

Prompt | LLM

- `|` (파이프)는 단계 연결 연산자입니다.
- 앞 단계의 출력이 다음 단계의 입력으로 전달됩니다.

---

## 🔄 2. Runnable Sequence (러너블 시퀀스)

여러 단계를 연결한 실행 흐름입니다.

예시:

Prompt | LLM | OutputParser

- 각 단계가 순차적으로 실행됩니다.
- 이전 결과가 다음 단계로 자동 전달됩니다.

---

## 🔗 3. 체인 연결 구조

여러 체인을 이어서 사용할 수 있습니다.

예시 흐름:

질문 생성 → 답변 생성 → 결과 정리

구조:

Chain1 → Chain2 → Chain3

- 이전 체인의 결과가 다음 체인의 입력으로 전달됩니다.

---

## 🧪 4. Callback Handler

체인 실행 중 내부 과정을 확인할 수 있습니다.

확인 가능한 내용:
- LLM 호출 과정
- 실행 흐름
- 토큰 사용량

디버깅 및 추적에 활용됩니다.

---

## 📦 전체 흐름 요약

Prompt  
↓  
LLM  
↓  
Output  

확장 구조:

Prompt  
↓  
LLM  
↓  
OutputParser  
↓  
Next Chain  

---

## 💡 핵심 정리

LangChain은  
"단계를 연결하여 하나의 실행 흐름을 만드는 프레임워크"입니다.
