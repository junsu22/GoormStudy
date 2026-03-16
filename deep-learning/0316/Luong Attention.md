# Effective Approaches to Attention-based Neural Machine Translation (2015)

신경 기계 번역에서 Attention 메커니즘의 효율적인 적용 방법을 제안한 논문

저자 : Minh-Thang Luong, Hieu Pham, Christopher D. Manning

---

# Luong Attention

Luong Attention은 **Bahdanau Attention 이후 제안된 Attention Mechanism**이다.

기존 Seq2Seq 모델에서는 입력 문장을 하나의 fixed-length vector로 압축하기 때문에  
문장이 길어질수록 정보 손실이 발생하는 문제가 있었다.

Luong Attention은 이러한 문제를 해결하기 위해  
디코더가 단어를 생성할 때 **입력 문장의 hidden state들을 참고하여 중요한 정보에 집중하도록 하는 방법**을 제안하였다.

---

# Luong Attention 핵심

Luong Attention은 Bahdanau Attention 이후 제안된 Attention Mechanism으로  
Attention 계산 방식을 단순화하고 계산 효율을 개선한 모델이다.

이 모델은 **Encoder–Decoder 기반 신경 기계 번역 구조**에서  
디코더가 단어를 생성할 때 입력 문장의 중요한 부분에 집중하도록 한다.

---

# Attention Score 계산 방식

Luong 논문에서는 Attention Score를 계산하는 세 가지 방법을 제안하였다.

## Dot Attention (벡터 내적)

디코더 hidden state와 encoder hidden state의 내적을 이용하여 계산한다.

score(s_t, h_i) = s_t^T h_i

---

## General Attention (가중치 행렬 W 추가)

encoder hidden state에 가중치 행렬 W를 적용하여 attention score를 계산한다.

score(s_t, h_i) = s_t^T W h_i

---

## Concat Attention (두 벡터 결합 후 신경망 계산)

디코더 hidden state와 encoder hidden state를 결합한 뒤  
신경망을 통해 attention score를 계산한다.

score(s_t, h_i) = v^T tanh(W[s_t ; h_i])

---

# Attention 방식

Luong 논문에서는 Attention을 적용하는 두 가지 방식을 제안하였다.

## Global Attention

모든 encoder hidden state를 참고하여 attention을 계산하는 방식이다.

즉 디코더는 입력 문장의 전체 정보를 참고하여  
context vector를 생성한다.

---

## Local Attention

입력 문장의 특정 위치 주변 hidden state만 선택하여  
attention을 계산하는 방식이다.

이를 통해 계산량을 줄이면서도 번역 성능을 유지할 수 있다.

---

# Conclusion 요약

Luong Attention은 Bahdanau Attention을 기반으로  
더 효율적인 Attention 계산 방법을 제안하였다.

특히 다음 두 가지 구조를 통해 계산 효율과 번역 성능을 개선하였다.

- Global Attention
- Local Attention

또한 Dot, General, Concat 방식의 Attention Score 계산 방법을 제안하여  
Attention 기반 신경 기계 번역 모델 발전에 중요한 기여를 하였다.