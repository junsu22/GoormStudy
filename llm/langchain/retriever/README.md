# LangChain Retriever 비교 실습

다양한 검색기(Retriever)를 실습하고 특성을 비교한 노트북 모음입니다.

## 실습 내용

| 파일 | 검색기 | 핵심 내용 |
|------|--------|-----------|
| [01-VectorStoreRetriever.ipynb](./01-VectorStoreRetriever.ipynb) | VectorStoreRetriever | similarity / MMR / score_threshold |
| [03-EnsembleRetriever.ipynb](./03-EnsembleRetriever.ipynb) | EnsembleRetriever | BM25 + FAISS 결합, RRF 재순위화 |
| [06-MultiQueryRetriever.ipynb](./06-MultiQueryRetriever.ipynb) | MultiQueryRetriever | LLM 기반 다중 쿼리 생성 |
| [10-Kiwi-BM25Retriever.ipynb](./10-Kiwi-BM25Retriever.ipynb) | Kiwi-BM25Retriever | 한국어 형태소 분석 + BM25 |

## 검색기 비교

| 검색기 | 방식 | 적합한 상황 |
|--------|------|------------|
| VectorStoreRetriever | 의미 유사도 | 자연어 질의 |
| EnsembleRetriever | 키워드 + 의미 혼합 | 실전 RAG |
| MultiQueryRetriever | LLM 쿼리 확장 | 모호한 질문 |
| Kiwi-BM25Retriever | 한국어 형태소 + BM25 | 한국어 데이터 |

## 블로그

- [LangChain Retriever 비교 실습](https://velog.io/@junsu22/Retriever)

## 환경 설정

```bash
pip install langchain langchain-community langchain-openai langchain-teddynote
pip install faiss-cpu rank_bm25 kiwipiepy beautifulsoup4
```

`.env` 파일에 API 키 설정:
```
OPENAI_API_KEY=your_key
LANGSMITH_API_KEY=your_key
```
