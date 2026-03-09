
    -- csv 파일로 만든 테이블 조회 
    SELECT name
    FROM sqlite_master
    WHERE type='table'
    ORDER BY name;
    -- bird_tracking
    -- bird_tracking_devices




    -- bird_tracking_devices 의 첫번째 레코드 조회하기
    select species_code, catch_location, device_info_serial, sex, scientific_name, ring_code, bird_name
    from bird_tracking_devices
    where rowid = 1

    -- hg	Vismijn, Oostende	801	male	Larus argentatus	H903185	Jurgen


    -- hg : 재갈매기 . 
    -- loc / Oostende : 벨기에 오스텐트 에서 잡은 
    --  movebank.org 에서 조회가능 

    -- device_info_serial 의 851번 레코드 조회   
    select
        sex 성별,
        scientific_name 학명,
        bird_name 이름,
        tracking_started_at 추적시작일시,
        tracking_ended_at 추적종료일시
    from bird_tracking_devices
    where device_info_serial = 851;


    male	Larus fuscus	Eric	2013-05-28 18:00:00+00	


    select
        count(*) 총건수,
        count(distinct device_info_serial) 추적장치개수
    from bird_tracking
    -- 총건수  |   추적장치의 개수
    -- 61920	3


    select count(*) 건수
    from bird_tracking
    where device_info_serial = 851;
    -- eric 을 추적한 데이터의 갯수
    -- 19795

    -- SQLite에서는 date를 사용 못함. substr을 사용
    select
        device_info_serial 추적장치일련번호,
        substr(date_time, 1, 7) 년월,
        count(*) 건수
    from bird_tracking
    group by 추적장치일련번호, 년월
    order by 추적장치일련번호, 년월
    /*
    833	2013-08	1364
    833	2013-09	2434
    833	2013-10	2562
    833	2013-11	2438
    833	2013-12	2486
    833	2014-01	2524
    833	2014-02	2298
    833	2014-03	2542
    833	2014-04	2356
    851	2013-08	1413
    ...*/


