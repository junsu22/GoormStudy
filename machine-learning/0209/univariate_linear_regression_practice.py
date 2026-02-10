import numpy as np
import matplotlib.pyplot as plt  # 그래프 시각화 라이브러리

# Data Generation
np.random.seed(42)  # 난수

# 0에서 1 사이 (실수) 랜덤숫자를 100 개 만든다.
x = np.random.rand(100, 1)  # 100행 1열 형태(세로형)
y = 1 + 2 * x + 1 * np.random.randn(100, 1)
# 1 절편 ,
# 2 * x 기울기2 * 입력값,
# 1 * np.random.randn(100, 1) 노이즈 (완벽할 수 없어 , 현실 처럼 오차를 추가한다.)

# 인덱스 섞기
idx = np.arange(100)  # 0 ~ 99 까지 숫자를 순서대로 만들고
np.random.shuffle(idx)  # 순서를 랜덤으로 섞는다.

# 랜덤으로 섞인 인덱스중 처음 80 개를 학습용으로 사용.
train_idx = idx[:80]

# 랜덤으로 섞인 인덱스중 80 이후인 나머지 20개는 검증용으로 사용
val_idx = idx[80:]

# 학습용, 데이터 검증 데이터 셋 만들기
# 짝이 맞는 같은 인덱스에서 뽑아야 함

# 학습용인덱스 80개 중에서 x,y를 뽑아 학습데이터를 만든다.
x_train, y_train = x[train_idx], y[train_idx]
# 검증용 나머지 20개 중에서 x,y를 뽑아 검증데이터를 만든다.
x_val, y_val = x[val_idx], y[val_idx]

# Plot
# 도화지(fig)와 축(ax)를 만든다.
fig, ax = plt.subplots()


# C0,C1 matplotlib의 기본색상
# C0 = 파란색, 학습데이터를 산점도에 파란색점으로 표시, alpha(투명도)
ax.scatter(x_train, y_train, color="C0", label="train", alpha=0.5)
# C0 = 주황색, 검증데이터를 산점도에 주황색점으로 표시, alpha(투명도)
ax.scatter(x_val, y_val, color="C1", label="validation", alpha=0.5)
ax.legend()  # 범례표시(train/validation)
ax.grid(True)  # 격자선표시
fig.show()  # 로컬에서 주로 사용 (파이참,VS코드)
plt.show()  # 코랩은 브라우저 기반 안정적으로 출력 권장
