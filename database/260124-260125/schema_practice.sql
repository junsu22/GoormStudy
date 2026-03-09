PRAGMA foreign_keys = ON;

/*========================================================================
학생 테이블
========================================================================*/
CREATE TABLE student (
  student_id INTEGER PRIMARY KEY AUTOINCREMENT, -- 학생 ID (PK)
  name       TEXT NOT NULL,
  email      TEXT UNIQUE,
  birth_date TEXT,
  phone      TEXT,
  created_at TEXT DEFAULT (datetime('now')) -- 등록시각 
);


/*========================================================================
도서관 테이블
========================================================================*/
CREATE TABLE member (
  member_id  INTEGER PRIMARY KEY AUTOINCREMENT, -- 회원 ID (PK)
  name       TEXT NOT NULL,
  email      TEXT UNIQUE,
  phone      TEXT,
  created_at TEXT DEFAULT (datetime('now'))
);

CREATE TABLE book (
  book_id        INTEGER PRIMARY KEY AUTOINCREMENT,	 -- 도서 ID (PK)
  title          TEXT NOT NULL,
  author         TEXT,		-- 저자
  isbn           TEXT UNIQUE,		-- ISBN(중복 불가)
  published_year INTEGER	-- 출판년도
);

CREATE TABLE loan (
  loan_id     INTEGER PRIMARY KEY AUTOINCREMENT,	-- 대출 ID (PK)
  member_id   INTEGER NOT NULL,	-- 회원 ID (FK)
  book_id     INTEGER NOT NULL,	-- 도서 ID (FK)
  loan_date   TEXT,
  return_date TEXT,
  FOREIGN KEY (member_id) REFERENCES member(member_id),
  FOREIGN KEY (book_id)   REFERENCES book(book_id)
);


/*========================================================================
병원 예약 테이블
========================================================================*/
CREATE TABLE patient (
  patient_id INTEGER PRIMARY KEY AUTOINCREMENT,	-- 환자 ID (PK)
  name       TEXT NOT NULL,
  birth_date TEXT,
  phone      TEXT,
  created_at TEXT DEFAULT (datetime('now'))
);

CREATE TABLE doctor (
  doctor_id  INTEGER PRIMARY KEY AUTOINCREMENT,	-- 의사 ID (PK)
  name       TEXT NOT NULL,
  department TEXT,	 -- 진료과
  phone      TEXT,
  created_at TEXT DEFAULT (datetime('now'))
);

CREATE TABLE appointment (
  appointment_id       INTEGER PRIMARY KEY AUTOINCREMENT,	-- 예약 ID (PK)
  patient_id           INTEGER NOT NULL,	-- 환자 ID (FK)
  doctor_id            INTEGER NOT NULL,	-- 의사 ID (FK)
  appointment_datetime TEXT NOT NULL,	-- 예약 일시
  status               TEXT DEFAULT 'scheduled',	 -- 상태(scheduled/done/canceled)
  created_at           TEXT DEFAULT (datetime('now')),	-- 생성 시각
  FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
  FOREIGN KEY (doctor_id)  REFERENCES doctor(doctor_id)
);


/*========================================================================
주차 관리 테이블
========================================================================*/
CREATE TABLE vehicle (	
  vehicle_id   INTEGER PRIMARY KEY AUTOINCREMENT,-- 차량 ID (PK)
  plate_number TEXT UNIQUE,	-- 차량번호(중복 불가)
  owner_name   TEXT,	
  created_at   TEXT DEFAULT (datetime('now'))
);

CREATE TABLE parking_spot (	
  spot_id     INTEGER PRIMARY KEY AUTOINCREMENT,-- 주차공간 ID (PK)
  location    TEXT,
  hourly_rate INTEGER,	   -- 시간당 요금
  created_at  TEXT DEFAULT (datetime('now'))
);

CREATE TABLE parking (		
  parking_id INTEGER PRIMARY KEY AUTOINCREMENT,	-- 주차 기록 ID (PK)
  vehicle_id INTEGER NOT NULL,	-- 차량 ID (FK)
  spot_id    INTEGER NOT NULL,	-- 주차공간 ID (FK)
  start_time TEXT,	-- 입차 시간
  end_time   TEXT,	-- 출차 시간
  fee        INTEGER,	-- 요금(정산 결과)
  created_at TEXT DEFAULT (datetime('now')),	-- 생성 시각
  FOREIGN KEY (vehicle_id) REFERENCES vehicle(vehicle_id),
  FOREIGN KEY (spot_id)    REFERENCES parking_spot(spot_id)
);


/*========================================================================
음악 스트리밍 테이블
========================================================================*/
CREATE TABLE artist (
  artist_id  INTEGER PRIMARY KEY AUTOINCREMENT,	-- 아티스트 ID (PK)
  name       TEXT NOT NULL,
  created_at TEXT DEFAULT (datetime('now'))
);

CREATE TABLE album (
  album_id     INTEGER PRIMARY KEY AUTOINCREMENT,	 -- 앨범 ID (PK)
  artist_id    INTEGER NOT NULL,	-- 아티스트 ID (FK)
  title        TEXT NOT NULL,	-- 앨범명
  release_date TEXT,	 -- 발매일
  created_at   TEXT DEFAULT (datetime('now')),	-- 생성 시각
  FOREIGN KEY (artist_id) REFERENCES artist(artist_id)
);

CREATE TABLE track (
  track_id   INTEGER PRIMARY KEY AUTOINCREMENT,	-- 트랙 ID (PK)
  album_id   INTEGER NOT NULL,	-- 앨범 ID (FK)
  title      TEXT NOT NULL,	-- 트랙명
  duration   INTEGER,	 -- 재생 길이(초)
  created_at TEXT DEFAULT (datetime('now')),	
  FOREIGN KEY (album_id) REFERENCES album(album_id)
);

CREATE TABLE playlist (
  playlist_id INTEGER PRIMARY KEY AUTOINCREMENT,	-- 플레이리스트 ID (PK)	
  name        TEXT NOT NULL,
  created_at  TEXT DEFAULT (datetime('now'))
);

CREATE TABLE playlist_track (
  playlist_id INTEGER NOT NULL,	-- 플레이리스트 ID (FK)
  track_id    INTEGER NOT NULL,	 -- 트랙 ID (FK)
  added_at    TEXT DEFAULT (datetime('now')),
  PRIMARY KEY (playlist_id, track_id),	-- 중복 추가 방지(복합 PK)
  FOREIGN KEY (playlist_id) REFERENCES playlist(playlist_id),
  FOREIGN KEY (track_id)    REFERENCES track(track_id)
);
