import pandas as pd # pandas를 pd라는 별칭으로 불러오다.
import matplotlib.pyplot as plt # pyplot을 plt 라는 별칭으로 불러오다.

# 선 그래프로 일별 주가 추이 시각화 
df = pd.DataFrame({
    # 25.12.31 ~ # 26.01.10
    "Date" : [
        "2025-12-31", "2026-01-01", "2026-01-02", "2026-01-03",
        "2026-01-04", "2026-01-05", "2026-01-06", "2026-01-07",
        "2026-01-08","2026-01-09","2026-01-10"
    ],
    # 변동 값
    "close": [50000,52000,54000,
              53500,52000,55000,
              56100,56500,58000,
              40000,59000]
})

# 날짜형으로 변환 + 정렬 (시계열 필수)
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date") 

# 선 그래프 그리기 
plt.figure(figsize=(10,5)) # 그래프의 크기(가로 , 세로, 인치)
plt.xlabel("Date") # x축 라벨
plt.ylabel("Close Price") # y축 라벨
plt.plot(df["Date"], df["close"]) # 선그래프 (x= 날짜(데이터프레임컬럼), y= 주가) 
plt.xticks(rotation = 45) # 날짜 의 글자 x 축으로 45도 회전 (겹침방지를 위해)
plt.tight_layout() # 레이아웃 자동 정리 기능
plt.show() # 그래프 출력




