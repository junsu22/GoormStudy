https://wikidocs.net/22893



# Seq2Seq-Attention (Bahdanau Attention)

Seq2Seq-Attention 모델은 기존 Encoder–Decoder 구조에서 발생하는
fixed-length vector 문제를 해결하기 위해 제안된 구조이다.

기존 Seq2Seq 모델은 입력 문장을 하나의 벡터로 압축하기 때문에
긴 문장에서 정보 손실이 발생할 수 있다.

이를 해결하기 위해 Attention Mechanism이 도입되었다.

Attention은 디코더가 단어를 생성할 때
입력 문장의 모든 hidden state를 참고하여
중요한 단어에 더 높은 가중치를 부여한다.

이를 통해 모델은 입력 문장의 특정 부분에 집중하며
더 정확한 번역 결과를 생성할 수 있다.

주어진 '쿼리(Query)'에 대해서 모든 '키(Key)'와의 유사도를 각각 구한 후 
구한 유사도를 값(value) 에 반영한다.
반영된 값을 모두 더해  리턴한다. 어텐션 값(attention value)



1. Attention Score 

디코더 현재 시점 t의 hidden state를 s_t
인코더 i번째 hidden state를 h_i 라고 하면

Dot-Product Attention에서 attention score는
두 벡터의 내적(dot product)으로 계산한다.

score(s_t, h_i) = s_t^T * h_i


2. 모든 Attention Score

인코더 hidden state가 N개라면

e_{t,i} = s_t^T * h_i

그리고 모든 attention score는

e_t = [e_{t,1}, e_{t,2}, ..., e_{t,N}]


3. Attention Weight 계산 (Softmax)

attention score를 확률 형태로 변환하기 위해
softmax 함수를 적용한다.

α_{t,i} = exp(e_{t,i}) / Σ exp(e_{t,k})

4. Context Vector (Attention Value)

attention weight를 이용하여
encoder hidden state의 가중합을 계산한다.

c_t = Σ α_{t,i} * h_i

```
Attention(Q, K, V) = Attention Value
```
```
Q = Query : t 시점의 디코더 셀에서의 은닉 상태
K = Keys : 모든 시점의 인코더 셀의 은닉 상태들
V = Values : 모든 시점의 인코더 셀의 은닉 상태들

```

-- 
# BiLSTM-Attention

BiLSTM-Attention 모델은 Bidirectional LSTM과
Attention Mechanism을 결합한 구조이다.

BiLSTM은 문장을 앞 방향과 뒤 방향으로 동시에 처리하여
문맥 정보를 더 풍부하게 학습할 수 있다.

Attention Mechanism은 모델이 입력 문장에서
중요한 단어에 집중하도록 도와준다.

이 구조를 통해 모델은 문장의 전체 문맥을 고려하면서
핵심 정보에 집중할 수 있으며

감정 분석, 기계 번역, 질의응답 등
다양한 자연어 처리 작업에서 활용된다.