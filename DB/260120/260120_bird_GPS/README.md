# 조류 GPS 데이터 가공 보고서

## 1. 데이터 개요
- 데이터 출처: Movebank (조류 GPS 추적 데이터)
- 사용 테이블:
  - `bird_tracking_devices`: 개체(장치) 메타데이터
  - `bird_tracking`: GPS 위치 로그 데이터

## 2. 테이블 구조 확인
```sql
SELECT name
FROM sqlite_master
WHERE type='table'
ORDER BY name;
```
결과:
- bird_tracking
- bird_tracking_devices

## 3. 개체(장치) 정보 확인
```sql
SELECT
  species_code,
  catch_location,
  device_info_serial,
  sex,
  scientific_name,
  ring_code,
  bird_name
FROM bird_tracking_devices
WHERE rowid = 1;
```
- 예시 개체: 재갈매기 (Larus argentatus)
- 포획 위치: Oostende, Belgium

특정 개체 조회:
```sql
SELECT
  sex AS 성별,
  scientific_name AS 학명,
  bird_name AS 이름,
  tracking_started_at AS 추적시작일시,
  tracking_ended_at AS 추적종료일시
FROM bird_tracking_devices
WHERE device_info_serial = 851;
```

## 4. GPS 로그 데이터 규모 확인
```sql
SELECT
  COUNT(*) AS 총건수,
  COUNT(DISTINCT device_info_serial) AS 추적장치개수
FROM bird_tracking;
```
- 총 GPS 기록 수: 61,920건
- 추적 장치 수: 3개

특정 개체(Eric, 851번) 기록 수:
```sql
SELECT COUNT(*) AS 건수
FROM bird_tracking
WHERE device_info_serial = 851;
```
- 19,795건

## 5. 날짜 데이터 가공 (월 단위 집계)
SQLite 환경에서 문자열 기반 날짜 처리를 위해 `substr()` 함수를 사용하였다.

```sql
SELECT
  device_info_serial AS 추적장치일련번호,
  substr(date_time, 1, 7) AS 년월,
  COUNT(*) AS 건수
FROM bird_tracking
GROUP BY 추적장치일련번호, 년월
ORDER BY 추적장치일련번호, 년월;
```

## 6. 정리
- 원본 GPS 로그 데이터는 개체별, 시간별로 분산되어 있어 가공이 필요함을 확인하였다.
- 개체 식별, 로그 필터링, 문자열 기반 날짜 가공을 통해 데이터 구조를 이해하기 쉬운 형태로 변환하였다.
- 이를 통해 조류 이동 데이터 전처리 과정을 경험하였다.
