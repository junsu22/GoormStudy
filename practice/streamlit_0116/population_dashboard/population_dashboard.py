"""
Streamlit 대시보드 - 출생/출산 지표 (통계청 데이터 기반)

- st.session_state로 세션 관리
- st.cache_data / st.cache_resource로 캐싱 처리
- 통계청 데이터 기반 대시보드 (전처리 → EDA → 시각화)

- 행: 지표(출생아수, 합계출산율, 자연증가 등)
- 열: 연도 (예: 2018, 2019, 2020, 2021, 2022, 2023, 2024)
"""

import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
import requests

# ---------------------------
# 페이지 설정
# ---------------------------
st.set_page_config(page_title="출생/출산 지표 대시보드", layout="wide")
st.title("출생/출산 지표 대시보드")
st.caption("통계청(KOSIS) 데이터 기반 | 전처리 → EDA → Plotly 시각화 실습")


# ---------------------------
# 캐싱
# ---------------------------
@st.cache_data(show_spinner=False)  # 데이터를 캐싱. 로딩 표시 숨김
def load_csv(path: str) -> pd.DataFrame:  # 이 함수의 파라미터 값은 Str 형이어야 함.
    try:
        return pd.read_csv(
            path, encoding="utf-8-sig"
        )  # utf-8-sig :CSV 읽을 때 쓰는 안전한 인코딩
    except Exception:  # 어떤 에러라도
        return pd.read_csv(path, encoding="cp949")  # cp949 : window에서 사용하는 인코딩


@st.cache_resource  # 무거운 객체를 한 번만 생성하고 재사용하는 데코레이터
def get_session() -> (
    requests.Session
):  # API 호출용 세션 객체 반환 (연결 재사용으로 속도 향상)
    return requests.Session()


# indicator = 측정/분석 대상
# to_long 세로 형으로 길게 (wide : 가로)
def to_long(df_wide: pd.DataFrame) -> pd.DataFrame:
    first_col = df_wide.columns[0]
    # 첫 번째 컬럼 이름을 "indicator"로 바꾸고 복사본 생성, 원본 보호 목적
    df = df_wide.rename(columns={first_col: "indicator"}).copy()
    year_cols = df.columns[1:]
    df_long = df.melt(  #   .melt 가로였던 컬럼들을 녹여서 세로로 펼침
        id_vars=["indicator"], value_vars=year_cols, var_name="year", value_name="value"
    )
    df_long["year"] = pd.to_numeric(df_long["year"], errors="coerce").astype("Int64")
    df_long["value"] = pd.to_numeric(df_long["value"], errors="coerce")
    return df_long.dropna(subset=["year"]).sort_values(["indicator", "year"])


# ---------------------------
# 데이터 로드
# ---------------------------
BASE_DIR = (
    Path(__file__).resolve().parent
)  # resolve : 상대경로를 절대경로로 , .parent 부모 디렉토리(한 단계 위)
DATA_PATH = BASE_DIR / "data" / "kosis_birth_fertility_natural_change_by_year.csv"

if not DATA_PATH.exists():
    st.error(f".CSV 파일을 찾을 수 없습니다.\n경로: {DATA_PATH}")
    st.stop()

raw = load_csv(str(DATA_PATH))
df = to_long(raw)

indicators = df["indicator"].dropna().unique().tolist()
if not indicators:
    st.error(
        "지표 데이터 컬럼을 읽지 못했습니다. CSV 구조를 확인해주세요."
    )  # 컬럼을 확인 했으나 읽지못함.
    st.stop()

# ---------------------------
# 세션 상태 초기화
# st.session_state  스트림릿은 입력때 마다 스크립트를 다시 실행함.
# st.session_state 에서는 값을 유지 시켜줌.
# ---------------------------
if "indicator" not in st.session_state:
    st.session_state.indicator = indicators[0]
# 년도를 오름차순 정렬
years = sorted(
    df["year"].dropna().unique().tolist()
)  # year 컬럼 선택 → 빈값 제거 → 중복 제거 → 리스트 변환
# 세션에 연도 범위가 없고 years가 비어있지 않으면 초기화
if "year_range" not in st.session_state and years:
    st.session_state.year_range = (
        int(years[0]),  # 첫번째 년도   (최솟값)
        int(years[-1]),  # 마지막 년도   (최댓값)
    )

# ---------------------------
# 사이드바
# ---------------------------
st.sidebar.header("설정")

st.session_state.indicator = st.sidebar.selectbox(
    "지표 선택", indicators, index=indicators.index(st.session_state.indicator)
)

st.session_state.year_range = st.sidebar.slider(
    "연도 범위",
    min_value=int(min(years)),
    max_value=int(max(years)),
    value=st.session_state.year_range,
)

if st.sidebar.button("캐시 초기화"):
    st.cache_data.clear()
    st.cache_resource.clear()
    st.success("캐시 초기화 완료")

# ---------------------------
# 데이터 필터링 : 데이터가 없다면 경고 후 중단
# ---------------------------
start_y, end_y = st.session_state.year_range  # 튜플 언패킹 (시작과 끝 년도)
df_sel = df[
    (df["indicator"] == st.session_state.indicator)
    & (df["year"].between(start_y, end_y))
].dropna(subset=["value"])

if df_sel.empty:
    st.warning("선택한 조건에 해당하는 데이터가 없습니다..")
    st.stop()

# ---------------------------
# KPI
# ---------------------------
# 최신 데이터
latest_year = int(df_sel["year"].max())
latest_value = float(df_sel[df_sel["year"] == latest_year]["value"].iloc[0])
# 전 년도 데이터
prev_year = latest_year - 1
prev_row = df_sel[df_sel["year"] == prev_year]
prev_value = float(prev_row["value"].iloc[0]) if not prev_row.empty else None

# 증감계산
delta = None  # 증감량
delta_pct = None  # 증감률
if prev_value is not None and prev_value != 0:  # 전년데이터가 있고, 0이 아니라면
    delta = latest_value - prev_value  # 차이
    delta_pct = (delta / prev_value) * 100  # 증감률 (백분율)

# KPI 표시
c1, c2, c3 = st.columns(3)  # 3개의 컬럼을 생성
c1.metric("최신 연도", latest_year)
c2.metric(
    "최신 값",
    (
        f"{latest_value:,.3f}" if abs(latest_value) < 1000 else f"{latest_value:,.0f}"
    ),  # 1000 미만, 소수점 셋째 자리, 이상이면 정수
)
c3.metric("전년 대비 증감률", "N/A" if delta_pct is None else f"{delta_pct:.2f}%")
# 없으면 N/A , 있으면 %


# ---------------------------
# 시각화
# ---------------------------
# 라인 차트 생성
fig = px.line(
    df_sel,  # 데이터
    x="year",  # x : 년도
    y="value",  # y : 값
    markers=True,  # 데이터 포인트 표시
    title=f"{st.session_state.indicator} 연도별 추이",  # 제목
)
# 화면 너비에 맞춤
st.plotly_chart(fig, use_container_width=True)
# 접을 수 있는 영역
with st.expander("데이터 미리보기 (EDA)"):
    st.dataframe(
        df_sel.sort_values("year"), use_container_width=True  # 년도 순 정렬
    )  # use_container_width=True : 화면 너비에 맞춤
