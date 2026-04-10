# LangChain Document Loader 비교 실습

데이터 형식별 Document Loader를 실습하고 비교한 노트북 모음입니다.

## 실습 내용

| 파일 | 로더 | 형식 |
|------|------|------|
| [01-PDF-Loader.ipynb](./01-PDF-Loader.ipynb) | PyPDFLoader | PDF |
| [02-HWP-Loader.ipynb](./02-HWP-Loader.ipynb) | HWPLoader | HWP |
| [03-CSV-Loader.ipynb](./03-CSV-Loader.ipynb) | CSVLoader | CSV |
| [07-WebBase-Loader.ipynb](./07-WebBase-Loader.ipynb) | WebBaseLoader | HTML |
| [09-JSON-Loader.ipynb](./09-JSON-Loader.ipynb) | JSONLoader | JSON |

## 로더 비교

| 로더 | 형식 | 적합한 상황 |
|------|------|------------|
| PyPDFLoader | PDF | 일반 문서, 논문, 보고서 |
| HWPLoader | HWP | 국내 공공/기업 문서 |
| CSVLoader | CSV | 정형 테이블 데이터 |
| WebBaseLoader | HTML | 웹페이지 크롤링 |
| JSONLoader | JSON | 구조화 데이터 특정 필드 추출 |

## 블로그

- [LangChain Document Loader 비교](https://velog.io/@junsu22/LangChain-Document-Loader)

## 환경 설정

```bash
pip install langchain langchain-community langchain-openai
pip install pypdf jq beautifulsoup4
```

`.env` 파일에 API 키 설정:
```
OPENAI_API_KEY=your_key
```
