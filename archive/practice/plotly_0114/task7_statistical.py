import plotly.graph_objects as go
import numpy as np

# ==========================================
# Task 7: 통계용 차트
# ==========================================

# 3개 그룹의 시험 점수 데이터
np.random.seed(42)  # seed 42 
# 컴퓨터는 랜덤을 만들지 못함. 랜덤으로 보이는 숫자.
# 42는 관습적으로 사용하는 숫자.(의미없음) 

group_a = np.random.normal(75, 10, 50)  # 평균 75, 표준편차 10
group_b = np.random.normal(80, 8, 50)   # 평균 80, 표준편차 8
group_c = np.random.normal(70, 12, 50)  # 평균 70, 표준편차 12

# box plot 생성
fig = go.Figure()

# 반 색상 구분 
# A반 > 파란색
# B반 > 녹색
# C반 > 빨간색


# A반
fig.add_trace(go.Box(
    y = group_a,
    name = 'A반',
    marker_color = 'lightBlue',
    boxmean = 'sd'  # 평균과 표준변차 표시
))

# B반
fig.add_trace(go.Box(
    y = group_b,
    name = 'B반',
    marker_color = 'lightGreen',
    boxmean='sd'
))

# C반
fig.add_trace(go.Box(
    y = group_c,
    name = 'C반',
    marker_color = 'lightcoral',
    boxmean='sd'
))

# 레이아웃
fig.update_layout(
    title = '반 별 시험 점수 분포도',
    yaxis_title = '점수',
    template = 'plotly_dark',
    showlegend =True
)

fig.show()