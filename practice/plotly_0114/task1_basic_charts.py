import plotly.express as px
import plotly.graph_objects as go


# ==========================================
# Task 1: 기본 차트 (바, 산점도, 라인)
# ==========================================

# 1. Bar Chart (막대 그래프)
# 월별 판매량 데이터

months = ['1월', '2월', '3월', '4월', '5월', '6월']
sales = [120, 135, 148, 162, 178, 195]

fig_bar = go.Figure()
fig_bar.add_trace(go.Bar(
    x = months, # x축 : 월
    y = sales , # y축 : 판매량
    marker = dict (color = 'steelblue'),    # 막대의 색상
    text = sales,   # 막대위의 숫자
    textposition= 'outside' # 텍스트 위치
))

fig_bar.update_layout(
    title = "월별 제품 판매량" , # 제목
    xaxis_title = "월", # x축 라벨
    yaxis_title = "판매량 (개)", # y축 라벨
    template = "plotly_white",   # 테마
    showlegend = False # 범례를 숨김
)

fig_bar.show()



# scatter plot (산점도로 표현하기)
# 공부시간과 시험점수 관계
study_hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_scores = [45, 55, 62, 68, 75, 78, 85, 88, 92, 95]

fig_scatter = go.Figure()
fig_scatter.add_trace(go.Scatter(
    x = study_hours,    # x축 : 공부시간
    y = test_scores, # y축 시험점수
    mode = 'markers',   # 점으로 표시
    marker = dict(
        size = 12,  #   점 크기 설정
        color = 'yellow',    # 점 색상
        line = dict(width = 1, color = 'darkblue'), # 점테두리
        symbol = "star"
    )
))

fig_scatter.update_layout(
    title = "공부시간과 시험점수의 관계",
    xaxis_title = "공부시간 (시간)",
    yaxis_title = "시험점수 (점)",
    template = "plotly_dark"
    
)

fig_scatter.show()


# 3. line chart (선 그래프)
# 일주일의 기온변화
days = ["월", "화", "수", "목", "금", "토", "일"]
temperature = [12, 14, 15, 18, 19, 21, 20]

fig_line = go.Figure()
fig_line.add_trace(go.Scatter(
    x = days,   # x축 : 요일
    y = temperature,    # y축 : 기온
    mode = 'lines + markers',   # 점과 선으로 표기하기
    line = dict(color = 'coral', width = 3 ),    # 스타일
    marker= dict(size = 10) # 점 크기
))

fig_line.update_layout(
    title = "일주일간 기온 변화",
    xaxis_title = "요일",
    yaxis_title = "기온(°C)",
    template = "plotly_dark"
)

fig_line.show()