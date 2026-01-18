Streamlit-SHAP 을 이용하여 드래거블 대시보드를 만들거야.
게임플레이 로그를 기반으로 승/패를 예측하고 SHAP으로 
왜 이 플레이어가 이겼는지를 설명하는 드래거블 대시보드야 .

컬렴명, 컬럼의 의미 ,데이터 타입순이야. 
이 데이터를 참조해 .
play_time	플레이 시간 (분)	숫자
level	플레이어 레벨	숫자
deaths	사망 횟수	숫자
items	획득 아이템 수	숫자
win 승/패 (1=승, 0=패)  타겟
damage_dealt 딜량   숫자

연습용 데이터를 넣을거야 . 현재 프로토타입이니까.


RandomForestClassifier , XGBoost 도 사용해줬으면 좋곘어(어느 부분에서 어떻게 사용했는지 주석이 필요 해.)


SHAP 에서 꼭 써야 하는 시각화 3종인데, 
1. 전체 설명이 필요해 
(승패에 가장큰 요인은?) : 1등을 자주함/ 레벨, 플레이 시간이 많았다 등..

2.개별플레이어 
(이 플레이어가 이긴 이유는?): 사망이 적었다. 아이템을 많이 확보 했다. 

관련 지식
st.sidebar
st.selectbox
st.columns or draggable component
shap.TreeExplainer
shap.summary_plot
shap.force_plot

패널 구조에 대해 설명 할게. 
Panel 1 – 전체 게임 인사이트
SHAP summary
승/패 비율

Panel 2 – 플레이어 선택
플레이어 ID 선택
예측 결과 (승/패)

Panel 3 – 선택한 플레이어 SHAP
force plot
변수별 기여도

Panel 4 – 게임 지표 시각화
deaths vs win
play_time vs win

최종 : 이걸 드래그해서 재배치 가능하게 ✨