import plotly.graph_objects as go

# ==========================================
# Task 3: 버튼 생성 및 튜닝
# ==========================================

# 분기별 실적 데이터
quarters = ['1분기', '2분기', '3분기', '4분기']
profit = [230, 280, 310, 350]
cost = [180, 200, 220, 240]

# Figure 생성
fig = go.Figure()

# 수익 데이터
fig.add_trace(go.Bar(
    x = quarters,   # x = 분기
    y = profit,     # y = 수익
    name = '수익',
    marker = dict(color = 'coral')
))

# 비용 데이터
fig.add_trace(go.Bar(
    x = quarters,
    y = cost,
    name = '비용',
    marker = dict(color = 'lightBlue')
))



# 버튼 추가
fig.update_layout(
    updatemenus=[
        dict(
            type='buttons',  # 버튼 타입
            direction ='left',  # 배치의 방향임 , 왼쪽으로 옮기고 싶으면 xanchor에서 
            buttons = [
                # 버튼 1: 수익만 보기
                dict(
                    label='수익',
                    method='update',
                    args=[{'visible': [True, False]}]  # 첫 번째만 보임
                ),
                # 버튼 2: 비용만 보기
                dict(
                    label='비용',
                    method='update',
                    args=[{'visible': [False, True]}]  # 두 번째만 보임
                ),
                # 버튼 3: 전체 보기
                dict(
                    label='전체',
                    method='update',
                    args=[{'visible': [True, True]}]  # 둘 다 보임
                )
            ],
            pad={'r': 10, 't': 10},  # 버튼 패딩
            x=0,  # x 위치 , 0 왼쪽 / 0,5 중앙
            # y=1.15,  # y 위치
            y = 1.25,   # 글씨가 겹쳐 타이틀을 y축으로 여백을 더 주어 타이틀 내림
            xanchor='left',
            yanchor='top'
        )
    ],
    title='분기별 수익/비용 (버튼으로 선택)',
    xaxis_title='분기',
    yaxis_title='금액 (백만원)',
    template='plotly_white',
    barmode='group'  # 막대 그룹화
)

fig.show()