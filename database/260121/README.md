# Neo4j Flight-Airport Graph 실습

Neo4j를 사용한 항공사-공항 그래프 데이터베이스 구축 실습

## 프로젝트 개요

이 프로젝트는 Neo4j 그래프 데이터베이스를 처음 사용해보면서 항공사와 공항 간의 운항 관계를 모델링한 실습임.
CSV 데이터를 Neo4j에 임포트하고, Cypher 쿼리로 그래프 구조를 생성하는 과정을 다룸.

## 주요 내용

### 1. Cypher 기본 실습
- Flight, Airport 노드 생성
- 노드 간 관계(DEPARTS_TO) 생성
- Cartesian product 경고 처리 방법

### 2. CSV 데이터 임포트
- 파일: `20251231_clean_utf8.csv`
- 인코딩 문제 해결 (EUC-KR → UTF-8)
- `LOAD CSV WITH HEADERS` 구문 사용

### 3. 그래프 모델링

```
(Airline)-[OPERATES]->(Airport)
```

- **노드**: Airline, Airport
- **관계**: OPERATES (운항 정보 포함)
- **속성**: year, month, flight_count

## 데이터 구조

### CSV 컬럼
- `airline_icao`: 항공사 ICAO 코드
- `airline_name`: 항공사명
- `airport_code`: 공항 코드
- `country`: 국가
- `year`, `month`: 운항 연월
- `flight_count`: 운항 횟수

## 주요 쿼리

### Airline 노드 생성
```cypher
LOAD CSV WITH HEADERS
FROM 'file:///20251231_clean_utf8.csv' AS row
MERGE (a:Airline {icao: row.airline_icao})
SET a.name = row.airline_name;
```

### Airport 노드 생성
```cypher
LOAD CSV WITH HEADERS
FROM 'file:///20251231_clean_utf8.csv' AS row
MERGE (p:Airport {code: row.airport_code})
SET p.country = row.country;
```

### 관계 생성 (OPERATES)
```cypher
LOAD CSV WITH HEADERS
FROM 'file:///20251231_clean_utf8.csv' AS row
MATCH (a:Airline {icao: row.airline_icao})
MATCH (p:Airport {code: row.airport_code})
MERGE (a)-[r:OPERATES {
  year: toInteger(row.year),
  month: toInteger(row.month)
}]->(p)
SET r.flight_count = coalesce(r.flight_count, 0) + toInteger(row.flight_count);
```

### 결과 확인
```cypher
MATCH (a:Airline)-[r:OPERATES]->(p:Airport)
RETURN a, r, p
LIMIT 30;
```

## 주요 이슈 & 해결

### 인코딩 문제
- **문제**: CSV 파일의 한글이 깨짐 (EUC-KR 인코딩)
- **해결**: VS Code에서 "Reopen with Encoding" → EUC-KR로 열기 → "Save with Encoding" → UTF-8로 저장

### Neo4j CSV Import 경로
- Neo4j는 특정 import 디렉토리의 파일만 읽을 수 있음
- `file:///` 경로 사용

### Cartesian Product 경고
- 여러 MATCH 절을 `,`로 연결하면 경고 발생
- 각 MATCH를 분리해서 작성하는 것을 권장

## 파일 구성

- `neo4j-flight-airport.cypher`: 전체 Cypher 쿼리 코드
- `Neo4j_Flight_Airport_TIL.md`: 상세 학습 내용 정리
- `README.md`: 프로젝트 개요

## 실행 환경

- Neo4j Desktop
- CSV 파일: UTF-8 인코딩 필수

## 배운 점

- Neo4j 그래프 데이터베이스의 기본 개념
- Cypher 쿼리 언어 사용법
- CSV 데이터를 그래프로 변환하는 방법
- 노드와 관계를 활용한 데이터 모델링
- MERGE를 사용한 중복 방지 처리
- 관계에 속성을 추가해서 시계열 데이터 표현

