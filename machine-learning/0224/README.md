# 📌 AdaBoost 알고리즘 이해하기 (Human Activity Recognition 실습 정리)

## ✅ AdaBoost란?

**AdaBoost(Adaptive Boosting)** 는 여러 개의 약한 모델(weak learner)을 순차적으로 학습시키면서,
이전 모델이 **틀린 데이터에 점점 더 집중하도록 만드는 앙상블(Ensemble) 알고리즘**이다.

단순히 모델을 반복 학습하는 것이 아니라,
**데이터의 중요도(weight)를 조정하며 학습 방식이 계속 변화한다**는 점이 핵심이다.

---

## 🧠 핵심 아이디어

일반적인 학습 방식은 전체 데이터를 다시 학습한다.

하지만 AdaBoost는 다르게 동작한다.

> ❌ 전체 데이터를 다시 학습하지 않는다
> ✅ 이전 모델이 틀린 데이터의 중요도를 높여 다음 모델이 더 집중하도록 만든다

즉, 학습이 진행될수록 모델은 **어려운 데이터(오답 데이터)** 를 더 많이 보게 된다.

---

## ⚙️ 동작 과정 (직관적 흐름)

1. 모든 데이터는 동일한 중요도로 시작한다.
2. 첫 번째 모델을 학습한다.
3. 모델이 틀린 데이터를 찾는다.
4. 틀린 데이터의 가중치(weight)를 증가시킨다.
5. 다음 모델은 해당 데이터를 더 중요하게 학습한다.
6. 이 과정을 여러 번 반복한다.
7. 여러 모델의 결과를 결합하여 최종 예측을 만든다.

---

## 🎯 한 줄 핵심 정리

> **AdaBoost는 틀린 데이터를 더 중요하게 만들어, 학습이 점점 오류를 보완하도록 만드는 알고리즘이다.**

---

## 📊 실습 내용 (HAR Dataset)

Human Activity Recognition 데이터셋을 이용해 AdaBoostClassifier를 적용하였다.

```python
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score

clf = AdaBoostClassifier(
    n_estimators=30,
    random_state=10,
    learning_rate=0.1
)

clf.fit(X_train, y_train)
pred = clf.predict(X_test)

print('Ada boost 정확도 : {:.4f}'.format(
    accuracy_score(y_test, pred)
))
```

실습 결과 AdaBoost는 약 **0.77 수준의 정확도**를 보이며,
단일 Decision Tree보다 성능이 향상되는 것을 확인할 수 있었다.

---

## 💡 AdaBoost의 특징

* 약한 모델(주로 얕은 Decision Tree)을 여러 개 결합
* 이전 모델의 오류를 다음 모델이 보완
* 데이터 가중치를 계속 조정하며 학습
* 이상치(outlier)에 비교적 민감함


---

## ✨ 정리

AdaBoost는 모델을 복잡하게 만드는 알고리즘이 아니라,
**학습 순서를 똑똑하게 바꾸는 알고리즘**이다.

틀린 데이터를 중심으로 학습이 계속 적응(adaptive)하면서
여러 약한 모델이 서로의 실수를 보완하도록 만든다.
