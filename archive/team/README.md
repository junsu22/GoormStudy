# 🧳 여행 상품 구매 예측 ML 파이프라인

> 고객 정보를 바탕으로 여행 상품 구매 여부를 예측하는 머신러닝 파이프라인

---

## 📌 프로젝트 개요

| 항목 | 내용 |
|------|------|
| **목표** | 고객 데이터로 여행 상품 구매 여부(`ProdTaken`) 예측 |
| **데이터** | Travel.csv — 4,888명 × 20개 변수 |
| **출처** | [Kaggle - Holiday Package Purchase Prediction](https://www.kaggle.com/datasets/susant4learning/holiday-package-purchase-prediction) |
| **팀** | 김준수 · 김한별 · 서동열 |

---

## 🗂️ 파일 구성

```
📦 team_2
 ├── travel_pipeline_final.ipynb   # 메인 노트북 (전체 파이프라인)
 ├── travel_pipeline_final.py      # 동일 코드 .py 변환본
 ├── Travel.csv                    # 원본 데이터
 └── README.md
```

---

## 🔄 파이프라인 구성

```
1단계. 패키지 설치 & 데이터 불러오기
2단계. 데이터 살펴보기 (EDA)
3단계. 전처리 및 피처 엔지니어링
4단계. 3가지 모델 학습 & 성능 비교
5단계. 하이퍼파라미터 튜닝
6단계. 혼동행렬 (Confusion Matrix)
7단계. 최종 모델 변수 중요도 분석
8단계. 모델 저장
```

---

## ⚙️ 전처리 전략

| 컬럼 타입 | 결측치 처리 | 변환 |
|-----------|------------|------|
| 숫자형 | 중앙값으로 대체 | StandardScaler 표준화 |
| 범주형 | 최빈값으로 대체 | OneHotEncoder |

**파생변수 추가**
- `TotalVisitors` : 성인 + 동반 어린이 수
- `HighIncome` : 월소득 중앙값 이상 여부 (0/1)

---

## 🤖 사용 모델

| 모델 | 특징 |
|------|------|
| Logistic Regression | 기준선(Baseline) |
| Random Forest | 안정적인 앙상블 |
| **LightGBM** ✅ | 최종 선택 — 빠르고 균형 잡힌 성능 |

> RandomizedSearchCV (3-Fold, ROC-AUC 기준) 로 LightGBM 하이퍼파라미터 튜닝

---

## 📊 평가 지표

`Accuracy` · `Precision` · `Recall` · `F1 Score` · `ROC-AUC`

---

## 🛠️ 사용 기술

```python
pandas / numpy
scikit-learn
lightgbm
plotly
pickle
```

---

## 🚀 실행 방법

```bash
# 1. 필요 패키지 설치
pip install lightgbm plotly

# 2. 노트북 실행
jupyter notebook travel_pipeline_final.ipynb
```

> Google Colab 환경에서도 실행 가능
