from wordcloud import WordCloud  # 워드클라우드 생성 라이브러리
import matplotlib.pyplot as plt

# 텍스트 데이터
text = """
주식 투자 네이버 삼성 LG SK 현대 카카오 NAVER 애플 테슬라 
주가 상승 하락 급등 급락 폭등 폭락 반등 조정 횡보 박스권
거래량 종가 시가 고가 저가 체결 호가 매물 물량 수급
매수 매도 투자자 개인 기관 외국인 세력 작전 수익 손실 
배당 금융 증권 은행 보험 카드 대출 이자 펀드 ETF
코스피 코스닥 나스닥 다우 S&P 닛케이 항셍 상해 유럽
차트 분석 데이터 그래프 캔들 이평선 골든크로스 데드크로스
시장 경제 기업 실적 영업이익 순이익 매출 성장 전망 예측
기술적분석 기본적분석 보조지표 RSI MACD 볼린저밴드 스토캐스틱
단타 스윙 장투 가치투자 성장투자 배당투자 퀀트 알고리즘
공매도 공매수 상한가 하한가 거래정지 관리종목 투자주의
"""


# 워드클라우드 생성
wordcloud = WordCloud(
    font_path="gulim.ttc",  # 한글 폰트 (굴림)
    background_color="white",  # 배경색
    width=800,  # 너비
    height=400,  # 높이
    colormap="rainbow",  # 무지개색으로
).generate(
    text
)  # 텍스트로 워드클라우드 생성

# 그래프 표시
plt.figure(figsize=(10, 5))  # 그래프 크기 설정
plt.imshow(wordcloud)  # 워드클라우드 이미지 표시
plt.axis("off")  # 축 숨기기
plt.title("Word Cloud")  # 제목
plt.show()
