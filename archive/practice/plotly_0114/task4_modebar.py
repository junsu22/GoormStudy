import plotly.express as px

# ==========================================
# Task 4: 모드바 생성 및 조정
# ==========================================

# 제품 카테고리별 판매 데이터
categories = ['전자제품', '의류', '식품', '가구', '도서', '완구']
sales_amount = [4500, 3200, 2800, 3900, 1500, 2100]

#막대 그래프 생성
fig = px.bar(
    x = categories,
    y = sales_amount,
    title= '카테고리별 판매액',
    labels={'x': '카테고리', 'y':'판매액 (만원)'}
)

fig.update_traces(marker_color = 'royalblue')   #막대 색상 설정
fig.update_layout(template = 'plotly_white') #레이아웃

# 모드바
fig.show(config ={
    'displaylogo' : False,
    'displayModeBar': True,  # 이 줄 추가 (항상 표시)
    'modeBarButtonsToRemove':[  # 제거할 버튼
        'select2d',
        'lasso2d'
    ],
    'modeBarButtonsToAdd':[     # 추가할 기능 버튼들
        'drawline',     # 선 그리기
        'drawrect',      #사격형그리기
        'eraseshape'    #지우개
    ],
    'toImageButtonOptions':{    # 파일다운로드 설정
        'format':'png',         # Png 형식
        'filename' : 'sales_chart', # 파일이름
        'width': 1200,              #너비
        'height': 800,              #높이   
        'scale': 2                 #해상도 (1~4,2400 x 1600 픽셀)
    }
})
