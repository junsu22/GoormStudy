# 라이브러리 호출
import numpy as np

np.random.seed(42)  # 난수 시드 고정
X = np.random.rand(100, 3)  # 100개의 데이터를 3개의 열로
y = 1 + 2 * X[:, 0:1] + 3 * X[:, 1:2] + 4 * X[:, 2:3] + np.random.randn(100, 1)
# 문제를 준다. y = 1 절편 + 2 3* X+ 2 + 4*3 + 노이즈 / 정답데이터 a= 1 , b =[2,3 ,4]
idx = np.arange(100)  # 100개의 데이터를
np.random.shuffle(idx)  # 랜덤으로 셔플하고
train_idx = idx[:80]  # 80 이전 의 인덱스들을 학습용으로 나누고
val_idx = idx[80:]  # 80 이후의 인덱스들을 검증용으로 나눈다.


# 데이터생성
# 학습용 데이터 생성
X_train, y_train = X[train_idx], y[train_idx]
# 검증용 데이터 생성
X_val, y_val = X[val_idx], y[val_idx]

a = np.random.randn(1)  # 절편을 초기화한다.
b = np.random.randn(3, 1)  # 기울기를 초기화한다. (특성 3개 , 단변량과 다른점임)

lr = 1e-1
n_epochs = 1000  # 학습횟수 반복
"""
@ 행렬곱 (matrix multiplication): 파이썬 3.5 ~ 이후 부터 지원
np.dot() 과 같은 의미
특성이 여러개면 *로 못곱하기 때문에 @행렬곱을 사용
------------------------------------
단변량:  숫자 * 숫자  /(1, ) * (80, 1)
yhat = a + b * X

다변량 : 행렬 @ 행렬 / (80, 3) @ (3, 1) = (80, 1)
yhat = a + X_train @ b 
----------------------------------------
같은표현들
X_train @ b
np.dot(X_train, b)
X_train.dot(b)
"""

# gradient descent 기울기 , 경사하강법
for epoch in range(n_epochs):
    yhat = a + X_train @ b  # 예측 (단변량 : b *x -> 다변량 : X@b 행렬곱)
    error = y_train - yhat  # 오차
    loss = (error**2).mean()  # MSE ,손실함수 최소화 과정 ,
    a_grad = -2 * error.mean()  # a 기울기  grad : 미분 후 어느방향으로 얼마나 움직일지
    b_grad = -2 * (X_train.T @ error) / len(X_train)  # b 기울기 (행렬 전치 곱)
    a = a - lr * a_grad  # a 업데이트
    b = b - lr * b_grad  # b 업데이트

print(f"a = {a[0]:.4f}")  # 소수점 4째자리까지 호출
print(f"b = {b.flatten()}")  # flatten 보기편하게 배열을 1차원 으로 펼친다.

from sklearn.linear_model import LinearRegression  # 선형회귀

linr = LinearRegression()  # 선형회귀 메서드 호출
linr.fit(X_train, y_train)  # 학습
print(f"sklearn: a={linr.intercept_[0]:.4f}, b={linr.coef_[0]}")
# linr.intercept_ sklearn 이 구한 절편 (=a) , linr.coef  sklearn 이 구한 기울기(=b)
# 위에서 for 문 구현으로 직접 구한 a, b (내가 구한 결과)
# sklearn 이 자동으로 구현한 intercept_,coef = 라이브러리 결과

# 둘이 같으면 현재 내가 짠 경사하강법 코드가 맞아.
# 이것을 sanity check (정상확인) 이라고 함

# 왜 기준이 저녀석? 사이킷런이 구한 intercept_,coef_는 검증된 라이브러리의 결과


"""
<출력>
a = 0.8264
b = [2.31713856 2.87003804 4.3782875 ]
sklearn: a=0.8261, b=[2.31737047 2.87017668 4.37852316]
"""
