# 📌 아마존 리뷰 데이터셋을 활용한 텍스트 요약 구현 (Seq2Seq + Attention) + TextRank 비교

## 📌 개요

이번 실습에서는 텍스트 요약을 두 가지 방식으로 구현했다.

1️⃣ **딥러닝 기반 생성적 요약 (Seq2Seq + Attention)**
2️⃣ **그래프 기반 추출적 요약 (GloVe + TextRank)**

특히 과제 요구사항에 맞게
👉 **아마존 리뷰 데이터셋 기반 Seq2Seq + Attention 모델 구현**을 중심으로 진행하고,
👉 추가적으로 TextRank 방식과 비교를 수행했다.

---

## ⚙️ 전체 흐름

```text id="c1n7a1"
[생성적 요약]
데이터 → 전처리 → 시퀀스 → 모델 학습 → 문장 생성

[추출적 요약]
문서 → 문장 분리 → 임베딩 → 유사도 → 그래프 → 순위 → 문장 선택
```

---

# 1️⃣ Seq2Seq + Attention 기반 텍스트 요약 (생성적 요약)

## 📊 개요

아마존 리뷰 데이터를 활용하여
입력 문장을 기반으로 요약 문장을 생성하는 모델을 구현했다.

---

## 🧹 데이터 전처리

### ✔ 텍스트 → 시퀀스 변환

* Tokenizer를 사용하여 정수 시퀀스로 변환

### ✔ Seq2Seq 구조

```text id="cs6n8x"
encoder_input → 입력 문장  
decoder_input → 시작 토큰 포함 문장  
decoder_target → 실제 출력 문장  
```

### ✔ Padding

* `pad_sequences()`로 길이 통일

---

## 🧠 모델 구조

* Encoder: LSTM
* Decoder: LSTM
* Attention: Bahdanau Attention 적용
* Loss: sparse_categorical_crossentropy
* Optimizer: RMSprop

---

## ⚠️ 주요 문제 & 해결 과정

### 🔥 길이 불일치 문제

👉 `pad_sequences()`로 해결

---

### 🔥 np.delete 오류

👉 filtering 방식으로 대체

---

### 🔥 tuple → numpy 문제

👉 `pad_sequences()`로 변환

---

### 🔥 shape mismatch

```python id="7zj2mf"
decoder_target_train = decoder_target_train.reshape(
    decoder_target_train.shape[0],
    decoder_target_train.shape[1],
    1
)
```

---

## 🚀 학습 결과

* train loss: 감소
* val loss: 안정적 감소

👉 모델은 정상적으로 학습됨

---

## 🧪 예측 결과

```text id="s7l0d6"
원문: mom kids older two hard time finding snack...
실제 요약: healthy snack
예측 요약: for the go
```

👉 의미 일부 반영되지만 정확도는 제한적

---

## 📌 특징

👉 **새로운 문장을 생성하는 방식 (Generative)**

---

# 2️⃣ GloVe + TextRank 기반 텍스트 요약 (추출적 요약)

## 📊 개요

테니스 기사 데이터를 활용하여
GloVe 임베딩과 TextRank 알고리즘 기반 요약을 구현했다.

---

## ⚙️ 전체 흐름

```text id="4kj2zj"
문장 분리 → 토큰화 → GloVe → 문장 벡터 → 유사도 → 그래프 → PageRank → 요약
```

---

## 🧠 핵심 구현

### ✔ 문장 벡터 생성

```python id="t5nn1w"
def calculate_sentence_vector(sentence):
    return sum([glove_dict.get(word, zero_vector)
                for word in sentence]) / len(sentence)
```

---

### ✔ 그래프 생성

```python id="bczq5y"
nx_graph = nx.from_numpy_array(sim_matrix)
```

---

### ✔ 중요도 계산

```python id="2p0zjv"
scores = nx.pagerank(nx_graph)
```

---

## 🧪 결과

👉 중요도가 높은 문장을 선택하여 요약 생성
👉 원문 문장을 그대로 사용

---

## 📌 특징

👉 **기존 문장을 선택하는 방식 (Extractive)**

---

# 🔥 두 방식 비교

| 구분 | Seq2Seq + Attention | TextRank |
| -- | ------------------- | -------- |
| 방식 | 생성                  | 추출       |
| 학습 | 필요                  | 불필요      |
| 모델 | LSTM                | 그래프      |
| 속도 | 느림                  | 빠름       |
| 결과 | 자연스러움               | 안정적      |

---

# 💥 공통 문제 (실습 현실)

이번 실습에서 가장 크게 느낀 점은

👉 **환경 문제가 매우 큰 비중을 차지한다는 것**

---

### ❗ 주요 에러

* gensim 설치 문제
* nltk `punkt`, `punkt_tab` 오류
* GloVe 로딩 시간


---

# 🧠 느낀 점

### 1️⃣ 생성 vs 추출은 완전히 다른 접근이다

* Seq2Seq → 문장 생성
* TextRank → 문장 선택

---

### 2️⃣ 딥러닝은 데이터 구조가 핵심이다

* padding, shape, sequence 중요

---

### 3️⃣ 전통 NLP도 충분히 강력하다

* 학습 없이도 요약 가능

---

### 4️⃣ 실습은 항상 예상대로 흘러가지 않는다

* 하지만 그 과정에서 더 많이 배운다

---

# 💡 한줄 정리

👉 **텍스트 요약은 생성과 추출 두 가지 방식으로 해결할 수 있다**


---

# 🙌 마무리

이번 실습을 통해
단순 구현을 넘어서

👉 **텍스트 요약의 다양한 접근 방식을 직접 경험**할 수 있었다.

특히
👉 딥러닝 기반 모델과 전통 NLP 기법을 모두 구현해본 점이 큰 수확이었다.
