// ============================================================
// Neo4j Practice: Flight - Airport Graph (Cypher Basics)
// + CSV Import: Airline - Airport OPERATES Graph
// ============================================================


// ============================================================
// Cypher 기본 실습: Flight / Airport
// ============================================================

// Flight 노드 생성
CREATE (:Flight {
  number: 23,
  airline: 'Delta',
  capacity: 160
});

// Airport 노드 2개 생성 (DTW, ATL)
CREATE (:Airport {
  label: 'DTW',
  city: 'Detroit',
  state: 'Michigan'
});

CREATE (:Airport {
  label: 'ATL',
  city: 'Atlanta',
  state: 'Georgia'
});

// 관계 생성: Flight -> Airport
// ⚠ Cartesian product 경고 예시 (에러는 아니지만 데이터가 커지면 느려질 수 있음)
// MATCH (f:Flight {number: 23}), (a:Airport {label: 'ATL'})
// CREATE (f)-[:DEPARTS_TO]->(a);

// 권장: 조건을 분리해서 명확하게 매칭 후 관계 생성
MATCH (f:Flight {number: 23})
MATCH (a:Airport {label: 'ATL'})
CREATE (f)-[:DEPARTS_TO]->(a);

// 확인: 지금 만든 노드/관계 조회
MATCH (n) RETURN n;
MATCH (f:Flight)-[r:DEPARTS_TO]->(a:Airport) RETURN f, r, a;

// 초기화(전체 삭제)
// 필요할 때만 실행!
MATCH (a)
OPTIONAL MATCH (a)-[r]-()
DELETE a, r;


// ============================================================
// CSV Import 전 점검 (헤더/샘플 확인)
// ============================================================
// 사용 파일 예시: 20251231_clean_utf8.csv
// - UTF-8로 저장된 CSV를 기준으로 진행

// (B-1) 샘플 row 확인 (필드명이 제대로 보이는지)
LOAD CSV WITH HEADERS
FROM 'file:///20251231_clean_utf8.csv' AS row
RETURN row.airline_name, row.country, row.airport_code, row.flight_count
LIMIT 5;

// (B-2) 헤더(컬럼명) 확인
LOAD CSV WITH HEADERS
FROM 'file:///20251231_clean_utf8.csv' AS row
RETURN keys(row) AS headers
LIMIT 1;


// ============================================================
// CSV Import: Airline / Airport 노드 + OPERATES 관계
// ============================================================

// Airline 노드 생성/병합
LOAD CSV WITH HEADERS
FROM 'file:///20251231_clean_utf8.csv' AS row
MERGE (a:Airline {icao: row.airline_icao})
SET a.name = row.airline_name;

// Airport 노드 생성/병합
LOAD CSV WITH HEADERS
FROM 'file:///20251231_clean_utf8.csv' AS row
MERGE (p:Airport {code: row.airport_code})
SET p.country = row.country;

// Airline -> Airport 관계 생성 (OPERATES)
// - year/month는 관계 식별에 포함
// - flight_count는 숫자형 변환
//
// 같은 (airline_icao, airport_code, year, month) 조합이
// 여러 번 들어올 가능성이 있으면 SET으로 덮어쓰지 말고 누적 방식이 안전
// 아래는 "누적" 방식(추천)
LOAD CSV WITH HEADERS
FROM 'file:///20251231_clean_utf8.csv' AS row
MATCH (a:Airline {icao: row.airline_icao})
MATCH (p:Airport {code: row.airport_code})
MERGE (a)-[r:OPERATES {
  year: toInteger(row.year),
  month: toInteger(row.month)
}]->(p)
SET r.flight_count = coalesce(r.flight_count, 0) + toInteger(row.flight_count);


// ============================================================
// 결과 확인 / 분석 쿼리
// ============================================================

// 일부 관계 확인 (그래프/테이블로 보기)
MATCH (a:Airline)-[r:OPERATES]->(p:Airport)
RETURN a, r, p
LIMIT 30;


// ============================================================
// 추가 참고: CSV 인코딩 문제 해결 과정
// ============================================================

// Neo4j import 는 아무 폴더의 csv 를 못읽는다..
// 1) 인코딩부터 고치기 (한글 깨짐 해결)
// 방법 A: VS Code로 고치기 (가장 빠름)
//
// - VS Code에서 20251231.csv 열기
// - 오른쪽 아래에 UTF-8 같은 글자 → 클릭
// - "Reopen with Encoding…" 선택
// - 목록에서 Korean (CP949) 또는 EUC-KR 로 열어보기
//   → 한글이 정상으로 보이는 쪽 선택!
// - 다시 오른쪽 아래 인코딩 클릭 → "Save with Encoding…"
// - UTF-8로 저장

// import 하려고 했는데 헤더 정리가 필요함..
// 2025,01,AAL,AA,아메리칸항공,미국,미국,미국,DFW,미국,미국,미국,29 ,4762 ,22 ,2938 ,226482 ,0 ,20853 ,160667
// 2025,01,AAR,OZ,아시아나항공,한국,한국,한국,CJU,한국,제주도,한국,1 ,232 ,0 ,0 ,0 ,0 ,0 ,1305
// 2025,01,AAR,OZ,아시아나항공,한국,일본,일본,AKJ,일본,아키타,일본,17 ,2172 ,6 ,85 ,0 ,0 ,0 ,29890
// ...


// ============================================================
// Neo4j CSV 데이터 적재 실습 정리 (260121)
// ============================================================

// 이번 실습에서는 Neo4j에서 처음으로 `LOAD CSV WITH HEADERS` 구문을 사용해서
// CSV 데이터를 그래프 데이터베이스에 적재해봄.
// 데이터 인코딩(EUC-KR → UTF-8) 문제와 헤더 깨짐 이슈를 해결한 후,
// 정제된 CSV 파일을 기반으로 항공사–공항 관계를 모델링함.

// 1. CSV 데이터 구조
// 정제된 CSV(`20251231_clean_utf8.csv`)에는 다음과 같은 주요 컬럼이 포함되어 있음:
// - `airline_icao` : 항공사 ICAO 코드
// - `airline_name` : 항공사명
// - `airport_code` : 공항 코드
// - `country` : 국가
// - `year`, `month` : 운항 연월
// - `flight_count` : 운항 횟수
//
// 이 중 **항공사와 공항은 노드**,
// **운항 정보는 관계의 속성**으로 모델링함.

// 2. Airline 노드 생성
// CSV 파일을 한 줄씩 읽어옴 (헤더 포함)
// 항공사 고유값(ICAO)을 기준으로 Airline 노드를 생성하거나 재사용
// 항공사 이름을 속성으로 저장
// MERGE를 사용해서 동일한 항공사가 중복 생성되지 않도록 처리함.
// 항공사의 고유 식별자는 ICAO 코드를 기준으로 삼음.

// 3. Airport 노드 생성
// CSV 파일을 다시 읽어옴
// 공항 코드를 기준으로 Airport 노드를 생성하거나 재사용
// 공항이 속한 국가 정보를 저장
// 공항은 airport_code를 기준으로 하나의 노드만 유지하도록 함.

// 4. Airline → Airport 관계 생성 (운항 정보)
// CSV 파일을 읽어옴
// 이미 생성된 Airline 노드를 찾음
// 이미 생성된 Airport 노드를 찾음
// 항공사가 공항을 운항한다는 관계를 생성
// 운항 횟수를 관계의 속성으로 저장
// 운항 연도(year), 월(month), 운항 횟수(flight_count)는
// 관계(OPERATES)의 속성으로 저장함.
// 숫자 비교가 가능하도록 toInteger()로 형 변환을 수행함.

// 5. 결과 확인
// 위 쿼리를 통해 항공사–공항 간 운항 관계가 그래프 형태로 정상 생성됨을 확인함.

// 정리:
// - CSV 인코딩 문제(EUC-KR → UTF-8)를 해결한 후 Neo4j에 데이터 적재 성공
// - 항공사와 공항을 노드로 분리해서 그래프 구조로 모델링
// - 운항 정보는 관계의 속성으로 표현해서 시계열 분석이 가능하도록 구성
// - Neo4j와 LOAD CSV 구문을 처음 사용해본 실습이었지만,
//   데이터 구조를 이해하고 그래프 모델링의 기본 개념을 익힐 수 있었음.
