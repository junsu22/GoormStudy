
테이블 조회
SELECT name FROM sqlite_master WHERE type='table';

Person table 조회
SELECT * FROM Person;

데이터 1 추가(완)
INSERT INTO Person (ID, Name, Birthday)
VALUES (1,'이혜리', '1994-06-09');

모든 컬럼 순서대로 값을 넣을 때는 컬럼명 생략 가능
INSERT INTO Person
VALUES (1, '이혜리', '1994-06-09');
문장하나만 입력시에는 세미콜론 생략 가능
PK, 이미 존재하는 ID로 행을 삽입 불가.

삭제(완) 데이터 사라짐
DELETE FROM Person;

추가
INSERT INTO Person VALUES (1, '이혜리', '1994-06-09');
업데이트
UPDATE Person SET Name = '혜리';

테이블, 모든 행,열 조회
SELECT * FROM Person;

행 삭제 (ID,Name, Birthday 같은 구조만 남고 데이터 다 지워짐)
DELETE FROM Person;

데이터 추가
INSERT INTO Person VALUES(1, '이혜리', '1994-06-09');
업데이트 이름이 이혜리 > 혜리 로 바뀜.
UPDATE Person Set Name = '혜리';

데이터 2개 추가
INSERT INTO Person (Name, Birthday)
VALUES ('박소진', '1986-05-21'), ('김아영', '1992-11-06');

'민아' 의 생일값 null로 데이터 추가
INSERT INTO Person (Name) VALUES ('민아');

ㄱㄴㄷ순 오름차 정렬(김아영,민아..)
SELECT Name FROM Person ORDER BY Name;
맨 뒤에서 부터 정렬 (혜리, 박소진..)
SELECT Name FROM Person ORDER BY Name DESC;

특정 데이터 찾기 .
SELECT * FROM Person WHERE Name = '박소진';

생일이 null 값이 아닌 데이터만 조회('민아'출력x)
SELECT * FROM Person
WHERE Birthday IS NOT NULL

'박소진'> '소진'
UPDATE Person SET Name = '소진' WHERE Name = '박소진';

'1986'이라는 데이터를 포함하는
SELECT * FROM Person WHERE Birthday LIKE '1986%';

'지선,지인 의 데이터를 추가'
INSERT INTO Person (Name, Birthday) VALUES ('지선', '1989-10-17');
INSERT INTO Person (Name, Birthday) VALUES ('지인', '1992-3-13');

id,name,Birthday 옆 new 라는 명의 컬럼 추가 (데이터는 NULL)
ALTER TABLE Person ADD COLUMN New INTEGER;

New 컬럼의 특정 데이터 중 NULL을 값으로 변경
UPDATE Person SET New = 164 WHERE NAME = '민아' ;
UPDATE Person SET New = 167 WHERE Name = '소진' ;
UPDATE Person SET New = 170.3 WHERE Name = '유라';

기존의 작업중이던 테이블 drop
데이터가 삭제됨 . 되돌릴 수 없음. 조회되지 않았음.
DROP TABLE Person;

테이블 새로 만듬.
CREATE TABLE "Person" (
    "Name"  TEXT NOT NULL,
    "Birthday"  TEXT,
    "Height"    INTEGER,
    "Weight"    INTEGER,
    ID INTEGER PRIMARY KEY AUTOINCREMENT
);

	AUTOINCREMENT : insert 할때 알아서 다음 큰 ID를 넣어줌 	(SQLite 옵션)
	ID INTEGER PRIMARY KEY AUTOINCREMENT 행 마다 자동으로 번호(ID) 증가
	PRIMARY KEY("ID" AUTOINCREMENT)	SQLite에서는 AUTOINCREMENT를 PRIMARY KEY() 구문 안에 쓸 수 없다
	AUTOINCREMENT는 INTEGER PRIMARY KEY 컬럼 정의에서만 허용된다

모든테이블 확인 , Person 테이블이 지워 진것을 확인
SELECT name
FROM sqlite_master
WHERE type = 'table';

INSERT INTO Person VALUES
    (1, '혜리', '1994-06-09', NULL, 50),
    (2, '소진', '1986-05-21', 167, NULL),
    (3, '유라', '1992-11-06', 170.3, 54),
    (4, '민아', NULL, 164, 46);

잘 insert 되었는지
SELECT * FROM Person

컬럼명 2개에 별명 붙여줌( 테이블 자체에 컬렴명이 바뀌는건 아니었음)
SELECT
    Name AS "이름",
    Birthday AS "생일"
FROM Person;

BMI 구하기
round() 함수는 소수점 이하에 대하여 반올림
SELECT
    Name,
    Height,
    Weight,
    round(weight / (height * height * 0.0001), 1) BMI
FROM Person;

뷰 생성
CREATE VIEW BirthdayView
AS
SELECT
    Name,
    Birthday bdate,
    substr(Birthday, 1, 4) YYYY,
    substr(Birthday, 6, 2) MM,
    substr(Birthday, 9, 2) DD
FROM Person;

SELECT * FROM BirthdayView;
확인했더니 데이터가 전부 잘못 들어감..

DROP TABLE IF EXISTS Person;
다시삭제
다시 테이블 생성
CREATE TABLE Person (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Birthday TEXT,
    Height REAL,
    Weight INTEGER
);

데이터 새로 입력
INSERT INTO Person (Name, Birthday, Height, Weight) VALUES
    ('혜리', '1994-06-09', NULL, 50),
    ('소진', '1986-05-21', 167, NULL),
    ('유라', '1992-11-06', 170.3, 54),
    ('민아', NULL, 164, 46);

SELECT * FROM BirthdayView;
*/

/*
혜리	1994-06-09	1994	06	09
소진	1986-05-21	1986	05	21
유라	1992-11-06	1992	11	06
민아
*/

조건절 Oracle 의 Decode()를 제공하지 않음. case 를 사용한다.

SELECT
    Name,
    bdate,
    MM,
    CASE
        WHEN MM = '01' THEN 'Jan.'
        WHEN MM = '02' THEN 'Feb.'
        WHEN MM = '03' THEN 'Mar.'
        WHEN MM = '04' THEN 'Apr.'
        WHEN MM = '05' THEN 'May.'
        WHEN MM = '06' THEN 'Jun.'
        WHEN MM = '07' THEN 'Jul.'
        WHEN MM = '08' THEN 'Aug.'
        WHEN MM = '09' THEN 'Sep.'
        WHEN MM = '10' THEN 'Oct.'
        WHEN MM = '11' THEN 'Nov.'
        WHEN MM = '12' THEN 'Dec.'
    END Month
FROM BirthdayView;

-- 다른방법
SELECT
    Name,
    bdate,
    MM,
    substr('JanFebMarAprMayJunJulAugSepOctNovDec', (CAST(MM AS INTEGER)-1)*3 + 1, 3) || '.' AS Month
FROM BirthdayView;

혜리	1994-06-09	06	Jun.
소진	1986-05-21	05	May.
유라	1992-11-06	11	Nov.
민아			


로컬 타임을 붙여줘야 현재 시간으로 나옴.('localtime'빼면 세계 표준시 출력됨)
SELECT strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime') 현지시간;


-- 만나이 구하기
SELECT
	name "이름",
    Birthday "생일",
    strftime('%Y', 'now') - substr(Birthday, 1, 4) - (strftime('%m-%d', 'now') < substr(Birthday, 6)) "나이"
 FROM Person
 WHERE Name IN ('혜리', '소진', '민아','유라')
 ORDER by "나이" desc;
 
 
집계 함수 연습 
 SELECT Height FROM Person;

167.0
170.3
164.0

 
 모든 행의 개수 > 4개
SELECT count(*) FROM Person;


특정 컬럼에 데이터가 있는 행을 세기/ 3개


셀수 있는 개수 3개 
-- SELECT count(Height) FROM Person;
NULL인 개수 1개
SELECT COUNT(*)
FROM Person
WHERE Height IS NULL;

-- height 최댓값, 최솟값 구하기
-- SELECT max(Height) FROM Person;
-- SELECT min(Height) FROM Person;
-- -- 컬럼한개의 모든 값들을 합한
-- SELECT sum(Height) FROM Person;



SELECT 
max(Height)"최댓값",
min(Height)"최소값",
sum(Height)"키 합계",
avg(Height)"키 평균"
FROM Person;
	
최대값	|최소값	|키합계	|키평균
170.3	164.0	501.3	167.1





UPDATE Person
SET Height = 166.8
WHERE Name = '혜리';



SELECT round(Height), count(*)
FROM   Person
GROUP  BY 1;


-- 반올림 한 값이 같은 . 사람 수 
데이터는 총 4개 
164 그룹 1명| 167 2명 | 170 1명
SELECT round(Height), count(*)
FROM   Person
GROUP  BY round(Height);

164.0	1
167.0	2
170.0	1

==============================================================
-- 새로운 테이블 생성
CREATE TABLE 노래 (
  ID INTEGER NOT NULL PRIMARY KEY,
  제목 TEXT NOT NULL
);

CREATE TABLE 음반 (
  ID INTEGER NOT NULL PRIMARY KEY,
  제목 TEXT NOT NULL,
  연도 INTEGER
);
CREATE TABLE 수록곡 (
  음반ID INTEGER NOT NULL,
  노래ID INTEGER NOT NULL
);



-- 데이터 INSERT
INSERT INTO 노래 VALUES
(1, '갸우뚱'),
(2, 'Shuppy Shuppy'),
(3, 'Control'),
(4, '영러브'),
(5, '한번만 안아줘'),
(6, '반짝반짝'),
(7, '기대해'),
(8, 'I Don''t Mind'),
(9, 'Easy go'),
(10, '여자대통령');
INSERT INTO 음반 VALUES
(1, 'Girl''s Day Party #1', 2010),
(2, 'Everyday', 2011),
(3, 'Expectation', 2013),
(4, '여자대통령', 2013);
INSERT INTO 수록곡 VALUES 
(1, 1),
(1, 2),
(1, 3),
(2, 4),
(2, 5),
(2, 6),  -- Everyday - 반짝반짝
(3, 7),
(3, 8),
(3, 9),
(3, 6),  -- Expectation - 반짝반짝
(3, 5),
(4, 10);





SELECT 음반.제목 앨범명, 음반.연도 발매년도, 노래.제목 곡명
FROM 수록곡 -- 기준으로
INNER JOIN 음반 ON 수록곡.음반ID = 음반.ID	-- 음반 > 음반 ID 연결
INNER JOIN 노래 ON 수록곡.노래ID = 노래.ID -- 노래 > 노래 ID 연결
WHERE 음반.연도 = 2011;	-- 2011년 데이터만 추출 



