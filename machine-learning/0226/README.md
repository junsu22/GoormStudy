# Credit Prediction ML Pipeline

신용등급 데이터를 활용하여 
데이터 분석부터 모델링까지 전체 머신러닝 파이프라인을 구현한 프로젝트입니다.

EDA(탐색적 데이터 분석), Feature Engineering, 모델 학습 및 평가 과정을 통해 다양한 머신러닝 모델의 성능을 비교하고 최종적으로 Voting Ensemble을 적용하여 모델 성능을 평가했습니다.

---

# 프로젝트 목표

- 데이터 분석 전체 흐름 경험 (EDA → Feature Engineering → 모델링 → 평가)
- 데이터 전처리 및 변수 생성 과정 이해
- 여러 머신러닝 모델 성능 비교
- Ensemble 기법(Voting)을 활용한 성능 개선 실험

---

# 사용 기술

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost

---

# 데이터 전처리

다음과 같은 전처리 과정을 수행했습니다.

- 결측치 처리  
- 범주형 변수 Label Encoding
- 이상치 처리
- 날짜 데이터 변환
- 로그 변환을 통한 데이터 분포 안정화

```python
np.log(train["income_total"])
np.log(train["DAYS_EMPLOYED"])
