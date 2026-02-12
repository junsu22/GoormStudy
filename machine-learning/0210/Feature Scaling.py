# 라이브러리 호출
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import numpy as np

np.random.seed(42)  # 랜덤시드 난수 고정
X = np.random.rand(100, 3)  # 100개의 데이터 3열
y = 1 + 2 * X[:, 0:1] + 3 * X[:, 1:2] + 4 * X[:, 2:3] + np.random.randn(100, 1)
# 문제주기,노이즈  : 절편 y = 1 + 2*x1 + 3*x2 + 4*x3 + 정답 (100주기)
idx = np.arange(100)  # 인덱스 100개
np.random.shuffle(idx)  # 100개의 인덱스 셔플
X_train, y_train = X[idx[:80]], y[idx[:80]]
# 훈련용 데이터 80 이전 인덱스 , 검증용 인덱스 80 이후의 인덱스
X_val, y_val = X[idx[80:]], y[idx[80:]]  # 검증용 데이터 생성


"""
스케일링의 전후를 비교하기 위해 출력하는 부분
mean(axis=0) 각 열 특성별 평균
std(axis=0) 각열 특성별 표준편차
axis=0  행 방향 세로로 계산한다는 뜻
"""
# 출력
print("스케일링 전:")  #
print(f"Train 평균: {X_train.mean(axis=0)}")  # 각 특성별 평균
print(f"Train 표준편차: {X_train.std(axis=0)}")  #  각 특성별 표준편차

scaler = StandardScaler()  # 표준화 도구 생성.(평균0, 분산1 변환)
X_train_scaled = scaler.fit_transform(X_train)  # 학습데이터로 평균 / 분산 계산 + 변환
X_val_scaled = scaler.transform(X_val)  # 같은기준으로 검증 데이터  변환
# fit_transform : 기준계산 + 변환 (학습데이터만 )
# transform : 변환만 (검증데이터 )
# 검증에 fit 쓰면 데이터 누수 생김

print("\n스케일링 후:")
print(f"Train 평균: {X_train_scaled.mean(axis=0).round(4)}")
print(f"Train 표준편차: {X_train_scaled.std(axis=0).round(4)}")


"""
<출력>
스케일링 전:
Train 평균: [0.48350466 0.52353709 0.4821311 ]
Train 표준편차: [0.29197639 0.31007235 0.2963168 ]

스케일링 후:
Train 평균: [-0. -0.  0.]
Train 표준편차: [1. 1. 1.]
"""
