# 라이브러리 불러오기
import numpy as np  # 숫자 계산
import torch  # 파이토치 라이브러리
import torch.nn as nn  # 모델 만들기
import torch.optim as optim  # 학습 최적화
import matplotlib.pyplot as plt  # 그래프 그리기


# 로지스틱 회귀 클래스 정의
class LogisticRegression(nn.Module):
    def __init__(self, input_dim):
        # 부모 클래스(nn.Module) 초기화
        super(LogisticRegression, self).__init__()
        # 선형 레이어 생성: input_dim개 입력 -> 1개 출력 (이진분류)
        self.linear = nn.Linear(input_dim, 1)

    def forward(self, x):
        # 순전파 함수: 입력 x를 받아서 선형 변환 수행
        return self.linear(x)


# 데이터 준비
# 랜덤 시드 난수 고정
np.random.seed(42)
# 100개 샘플, 2개 특성을 가진 랜덤 데이터 생성
X = np.random.randn(100, 2)
# 레이블(정답) 만들기: 두 특성의 합이 0보다 크면 1, 아니면 0
# 인위적으로 분류 문제를 만드는 것
y = (X[:, 0] + X[:, 1] > 0).astype(float).reshape(-1, 1)
# ====================================================
# Numpy -> PyTorch Tensor 변환
# Numpy 는 Pytorch 에 바로 넣을 수 가 없다.
# 변환이유 : 1.자동 미분 (Autograd) : Numpy는 자동미분을 못하기 때문에 Pytorch, 역전파를 못하기 때문에 tensor 여야 함.
#           2. GPU 사용가능 : x_np.cuda() 불가능, cpu를 사용함. pytorch는 GPU 로 옮길 수있다.
#              이게 무슨 문제? 딥러닝은 GPU가 필수이다. Numpy는 GPU를 못쓴다.
X_tensor = torch.FloatTensor(X)
y_tensor = torch.FloatTensor(y)

# ==================== 모델 생성 ====================
model = LogisticRegression(input_dim=2)  # 특성 2개

# ==================== 손실함수 & 옵티마이저 ====================
criterion = nn.BCEWithLogitsLoss()
# criterion :모델이 얼마나 틀렸는지 확인 하는 녀석. (채점기)/ nn : 뉴럴네트워크(신경망) / BCEWithLogitsLoss : 이진함수(0,1)용 손실함수
# 신경망 도구에서 가져온, 0 아니면 1 맞추는 문제의 채점기"
# 합격이냐 불합격이냐 예측 한다고 생각
optimizer = optim.SGD(model.parameters(), lr=0.1)
# optimizer : 수리공 / optim.SGD : 공구상자 / model.parameters() : 고칠 부품들 / lr=0.1 : 수리 속도
# 손실을 줄이기 위해 모델 가중치를 업데이트 하는 도구
# ==================== 학습 ====================
losses = []  # 손실을 기록 (매 epochs 마다 손실값 저장)
epochs = 1000  # 학습 반복 횟수

for epoch in range(epochs):  # 반복변수, epochs 수만큼 반복 [0...999]
    # 순전파 (FowardPass) : 입력데이터가 모델을 통과해서 나오는 과정 , 앞으로 진행
    outputs = model(X_tensor)  # outputs : 예측값, 모델,(입력 데이터 X_tensor)
    loss = criterion(outputs, y_tensor)  # 오류 = 채점기(예측값, 정답 데이터 y_tensor)

    #  역전파 (BackwardPass) : 손실을 줄이기 위해 가중치를 어떻게 수정해야 하는지 계산 , 뒤로진행
    optimizer.zero_grad()  # 그래디언트 초기화
    loss.backward()  # 역전파
    optimizer.step()  # 가중치 업데이트

    # 손실 기록
    losses.append(loss.item())
    # 현재 손실값을 리스트에 기록한다. item() : 숫자로 변환한다.

    # 100번째 epoch마다 진행상황 출력
    if (epoch + 1) % 100 == 0:
        # epoch는 0 부터 시작하기 때문에 1을 더해줌. 그래야 1번째 가 되니까.
        print(f"Epoch [{epoch + 1}/{epochs}], Loss: {loss.item():.4f}")
        # 현재번호/ 전체횟수 , 손실. 숫자변환(): 소숫점 4째자리까지

# ==================== 예측 및 평가 ====================
with torch.no_grad():  # 그래디언트 계산 비활성화
    predictions = torch.sigmoid(model(X_tensor))
    # 시그모이드 함수 : 모델 예측값을 0 ~ 1 사이 확률로 변환
    predicted_classes = (predictions >= 0.5).float()
    # 최종 분류 : 확률이 50% 이상이라면 1 , 아니라면 0 으로 분류한다.

    # 정확도 계산 (예측이 정답과 맞은 비율)
    accuracy = (predicted_classes == y_tensor).sum() / len(y_tensor)
    # 맞은개수 / 전체개수   = 정확도
    print(f"\n정확도: {accuracy:.2%}")  # 퍼센트로 출력 . 소수점 둘째자리 까지

# ==================== 손실 그래프 ====================
plt.plot(losses)  # 손실값을 선 그래프로
plt.xlabel("Epoch")  # x축 레이블 이름설정
plt.ylabel("Loss")  # y축 레이블 이름설정
plt.title("Training Loss")  # 그래프 제목
plt.grid(True, alpha=0.3)  # 그리드 추가 , 투명도 30%
plt.show()  # 화면 표시



'''
Epoch [100/1000], Loss: 0.2535
Epoch [200/1000], Loss: 0.2007
Epoch [300/1000], Loss: 0.1743
Epoch [400/1000], Loss: 0.1575
Epoch [500/1000], Loss: 0.1456
Epoch [600/1000], Loss: 0.1365
Epoch [700/1000], Loss: 0.1292
Epoch [800/1000], Loss: 0.1232
Epoch [900/1000], Loss: 0.1182
Epoch [1000/1000], Loss: 0.1138

정확도: 99.00%

'''


