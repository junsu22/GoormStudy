"""
Date: 2026.02.16
LLM 선행학습 (부제 : GPT-2 찍먹)
=====================================================
GPT2 모델로 테스트 해보기 (2019년 수준이라 성능이 많이 떨어짐. 횡설수설 등)
- 어떻게 동작하는지 실험하기 위해 개발.
=====================================================
"""

from transformers import pipeline

print("=" * 50)
print("GPT-2 테스트 시작!")
print("=" * 50)


# GPT-2 모델 로딩 (처음엔 다운로드해서 시간 좀 걸림)
print("\n모델 로딩 중... (처음실행 시 1-2분 걸릴 수 있습니다)")
generator = pipeline("text-generation", model="gpt2")
# pipeline : 허깅페이스 트랜스포머 라이브러리에서 제공하는 간편한 인터페이스
# 모델 다운로드 , 실행 , 텍스트 ↔ 토큰 변환 ,
# 토크나이저로드 (토크나이저 : 텍스트를 AI 가 읽을 수 있도록 해주는 작업 ex. Hello → [3245, 1028])

# No module named 'transformers' error
# > pip install transformers torch


# 영어 질문 테스트
print("\n[테스트 1] 영어 질문")
prompt1 = "Python is a programming language that"
print(f"질문: {prompt1}")
result1 = generator(prompt1, max_length=50, num_return_sequences=1)
print(f"답변: {result1[0]['generated_text']}")

print("\n" + "=" * 50)


# 코딩 질문
print("\n[테스트 2] 코딩 질문")
prompt2 = "To sort a list in Python, you can"
print(f"질문: {prompt2}")
result2 = generator(prompt2, max_length=50, num_return_sequences=1)
print(f"답변: {result2[0]['generated_text']}")

print("\n" + "=" * 50)


# 한국어 테스트 (기대하지 말기. 재미로 해봄)
print("\n[테스트 3] 한국어 질문 (재미로)")
prompt3 = "파이썬은"
print(f"질문: {prompt3}")
result3 = generator(prompt3, max_length=30, num_return_sequences=1)
print(f"답변: {result3[0]['generated_text']}")

print("\n" + "=" * 50)
print("테스트 완료!")

# python test_gpt2.py 처음에 아무것도 안뜬다고 당황하지 말기 (백그라운드에서 다운로드 중)

# ------------------------------------------------------------------------
# 테스트 결과 (문장을 이어서 작성할 수 있도록 앞부분 만 얘기해 봄 )
# [테스트 1] 영어 질문
# 질문: Python is a programming language that
# 답변: Python is a programming language that allows you to work with data from your code, without needing to write any code.

# [테스트 2] 코딩 질문
# 질문 : To sort a list in Python, you can"
# 답변: To sort a list in Python, you can use the SortBy keyword to sort a list.


# [테스트 3] 한국어 질문 (재미로)
# 질문: 파이썬은
# 답변: 파이썬은 나를에서 븄로 쟠구정페의 장고우이 저에광이했다.

# 문장을 완성해주길 바랬는데, 알 수 없는 답변들을 했다.(모델의 한계)
