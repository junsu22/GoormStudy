import plotly.graph_objects as go

# ==========================================
# Task 5: 드롭다운 메뉴 생성 및 튜닝
# ==========================================

# 월별 고객 방문 데이터
months = ['1월', '2월', '3월', '4월', '5월', '6월']
online = [450, 520, 480, 610, 580, 650]    # 온라인 방문
offline = [320, 380, 340, 420, 460, 490]   # 오프라인 방문
total = [770, 900, 820, 1030, 1040, 1140]  # 전체

# Figure 생성
fig = go.Figure()

# 온라인 방문
fig.add_trace(go.Scatter(
    x = months,
    y = online,
    mode = 'lines + markers',
    name = '온라인',
    line = dict(color = 'blue', width = 3)
))

# 오프라인 방문
fig.add_trace(go.Scatter(
    x = months,
    y = offline,
    mode = 'lines + markers',
    name = '오프라인',
    line = dict(color = 'red', width = 3 )
))

# 전체 방문
fig.add_trace(go.Scatter(
    x = months,
    y = total,
    mode = 'lines + markers',
    name = '전체',
    line = dict(color = 'green', width = 3)
))

# 드롭다운 메뉴 추가
fig.update_layout(
    updatemenus = [
        dict(
            type = 'dropdown',
            direction = 'down',
            buttons = [
                dict(
                    label = '온라인',
                    method = 'update',
                    args = [{'visible': [True, False, False]}]
                    ),
                dict(
                    label = '오프라인',
                    method = 'update',
                    args = [{'visible': [False, True, False]}]
                ),
                dict(
                    label = '전체비교',
                    method = 'update',
                    args = [{'visible': [True, True, True]}]
                )
            ],
            x = 1.15,   # 위치
            y = 1,
            xanchor = 'left',
            yanchor = 'top'
        )
    ],
    title = '월별 고객 방문 현황 (드롭다운 선택)',
    xaxis_title = '월',
    yaxis_title = '방문자 수 (명)',
    template = 'plotly_white'
)

fig.show()