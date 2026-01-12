

# 라이브러리 불러오기
import plotly.express as px # 빠르게 기본 그래프를 그릴때 편리
import plotly.graph_objects as go # 세부적인 사항을 건드릴때 

# ==============================
# STEP 1. 기본 산점도 + trace 추가
# ==============================


df = px.data.iris() # 붓꽃데이터


# plotly 기본 그래프 만들기 (px)

# scatter 그리기
fig = px.scatter(
    df,
    x = 'sepal_width',
    y = 'sepal_length',
    color= 'species',
    title = "Iris Scatter - Base"
)

fig.show()


# add_trace 실습

mean_df =df.groupby("species", as_index = False)[
    ["sepal_width", "sepal_length"]
].mean()

fig.add_trace(
    go.Scatter(# 클래스 명 대문자 필수
        x = mean_df["sepal_width"],
        y = mean_df["sepal_length"],
        mode = "markers",
        name = "species mean",
        marker = dict(size = 16, symbol = "x")
        # (symbol 찾아보니 마름모 x자 등 모양이 다양했다.)
    )
)
fig.show()

# 디버깅 내역 (불러오기 에러 발생)
#     raise ImportError(
# ...<2 lines>...)
    
# > 설치
#  pip install -U plotly
# (설치 처음하는경우 시간이 좀 소요될 수 있음 , uninstall)
    
# > 확인   
# pip install plotly
# 버젼 확인 (설치여부)
# python -c "import plotly; print(plotly.__version__)"

# > 에러
# $ pip install numpy
# Or install Plotly Express and its dependencies directly with:    
# $ pip install "plotly[express]"

# > 설치
# px.data.iris > numpy, pandas 가 필요함 
# pip install numpy
# pip install "plotly[express]"

# > 에러
# ModuleNotFoundError: return_type=pandas, but pandas is not installed
# (pandas가 설치되어있지 않은데 달라고 요청해 발생한 에러), px.data.iris()

# > 설치
# pandas 설치  두개 중 택 1
# pip install pandas
# pip install "plotly[express] # plotly, pandas, numpy 한번에 설치.

# 확인
# python -c "import pandas as pd; print(pd.__version__)"


# 분포도 확인. <정확한 명칭은 산점도>


# ==============================
# STEP 2. Axis 범위 지정 / 삭제 / modify
# ==============================


# 2 axis 범위 지정 / 삭제 / modify 실습

# 축의 범위 지정
fig.update_xaxes(range = [2.0, 4.5])
fig.update_yaxes(range = [4.0, 8.5])
fig.update_layout(title= "Axis range fixed")
fig.show()

# 자동계산을 멈췄고, 받은 범위만 보여줌



# 축 범위 삭제 ( autorange (자동범위)로 복귀)  # outor → autorange
fig.update_xaxes(autorange = True)
fig.update_yaxes(autorange = True)
fig.update_layout(title = "Axis autorange reset")
fig.show()
# axis 범위를 삭제한다는건 값을 삭제하는 것이 아닌 autorange 모드로 돌아감 의미



# axis modify (뒤집기 / 줌 고정)
# y 축 뒤집기
fig.update_yaxes(autorange = "reversed")

# x 축 (슬라이더) 고정
fig.update_xaxes(fixedrange = True)

fig.update_layout(title = "Axis modify: y reversed, x fixed")
fig.show()

# # 디버깅 내역 (메서드 이름 오타)
# line 94, in <module>
#     fig.update_yaxex(range = [4.0, 8.5])
#     ^^^^^^^^^^^^^^^^
# yaxes 오타 남.




# ==============================
# STEP 3-1. update_traces 실습
# ==============================

# update trace를 새로 그리지 않고 ,한번에 수정한다.


# 모든 scatter trace(평균점, species mean)의 스타일을 한번에 수정하는 코드
fig.update_traces(
    marker = dict(
        opacity = 0.6, # 투명도
        line = dict(width =5, color ="red") # 테두리 두께 / 색상
    ),
    selector=dict(type = "scatter")
)

fig.update_layout(title = "update_traces (all scatter)")
fig.show()

# 동그라미 마커(점)들이 빨갛게 나오고, x모양 의 마커에 빨간 줄이 두꺼워짐.
# 약간 투명해짐

# 디버깅내역 (line 은 스타일 구간으로 타입이 올 수 없다.)
# 디버깅: update_yaxex -> update_yaxes 처럼 메서드/키 
# 오타는 바로 에러나거나 적용이 안 됨



# ==============================
# 3-2. 특정 trace만 업데이트 (평균점 강조)
# ==============================

# 평균값 trace만 선택해 강조함 (요약 데이터 시각적 구분)

fig.update_traces(
    marker=dict(
        size = 50,
        opacity = 1.0,
        line = dict(width = 10, color = "Green")
    ),
    selector=dict(name = "species mean")
)

fig.update_layout(title = "highlight species mean only")

fig.show()


# 눈에 확 띄는 크기의 x(symbol) 가 녹색 테두리로 출력되었다.



# ==============================
# STEP 4. 수업 외 Plotly 기능
# hover 마우스를 올리면 내가 원하는 글 추가, 구조 바꾸기
# ==============================

fig.update_traces(
    hovertemplate= (
        "추가 된 한줄<br>"
        "종: %{fullData.name}<br>"  # <br>은 HTML 줄바꿈 태그
        "sepal_width: %{x:.2f}<br>" # 소수점 둘째 까지 출력
        "sepal_length: %{y:.2f}<br>"
        "<extra></extra>"   #  # hover 오른쪽의 trace 이름 박스 숨김
    ),
    selector= dict(type = "scatter")    #scatter(trace) 들에 적용할것.
    
)
fig.update_layout(
    title = "HOVER : 마우스를 올리면 내가 원하는 텍스트 , 구조 출력",
    hovermode = "closest"   # 철자 하나 틀려도 적용이 안됌.
)
fig.show()

# 설명: 마우스를 올리면 내가 넣은 문장과 종 이름이 같이 출력됨
# 설명: hovertemplate으로 출력되는 순서랑 내용을 직접 바꿈


# 디버깅 내역
# - hovermode 오타: "closet" -> "closest"

