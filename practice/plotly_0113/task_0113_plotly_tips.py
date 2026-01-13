import plotly.express as px
import plotly.io as pio

# 배운내용을 토대로 plotly 문법 실습 

# ==============================
# Pandas Plotly Backend 설정을 해주세요.
# ==============================

# 백앤드 설정 (renderer)
pio.renderers.default = "browser" # IDE 가 아닌 웹 브라우저 로 띄워줘
# plotly Express 에 내장된 예제 로드
df = px.data.tips() 

# 데이터 로드 확인 (상위 5행 출력)
print(df.head())
'''
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
'''


# ==============================
# 최소 2개의 템플릿을 사용하여 그래프를 그려주세요.
# Plotly 그래프를 여러개로 나누거나 겹쳐 생성해주세요. (그래프 A, B)
# ==============================

# (그래프 A) Scatter : total_bill vs tip / 그룹 : day
# 요일에 따른 총 결제 금액과 팁의 관계 / 산점도 시각화
x_main = "total_bill"
y_main = "tip"
group_a = "day" 

fig_a = px.scatter(
    df,
    x = x_main,
    y = y_main,
    color=group_a,
    title="Tips Scatter : Total Bill vs Tip (by Day)"
)
# 다크한 템플릿 적용
fig_a.update_layout(template = "plotly_dark")

# (그래프 B)히스토그램
# total_bill 분포 / 그룹 : day
# 동일한 기준. 총 결제 금액의 분포를 히스토그램으로 비교

x_sub = "total_bill" # 콤마를 넣어서 튜플이 될뻔함.
# group_b (히스토그램)에는 y축을 지정하지 않는다.
group_b = "day"
fig_b = px.histogram(
    df,
    x = x_sub,
    color= group_b,
    barmode = "overlay",    # 겹치기
    title = "Tips Histogram : Total Bill Distribution (by Day)"
)

fig_b.update_layout(template = "ggplot2")

# 그래프 출력
# 이미 출력이 되어 아래 출력 변화를 확인하기 어려워 주석처리
# fig_a.show() 
# fig_b.show()

# 검은배경에 알록달록한 산점도가 나왔다

# ==============================
# Plotly 그래프의 범례를 설정하고 조정해주세요.
# ==============================

# 그래프 A 범례 : 아래 가로형(바깥)
fig_a.update_layout(
    legend= dict(
        title = "Day",
        orientation = "h",
        x = 0.5,
        # x = 0.01,(변화 확인용)    
        y = -0.25,
        # y = 1.2(변화 확인용)
        xanchor = "center",
        # xanchor="left",
        yanchor = "top",
        bgcolor = "rgba(0, 0, 0, 0.4)",
        bordercolor = "rgba(255, 255, 255, 0.4)",
        borderwidth = 1
        
    )
)


# 그래프 B 범례: 오른쪽 바깥
fig_b.update_layout(
    legend =dict(
        title = "Day",
        x = 1.02,
        y = 1,
        xanchor = "left",
        yanchor = "top"
    )
)



# ==============================
# Plotly 그래프를 생성하여, 축과 그리드 관련 설정을 해주세요.
# ==============================

# 그래프 A : 축  / 그리드 설정
# (다크 템플릿이라 그리드는 은은하게 보이도록 색 조정)
fig_a.update_xaxes(showgrid=True, showline=True, mirror=True, gridwidth=1,
                   gridcolor="rgba(255,255,255,0.15)")
fig_a.update_yaxes(showgrid=True, showline=True, mirror=True, gridwidth=1,
                   gridcolor="rgba(255,255,255,0.15)")
# 그래프 B : 축 / 그리드 설정
fig_b.update_xaxes(showgrid = True, showline = True, mirror = True, gridwidth = 1)
fig_b.update_yaxes(showgrid = True, showline = True, mirror = True, gridwidth = 1)


fig_a.show() # 확인 후 출력은 아래로 내려야 변경되는 부분이 확인 가능함
fig_b.show()

