import plotly.graph_objects as go
import numpy as np

# ==========================================
# Task 6: 슬라이더 생성 및 튜닝
# ==========================================

# 데이터: 여러 배율의 곡선
x = np.linspace(0, 10, 100)

# Figure 생성
fig = go.Figure()

# 배율별 곡선 추가 (1x, 1.5x, 2x, 2.5x, 3x)
scales = [1, 1.5, 2, 2.5, 3]
for scale in scales:
    fig.add_trace(go.Scatter(
        x = x,
        y = scale * np.exp(-x/5) * np.sin(x),   # 감쇠사인파
        mode = 'lines',
        name = f'{scale} 배',   # f-string
        visible= False  # 처음에 숨길 것.
    ))
    
    
# 첫번째 만 보이게 
fig.data[0].visible = True

# 슬라이더 스텝 만들기
steps = []  # 리스트를 만듬
for i in range(len(scales)):
    step = dict(
        method = 'update',
        args = [
            {'visible': [False] * len(fig.data)},   # 모두 숨기기
            {'title' : f'배율: {scales[i]}배'}  # 제목변경
        ],
        label = f'{scales[i]}x' #슬라이더 라벨  
    )
    step['args'][0]['visible'][i] = True  # i번째 보임
    steps.append(step)
    
    
# 슬라이더 추가
sliders = [dict(
    active = 0, # 시작위치
    currentvalue = {
        'prefix' : '배율 : ',   # 현재 값 표시
        'visible' : True,
        'xanchor': 'center'
    },
    pad = {'t' : 50},   # 위쪽 패딩
    steps = steps
)]

fig.update_layout(
    # updatemenus : 재생 기능 추가 animate 써보기
    updatemenus = [
        dict(
            type = 'buttons',
            showactive = False,
            buttons = [
                dict(label = '재생', method = 'animate',
                     args = [None, {'frame': {'duration' :500}}]),
                dict(label = '정지', method = 'animate',
                     args = [[None], {'frame': {'duration': 0}}])
            ],
            x = 0.1, y = 0
        )
    ],
    sliders = sliders,
    title = "배율 조절 (슬라이더)",
    xaxis_title = 'x',
    yaxis_title = 'y',
    template = 'plotly_white'
)
# 애니메이션 프레임생성 
frames =[]
for i in range(len(scales)):
    frame_data = []
    for j in range(len(scales)):
        frame_data.append(go.Scatter(
            x=x,
            y=scales[j] * np.exp(-x/5) * np.sin(x),
            mode='lines',
            name=f'{scales[j]}배',
            visible=(i == j)    # i번째 배율 표시
        ))
    frames.append(go.Frame(data=frame_data, name = str(i)))
    
fig.frames = frames
fig.show()