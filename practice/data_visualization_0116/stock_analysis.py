import pandas as pd
import matplotlib.pyplot as plt
import FinanceDataReader as fdr  # 한국 주식데이터 가져오기

# python -m pip install finance-datareader

# 네이버(주식코드 : 035420) 데이터 불러오기
df = fdr.DataReader("035420", "2025-01-01")

print(df.head())  # 잘 불러와졌는지 확인
print(df.columns)  # 컬럼 확인
# '[Open', 'High', 'Low', 'Close', 'Volume', 'Change'], dtype='object'
print(len(df))  # 데이터 개수 확인

# ========== 선 그래프 (Line Chart) ==========
plt.figure(figsize=(10, 5))  # 그래프 크기 설정
plt.plot(df.index, df["Close"])  # x축: 날짜, y축: 종가
plt.title("NAVER Daily Stock Price (Last 1 Year)")  # 제목
plt.xlabel("Date")  # x축 label
plt.ylabel("Close Price (KRW)")  # y축 label
plt.grid(True)  # 격자 표시
plt.show()

# ========== 산점도 (Scatter Plot) ==========
plt.figure(figsize=(10, 5))  # 그래프 크기 설정
plt.scatter(df["Volume"], df["Change"], alpha=0.5)  # x축: 거래량, y축: 등락률
plt.xlabel("Volume")  # x축 label
plt.ylabel("Change (%)")  # y축 label
plt.title("Volume vs Price Change")  # 제목
plt.grid(True)  # 격자 표시
plt.show()

# ========== 막대 그래프 (Bar Chart) ==========
df["Month"] = df.index.to_period("M")  # 월 단위로 변환
monthly_avg = df.groupby("Month")["Close"].mean()  # 월별 평균 종가 계산

plt.figure(figsize=(10, 5))  # 그래프 크기 설정
monthly_avg.plot(kind="bar")  # 막대 그래프 그리기
plt.title("Monthly Average Close Price")  # 제목
plt.xlabel("Month")  # x축 label
plt.ylabel("Average Close Price (KRW)")  # y축 label
plt.xticks(rotation=45)  # x축 라벨 45도 회전
plt.tight_layout()  # 레이아웃 자동 조정
plt.show()
