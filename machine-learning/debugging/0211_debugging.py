# 라이브러리 불러오기
import numpy as np  # 숫자계산
import torch  # 파이토치 라이브러리
import torch.nn as nn  # 모델만들기
import torch.optim as optim  # 학습 최적화
import matplotlib.pyplot as plt  # 그래프 그리기


# 로지스틱 회귀 클래스 정의
class LogisticRegressionPytorch(nn.Module):
    def __init__(self, input_dim):
        # 부모 클래스 (nn.module)초기화
        super(LogisticRegressionPytorch, self).__init__()
        # 선형 레이어 생성 : input_dim > 1개 출력 (이진분류)
        self.linear = nn.Linear(input_dim, 1)  # 입력 한개

    def forward(self, x):  # fowrard 함수추가
        # forward: 순전파 함수: x를 받아 선형 변환 수행
        return self.linear(x)


# 데이터 준비
np.random.seed(42)  # 난수.랜덤값변동업시
X = np.random.randn(100, 2)  # 100개의 샘플과2개의 특성을 가진

y = (X[:, 0] + X[:, 1] > 0).astype(float).reshape(-1, 1)

# numpy -> Tensor 변환
X_tensor = torch.FloatTensor(X)
y_tensor = torch.FloatTensor(y)

# 모델생성
model = LogisticRegressionPytorch(input_dim=2)

# 손실함수 & 옵티마이저
crioterion = nn.BCEWithLogitsLoss()  # 시그모이드 + BCE 합쳐진 버젼
optimizer = optim.SGD(model.parametes(), lr=0.1)

# 학습
losses = []
epochs = 1000  # 횟수

for epoch in range(epochs):
    outputs = model(X_tensor)
    loss = crioterion(outputs, y_tensor)


# 역전파
optimizer.zero_grad()  # 그래디언트 초기화
loss.backward()  # 역전파
optimizer.step()  # 가중치 업데이트

losses.append(loss.item())

if (epoch + 1) % 100 == 0:
    print(f"Epoch [{epoch + 1} / {epochs}], Loss: {loss.item():.4f}")
    # 소숫점 4째번까지

# 예측
with torch.no_grad():  # 그래디언트 계산 비활성
    predictions = torch.sigmoid(model(X_tensor))  # 시그모이드 함수 적용해서 0~ 1 확률로
    predicted_classes = (predictions >= 0.5).float()
    accuracy = (predicted_classes == y_tensor).sum() / len(y_tensor)
    print(f"\n정확도 : {accuracy : .2% }")  # 소수둘쨰 까지


# 손실그래프

plt.plot(losses)
plt.xlabel("Epoch")  # x축 레이블
plt.ylabel("Loss")  # y축 레이블
plt.title("Traninig Loss")  # 제목
plt.show()  # 화면표시


# Logistic Regression에 대해 이해하고, 전체 진행과정을 실습하고 설명하세요 (Line-by-Line으로)
# 다변량 선형회귀분석에 대해 이해하고, 전체 진행과정을 실습하고 설명하세요 (Line-by-Line으로)
# Gradient Descent를 명확히 구현하기 위한 Feature Scaling 기법을 조사하고 분석하세요
