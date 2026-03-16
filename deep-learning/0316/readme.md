# Attention 모델 논문 정리

딥러닝 자연어 처리에서 중요한 **Attention 메커니즘의 발전 흐름**을 이해하기 위해 주요 논문들을 정리하였다.

본 문서는 다음 논문들을 기반으로 작성되었다.

- Seq2Seq (2014)
- Bahdanau Attention (2014)
- Memory Network (2015)
- Luong Attention (2015)
- Attention Is All You Need (2017)

---

# Attention 모델 발전 흐름

```
Seq2Seq (2014)

↓

Seq2Seq + Attention (Bahdanau, 2014)

↓

Memory Network (2015)

↓

Attention Is All You Need (2017) → Transformer
```

---

# 정리한 논문 목록

## 1. Seq2Seq + BiLSTM Attention

파일  
```
seq2seq_attention_bilstm_attention.md
```

내용

- Seq2Seq 모델 구조
- Attention Mechanism 개념
- BiLSTM + Attention 구조
- Context Vector 계산

핵심 개념

```
Query (Q)
Key (K)
Value (V)
```

Attention은 Query와 Key의 유사도를 계산하여  
Value를 가중합하여 결과를 생성한다.

---

# 2. Bahdanau Attention (2014)

파일

```
bahdanau_attention_2014.md
```

논문

```
Neural Machine Translation by Jointly Learning to Align and Translate
```

저자

```
Dzmitry Bahdanau
KyungHyun Cho
Yoshua Bengio
```

핵심 아이디어

기존 Seq2Seq 모델은 입력 문장을 하나의 **fixed-length vector**로 압축한다.

이 과정에서 **긴 문장에서 정보 손실이 발생하는 문제**가 있다.

이를 해결하기 위해 **Attention Mechanism**이 제안되었다.

Context Vector 계산

```
c_i = Σ α_ij h_j
```

```
α_ij = softmax(e_ij)
```

Attention은 입력 문장의 hidden state 중  
**중요한 부분에 집중하도록 한다.**

---

# 3. Memory Network (2015)

파일

```
MemoryNetwork.md
```

논문

```
Memory Networks
```

저자

```
Jason Weston
Sumit Chopra
Antoine Bordes
```

핵심 개념

Memory Network는 **장기 메모리(long-term memory)**를 활용하는 모델이다.

모델 구조

```
I : Input feature map
G : Generalization
O : Output feature map
R : Response
```

동작 과정

```
1 입력을 feature representation으로 변환

2 메모리에 정보 저장

3 메모리를 기반으로 추론 수행

4 최종 응답 생성
```

Memory Network는 **Question Answering 문제**에서  
지식 기반 추론을 수행할 수 있다.

---

# 4. Luong Attention (2015)

파일

```
Luong Attention.md
```

논문

```
Effective Approaches to Attention-based Neural Machine Translation
```

저자

```
Minh-Thang Luong
Hieu Pham
Christopher D. Manning
```

Luong Attention은 **Bahdanau Attention 이후 제안된 Attention 구조**이다.

Attention 계산 방식을 단순화하여  
계산 효율을 개선하였다.

### Attention Score 계산

#### Dot Attention

```
score(s_t, h_i) = s_t^T h_i
```

#### General Attention

```
score(s_t, h_i) = s_t^T W h_i
```

#### Concat Attention

```
score(s_t, h_i) = v^T tanh(W[s_t ; h_i])
```

### Attention 방식

**Global Attention**

입력 문장의 모든 hidden state를 사용하여  
attention을 계산한다.

**Local Attention**

입력 문장의 일부 hidden state만 사용하여  
attention을 계산한다.

이를 통해 계산 비용을 줄이면서도 성능을 유지한다.

---

# 5. Attention Is All You Need (2017)

파일

```
Attention is All you Need.md
```

논문

```
Attention Is All You Need
```

저자

```
Ashish Vaswani 외
```

이 논문은 **Transformer 모델**을 제안하였다.

Transformer는 RNN이나 CNN을 사용하지 않고  
**Self-Attention 구조만으로 문장을 처리한다.**

핵심 구조

```
Self Attention
Multi-head Attention
Positional Encoding
Feed Forward Network
```

Transformer는 이후

```
BERT
GPT
T5
LLM
```

등 대부분의 현대 NLP 모델의 기반이 되었다.

---

# 정리

Attention Mechanism은 자연어 처리에서 중요한 기술이며  
다음과 같은 흐름으로 발전하였다.

```
Seq2Seq

↓

Bahdanau Attention

↓

Luong Attention

↓

Transformer
```

이러한 발전을 통해 모델은  
**긴 문장에서도 중요한 정보를 선택적으로 학습**할 수 있게 되었다.

---

# Repository 구조

```
0316
 ├─ images
 ├─ Attention is All you Need.md
 ├─ Luong Attention.md
 ├─ MemoryNetwork.md
 ├─ bahdanau_attention_2014.md
 ├─ seq2seq_attention_bilstm_attention.md
 └─ readme.md
```
