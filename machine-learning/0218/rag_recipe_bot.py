# -*- coding: utf-8 -*-
# pip install langchain langchain-community langchain-groq langchain-text-splitters faiss-cpu sentence-transformers

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
import os
import re


# ============================================
# Helper Functions  프롬프트로는 처리의 한계가 있음. 필터링 추가
# ============================================
def clean_japanese(text):
    """일본어 완전 제거"""
    text = re.sub(r"[\u3040-\u309F]", "", text)  # 히라가나
    text = re.sub(r"[\u30A0-\u30FF]", "", text)  # 카타카나
    text = re.sub(r"\s+", " ", text)  # 연속 공백 정리
    return text.strip()


# ============================================
# 1단계: Groq API 키 설정
# ============================================
os.environ["GROQ_API_KEY"] = ""

# ============================================
# 2단계: txt 파일 읽기
# ============================================
print("레시피 파일 읽는 중...")
loader = TextLoader("recipes.txt", encoding="utf-8")
documents = loader.load()
print(f"문서 로드 완료! (총 {len(documents)}개 문서)")

# ============================================
# 3단계: 문서를 작은 청크로 쪼개기
# ============================================
print("\n 문서를 청크로 쪼개는 중...")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(documents)
print(f" {len(chunks)}개 청크로 분할 완료!")

# ============================================
# 4단계: 임베딩 모델 준비 (한국어 지원)
# ============================================
print("\n 임베딩 모델 로딩 중...")
embeddings = HuggingFaceEmbeddings(
    model_name="jhgan/ko-sroberta-multitask", model_kwargs={"device": "cpu"}
)
print(" 임베딩 모델 로드 완료!")

# ============================================
# 5단계: FAISS 벡터 저장소 만들기
# ============================================
print("\n 벡터 DB 생성 중...")
vectorstore = FAISS.from_documents(chunks, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
print(" FAISS 벡터 저장소 생성 완료!")

# ============================================
# 6단계: Groq LLM 설정
# ============================================
print("\n Groq LLM 연결 중...")
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.2)
print("LLM 연결 완료!")

# ============================================
# 7단계: RAG 프롬프트 템플릿 만들기
# ============================================

template = """당신은 한식 레시피 전문 챗봇입니다.

**핵심 규칙:**
1. 질문에 정확히 답변만 하세요 (불필요한 서론, 인사, 부연설명 금지)
2. 레시피 질문: 재료 → 조리법 → 조리시간 → 난이도 → 꿀팁 형식으로만
3. 맥락 없는 질문("꿀팁은?", "재료는?"): "어떤 메뉴의 꿀팁/재료가 궁금하신가요?" 라고만 답변
4. 레시피 정보에 없으면: "죄송합니다. 해당 레시피는 등록되어 있지 않습니다."
5. 반드시 한국어로만 답변 (일본어 금지)

레시피 정보:
{context}

질문: {question}

답변 형식:
- 메뉴명만 물으면: 바로 재료부터 시작 (예: "재료: 김치 300g...")
- "꿀팁", "재료", "조리법" 만 물으면: 어떤 메뉴인지 물어보기
- 한 문장마다 줄바꿈
- 핵심만 간결하게"""

prompt = ChatPromptTemplate.from_template(template)

# ============================================
# 8단계: RAG 체인 구성
# ============================================
print("\n RAG 체인 구성 중...")


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

print(" RAG 체인 준비 완료!\n")

# ============================================
# 9단계: 챗봇 실행
# ============================================
print("=" * 50)
print("한식 레시피 RAG 챗봇이 준비되었습니다.")
print("=" * 50)
print("사용법: (한식) 궁금한 메뉴를 질문해주시면 됩니다! ")
print("종료: 'quit' 또는 'exit' 입력\n")

while True:
    user_question = input(" 질문: ")

    if user_question.lower() in ["quit", "exit", "종료"]:
        print(" 챗봇 종료!")
        break

    # RAG로 답변 생성
    print("\n 답변: ", end="")
    answer = rag_chain.invoke(user_question)
    answer = clean_japanese(answer)
    print(answer)

    print("\n" + "-" * 50 + "\n")

"""

테스트 화면
==================================================
 레시피 RAG 챗봇이 준비되었습니다.
==================================================
 사용법: (한식) 궁금한 메뉴를 질문해주시면 됩니다!
 종료: 'quit' 또는 'exit' 입력
 질문: 짜장면 만드는법 알아? 만드는 방법을 가르쳐 줘.
 답변: 레시피에 해당 정보가 없습니다. 
 제공된 레시피 정보에는 부대찌개, 김치찌개, 된장찌개의 조리법이 있지만, 짜장면 만드는 법에 대한 정보는 없습니다. 
 다른 레시피에 대한 도움이 필요하시면 언제든지 물어봐주세요!
--------------------------------------------------
 질문: 계란볶음밥은
 답변: 레시피에 해당 정보가 없습니다. 
 제공된 레시피 정보에는 비빔밥, 김치볶음밥, 미역국에 대한 정보만 있기 때문에 
 계란볶음밥에 대한 정보는 없습니다.
--------------------------------------------------
 질문: 김치볶음밥은?
 답변: 김치볶음밥은 재료와 조리법이 간단한 레시피로, 
 조리시간은 10분이며 난이도는 쉬움으로 분류됩니다. 
 김치볶음밥의 재료로는 밥 1공기, 김치 150g, 스팸 반캔, 
 김치국물 2스푼, 참기름,  김가루가 필요합니다. 
 조리법은 스팸을 먼저 볶은 후, 김치를 넣고 볶은 다음, 밥과 김치국물을 넣고 볶습니다. 
 마지막으로 참기름을 두르면 완성됩니다. 또한, 꿀팁으로 계란 프라이를 올리시면 더욱 맛있습니다. 

--------------------------------------------------
 질문: 난이도 쉬운 메뉴는?
 답변: 난이도 쉬운 메뉴는 두 가지가 있습니다. 
첫 번째는 부대찌개입니다. 부대찌개의 조리법은 비교적 단순하며, 조리시간도 15분으로 비교적 짧습니다. 
재료 준비와 조리 과정이 간단하여 누구나 쉽게 만들 수 있는 메뉴입니다.
두 번째는 떡볶이입니다. 떡볶이의 조리법도 간단하며, 조리시간도 15분으로 부대찌개와 동일합니다. 
재료 준비와 조리 과정이 간단하여 누구나 쉽게 만들 수 있는 메뉴입니다.
두 메뉴 모두 조리법이 간단하고 조리시간이 짧아, 난이도가 쉬운 메뉴로 분류됩니다.
--------------------------------------------------
 질문: 종료
 챗봇 종료!
"""

# 말을 제대로 하게 만드는 과정이 많이어려웠고
# 여러 시행 착오를 겪다보니 무료 크레딧을 다 사용하였다.
# 줄바꿈, 불필요한 정보 언급, 외국어 등등..
# groq.RateLimitError: Error code: 429 사용 한도 초과
