import plotly.graph_objects as go
import numpy as np

# ==========================================
# Task 8: 과학용 차트
# ==========================================

# 실험 데이터: 온도에 따른 화학 반응 속도
temperature = np.array([20, 30, 40, 50, 60, 70, 80])
reaction_rate = np.array([2.3, 4.1, 7.8, 14.2, 25.1, 43.5, 72.8])
error = np.array([0.3, 0.5, 0.8, 1.2, 2.1, 3.5, 5.8])

fig = go.Figure()

fig.add_trace(go.Scatter(
    x = temperature,
    y = reaction_rate,
    mode = 'markers',
    name = '실험 데이터',
    marker = dict(
        size = 10,
        color = 'darkblue',
        line = dict(width = 2, color = 'white')
    ),
    error_y = dict(
        type = 'data',
        array = error,
        visible = True,
        color = 'rgba(0, 0, 139, 0.5)', 
        thickness = 2, 
        width = 4
    )
))

# 용어정리
# 지수 함수 (x가 커질수록 y가 급격히 증가 (또는 감소))
# y = a * e^(bx)
# 예시 : x = 0  →  y = 0.5 * e^0 = 0.5
# 피팅파라미터
# 실제 데이터를 곡선에 맞출 때 조절하는 값들

# 지수 함수 피팅
# a, b = 0.5, 0.06  # a: 초기값, b: 증가율

# 추세선 (지수함수 피팅)
temp_fit = np.linspace(20, 80, 100)
a, b = 0.2, 0.085
rate_fit = a * np.exp(b * temp_fit)

fig.add_trace(go.Scatter(
    x = temp_fit,
    y = rate_fit,
    mode = 'lines',
    name = '이론 모델',
    line = dict(
        color = 'red',
        width = 2,
        dash = 'dash'
    )
))

fig.update_layout(
    title = "온도에 따른 화학 반응 속도 (오차 막대 포함)",
    xaxis = dict(
        title = '온도(°C)',
        showgrid = True,
        gridcolor = 'lightgray',
        zeroline = False
    ),
    yaxis = dict(
        title = "반응속도",
        showgrid = True,
        gridcolor = 'darkblue',
        zeroline = False,
        type = 'log'
    ),
    template = 'plotly_white',
    hovermode = 'closest',
    legend = dict(
        x = 0.02,
        y = 0.98,
        bgcolor = 'rgba(255, 255, 255, 0.8)',
        bordercolor = 'gray',
        borderwidth = 1
    )
)

fig.add_annotation(
    x = 60,
    y = 25.1,
    text = "최적 반응 온도",
    showarrow = True,
    arrowhead = 2,
    arrowcolor = 'purple',
    arrowwidth = 2,
    bgcolor = 'yellow',
    bordercolor = 'orange',
    borderwidth = 2,
    font = dict(size = 12, color = 'black')
)

fig.show()