# polynomial Regression (다항회귀)

# 라이브러리 불러오기
import numpy as np  # 숫자계산
import torch  # 파이토치 라이브러리
import torch.nn as nn  # 모델만들기
import torch.optim as optim  # 학습 최적화

# 1. 훈련 시킬 데이터 생성
np.random.seed(42)  # 난수 , 랜덤숫자고정
X = np.random.rand(100, 1).astype(np.float32)
# 100개행 1개 열 , float32 : float64의 절반. 속도 빠르고 메모리를 적게 씀. 최적화
y = (4 * X**3 + 2 * X**2 + X).astype(np.float32)  # 정답값 (y = 4x³ + 2x² + x)

#   2. Polynomial 변환: x → x , x^2, x^3
# np.concatenate = 사슬로 이은다.   axis (축_방향 0 : 아래로 붙임. 1 좌 우로 붙임.)
X_poly = np.concatenate([X**1, X**2, X**3], axis=1)
# x를 옆으로 복사해서 x , x^2, x^3  옆으로 붙이기


# 3. Tensor 변환
X_t = torch.FloatTensor(X_poly)
# Numpy → PyTorch Tensor로 변환 (32비트 실수형)
y_t = torch.FloatTensor(y)

# 4. 모델 설정
model = nn.Linear(3, 1)  # 입력 3개  (x, x^2, x^3) => 출력 1개
# y = W1 * x + w2 * x^2 + w3*x^3 + b
loss_fn = nn.MSELoss()  # 손실함수 : 예측값과 정답의 차이를 계산 , MSE (평균제곱오차)
optimizer = optim.Adam(model.parameters(), lr=0.01)
# 최적화 도구./ Adam 경사하강법 업글버전 / lr = 0.01 학습률 (한번에 얼마나 바꿀까?)

# 5. 훈련
print("훈련 시작")
for epoch in range(100):  # 100번 반복
    # 예측
    y_pred = model(X_t)  # 모델에 X_t, 라는 데이터를 넣어서 예측 값을 계산한다.
    # 예측을 해야하기 때문에 정답(y_t)을 주면 안된다!
    loss = loss_fn(y_pred, y_t)
    # 예측값 , 정답 얼마나 틀렸는지 비교(검증이 아닌 훈련 중 손실 계산)

    # 업데이트
    optimizer.zero_grad()  # 이전 기울기를 초기화 (안하면 쌓이게 됨 )
    loss.backward()  #  손실 줄이려면 파라미터를 어떻게 바꿔야 할지 계산(손실이 줄어드는 방향 찾기)
    optimizer.step()  # 찾은 방향으로 파라미터를 조금씩 이동시킴, 재배치

    # 진행상황 출력
    if (epoch + 1) % 20 == 0:  # 20으로 나눈 나머지가 0이면
        print(f"Epoch {epoch+1}/100 - Loss: {loss.item():.4f}")
        # loss.item(): Tensor에서 숫자만 꺼냄 / .4f: 소수점 4자리

print("훈련 완료")

# 훈련 시작
# Epoch 20/100 - Loss: 5.4131
# Epoch 40/100 - Loss: 3.8862
# Epoch 60/100 - Loss: 2.7970
# Epoch 80/100 - Loss: 2.0616
# Epoch 100/100 - Loss: 1.5835
# 훈련 완료

# 여러번 반복(Epoch값이 커질수록)이 될수록 로스가 줄어드는 것을 확인할 수 있었다.
