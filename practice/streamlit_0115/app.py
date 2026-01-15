# st.metric

# st.tabs

# st.expander

# st.dataframe
# metric 컴포넌트를 활용하여 주요 매출 지표를 카드 형태로 표시하였고,
# tabs를 사용해 매출 추이/상품별 분석/데이터 화면을 구분하였다.
# expander를 통해 사용 가이드를 접었다 펼 수 있도록 구성하였다.


import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# 페이지 설정   (wide : 화면 넓게 쓰기)
st.set_page_config(page_title="편의점 매출 대시보드", layout="wide")

# 컬러 팔레트   (브랜드 컬러 담음)
BRAND_COLORS = ["#00AB84", "#00D4AA", "#7FDBCA", "#B3E8DC"]

# 스타일
st.markdown(
    """
    <style>
    /* 메인 배경 */
    .stApp {
        background-color: #f0f8f0;
    }
    
    /* 사이드바 배경 */
    [data-testid="stSidebar"] {
        background-color: #00AB84;
    }
    
    /* 사이드바 텍스트 흰색 */
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* 메트릭 박스 */
    [data-testid="stMetricValue"] {
        color: #00AB84;
        font-weight: bold;
    }
    
    /* 제목 색상 */
    h1 {
        color: #00AB84 !important;
    }
    
    h2, h3 {
        color: #007A5E !important;
    }
    </style>
    """,
    unsafe_allow_html=True,  # CSS로 색상 커스터마이징 시 필요
)

# 제목
st.title("🏪 우리집앞 C* 편의점 매출")
st.write("⚠️ Made by Junsu | 본 데이터는 사실과 무관합니다.")


# 데이터 생성
@st.cache_data  # 슬라이더를 움직일때마다  load_data를 다시 실행함.
# 처음만 실행하고 저장된 것 (캐시)를 사용 하기 위해 추가
def load_data():
    """데이터 생성"""
    np.random.seed(42)
    dates = pd.date_range("2025-12-01", "2026-01-15", freq="D")
    n = len(dates)

    df = pd.DataFrame(
        {
            "날짜": dates,
            "요일": [d.strftime("%A") for d in dates],
            "매출": np.random.randint(500000, 2000000, n),
            "손님수": np.random.randint(200, 800, n),
            "상품": np.random.choice(["도시락", "음료", "과자", "생활용품"], n),
        }
    )
    df["객단가"] = df["매출"] // df["손님수"]
    return df


df = load_data()

# =====================================================================================
# 사이드바 (필터)
# =====================================================================================
# form 여러입력을 한번에 묶기
with st.sidebar:  # 사이드바 영역
    st.header("🔍 필터 설정")
    with st.form("filter_form"):
        st.subheader("조건 선택")

        # 매출 범위 (슬라이더)
        min_sales = st.slider("최소 매출액", 0, 2000000, 500000, 100000)

        # 상품 선택 (다중선택)
        products = st.multiselect(
            "상품 카테고리",
            ["도시락", "음료", "과자", "생활용품"],
            default=["도시락", "음료", "과자", "생활용품"],
        )

        # 적용 버튼 (폼 제출)
        submitted = st.form_submit_button(
            "필터 적용 🔄"
        )  # 현재는 입력값이 바뀌면 바로 필터가 적용되며, 버튼 클릭 여부(submitted)는 추후 기능 확장을 위해 남겨둠

# 필터 적용
filtered = df[df["매출"] >= min_sales]
if products:
    filtered = filtered[filtered["상품"].isin(products)]

# 데이터 없을 때 처리
if len(filtered) == 0:
    st.warning("⚠️ 조건에 맞는 데이터가 없습니다. 필터를 조정해주세요!")
    st.stop()

# =====================================================================================
# 주요 지표(사장님이 중요하게 생각하는 것들)  KPI  (Key Performance Indicator)
# =====================================================================================
st.subheader("📊 평균 매출 현황")

col1, col2, col3, col4 = st.columns(4)
# 화면을 가로 4개로 나눔, 숫자를 카드형태로 크게 표시
# metric: (레이블, 값) 형태로 KPI 카드처럼 표시 (변화량 delta는 옵션)

col1.metric("총 매출", f"{filtered['매출'].sum():,}원")
col2.metric("평균 매출", f"{filtered['매출'].mean():,.0f}원")
col3.metric("평균 객단가", f"{filtered['객단가'].mean():,.0f}원")
col4.metric("총 손님수", f"{filtered['손님수'].sum():,}명")

st.divider()  # 구분선

# =====================================================================================
# 차트 탭
# =====================================================================================

tab1, tab2, tab3 = st.tabs(["📈 매출 추이", "🛒 상품별 분석", "📋 데이터"])

with tab1:
    fig1 = px.line(
        filtered,
        x="날짜",
        y="매출",
        title="일별 매출 추이",
        color_discrete_sequence=[BRAND_COLORS[0]],
    )
    fig1.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(color="#007A5E"),
    )
    st.plotly_chart(fig1, use_container_width=True)  # 화면 너비에 맞춤

with tab2:
    fig2 = px.bar(
        filtered.groupby("상품")["매출"].sum().reset_index(),
        x="상품",
        y="매출",
        title="상품 카테고리별 총 매출",
        color="상품",
        color_discrete_sequence=BRAND_COLORS,
    )
    fig2.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(color="#007A5E"),
    )
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    st.dataframe(filtered, use_container_width=True)

# =====================================================================================
# 사용 가이드
# =====================================================================================
with st.expander("ℹ️ 가이드"):  # 접고 펴기
    st.write(
        """
    **사용법:**
    1. 왼쪽 사이드바에서 필터 설정
    2. '필터 적용 🔄' 버튼 클릭
    3. 탭을 이동하며 데이터 확인
    
    **상품 카테고리:**
    - 도시락: 김밥, 삼각김밥, 도시락
    - 음료: 음료수, 커피
    - 과자: 과자, 아이스크림
    - 생활용품: 휴지, 세제 등
    
    **분석 기간:**
    - 2025년 12월 1일 ~ 2026년 1월 15일
    - 연말-연초 매출 비교 분석
    """
    )
