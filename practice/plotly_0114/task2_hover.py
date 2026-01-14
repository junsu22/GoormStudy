import plotly.express as px
import plotly.graph_objects as go

# ==========================================
# Task 2: 마우스 오버 (Hover) 정보 출력
# ==========================================

# 지역별 매출 데이터
regions = ['서울','부산','대구','인천','광주','대전']
revenue = [850, 520, 380, 450, 320, 410]
growth_rate = [12.5, 8.3, 5.2, 9.1, 7.4, 6.8]

# 막대그래프 생성
fig = go.Figure()

fig.add_trace(go.Bar(
    x = regions,
    y = revenue,
    marker= dict (color = 'teal'),
    
    hovertemplate = '<b>%{x}</b><br>' + # 지역 (굵게) 
                    '매출: %{y}억원<br>' + # 매출
                    '성장률 : %{customdata}%<br>'+ # 성장률 
                    '<extra></extra>',  # 추가 정보 제거
                    
    customdata = growth_rate #  커스텀 데이터 (성장률)
))


# 레이아웃 
fig.update_layout(
    title = '지역별 매출 현황 (마우스 오버로 상세 정보를 확인)',
    xaxis_title = '지역',
    yaxis_title = '매출 (억원)',
    hovermode = 'x', # x축을 기준으로 hover
    template = 'plotly_dark'
)

# spike 라인 추가 (커서선)
fig.update_xaxes(
    showspikes = True,  # spike 활성화
    spikecolor = 'green',   
    spikethickness = 2, # 두께  
    spikedash = 'dot'   # 점선 스타일
)

fig.update_yaxes(
    showspikes=True,
    spikecolor='red',
    spikethickness=2,
    spikedash='dot'
)

fig.show()