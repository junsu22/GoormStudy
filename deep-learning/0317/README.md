# Transformer부터 BERT까지: 수업 필기 정리

---

## 1. RNN과 Transformer

### RNN
- RNN은 병렬 연산이 어렵다.
- 많은 Attention 메커니즘이 RNN과 함께 사용되었다.

사람들은 이런 의문이 생긴다.

```text
Attention으로 모든 state에 접근할 수 있다면
굳이 RNN이 필요할까?
```

- 병렬 연산을 추구하면서 RNN을 사용하지 않는 구조가 등장했다.

---

## 2. Transformer

Transformer는 기계 번역 모델이다.

- Encoder - Decoder 구조
- Encoder Block × N
- Decoder Block × N

```text
Encoder Block × N
Decoder Block × N
```

---

## 3. Embedding

- Embedding Layer를 사용한다.
- 단어를 임베딩 벡터로 바꾼다.
- 임베딩 벡터를 Encoder / Decoder 입력으로 사용한다.

---

## 4. Positional Encoding

- RNN은 순차적 구조이기 때문에 순서 정보가 자연스럽게 반영된다.
- Transformer는 순서를 알 수 없기 때문에 위치 정보가 필요하다.
- 위치 정보를 벡터에 더해 준다.
- sin / cos 함수를 사용한다.

```text
pos : 단어 위치
i : 임베딩 차원
d_model : 벡터 차원
```

---

## 5. Transformer의 Attention 종류

Transformer에는 세 가지 Attention이 존재한다.

### 1) Encoder Self Attention

```text
Q = K = V
```

- Encoder 내부 단어 관계를 계산한다.

### 2) Masked Decoder Self Attention

- Decoder Self Attention
- 미래 단어를 보면 안 된다.
- 그래서 Masking을 사용한다.
- Teacher Forcing 상황에서 미래 단어를 보는 것을 방지한다.

### 3) Encoder-Decoder Attention

```text
Q : Decoder vector
K : Encoder vector
V : Encoder vector
```

- Decoder가 Encoder 정보를 참고한다.

---

## 6. Attention 계산

- Query vector
- Key vector
- 두 벡터를 사용하여 Attention score를 계산한다.

### Scaled Dot Attention

- Attention score 계산 방식

```text
Q · K
```

- Attention score를 만든다.

### Multi Head Attention

- 여러 개의 Attention을 수행한다.

```text
Concat한 결과에 출력 가중치 W^O를 곱한다.
```

### Padding Mask

- PAD 토큰은 실제 단어가 아니다.
- 문장 길이 맞추기 용도이다.
- Attention 계산에서 제외한다.
- Mask를 적용한다.

### Feed Forward

```text
f = Wx + b
```

### Add & Norm

- Residual connection
- 입력 + 출력
- 정규화 수행

```text
Layer Norm
```

- gamma = 1
- beta = 0

### Decoder Attention

```text
Q : Decoder
K : Encoder
V : Encoder
```

- Decoder가 Encoder 정보를 사용해 다음 단어를 생성한다.

---

## 7. inference (추론)

- 테스트 단계
- 예: 번역기, 챗봇이 구동될 때
- 디코더가 단어를 1개씩 생성한다.

---

## 8. ELMO

- ELMO는 언어모델로부터 얻는 임베딩이다.
- 양방향 언어모델을 사용한다.
- 순방향 / 역방향 언어모델을 따로 학습한 뒤 합친다.

### ELMO 특징

- 각 층 출력값을 연결한다.
- 각 층 출력값별로 가중치를 준다.
- 각 층 출력값을 모두 더한다.
- 벡터의 크기를 결정하는 스칼라 매개변수를 곱한다.

- 논문 읽어보기

---

## 9. pre-training in NLP

- 워드 임베딩은 딥러닝 자연어 처리의 기본이다.
- 사전 훈련된 임베딩은 대용량 텍스트에서 단어들의 동시 등장 통계로 훈련시키는 방법이다.

예:
- word2vec
- GloVe

- 이런 임베딩을 불러와서 추가 학습할 수 있다.

### 문제
- 단어는 문맥에 따라서 뜻이 달라진다.

### 해결 방법
- 언어 모델을 사전 훈련시켜 문맥에 따른 표현을 얻는다.

---

## 10. 관련 흐름

- Semi-supervised Sequence Learning (2015)
- Deep Contextualized Word Embeddings (2017)
- Improving Language Understanding by Generative Pre-Training / OpenAI (2018)

- 논문은 세부 구현보다 컨셉과 발전 방향을 보는 것

---

## 11. GPT

- 여러 언어모델을 학습한 후 fine-tuning 시킨다.
- 이 모델을 GPT라고 한다.
- 구조는 이전에도 있었음을 알 수 있다.

### 특징
- 단방향 모델
- 이전 단어들을 보고 다음 단어를 예측한다.
- RNN, Transformer 계열에서 사용된다.

### 문제점
- 정방향 또는 역방향으로만 진행되었다.
- 양방향이 아니었다.

### 왜 언어모델은 단방향만 될까?
- 양방향이면 미리 예측할 단어를 보게 되므로 정답을 미리 주는 문제가 생긴다.

---

## 12. Masked Language Model

- 해결 방법: 일부 단어를 마스크 처리하고 그 단어를 예측하도록 한다.
- 논문에서는 15%를 제안한다.

```text
15%
```

### 마스크 토큰 처리
- 80%는 `[MASK]`로 바꾼다.
- 10%는 랜덤 단어로 바꾼다.
- 10%는 그대로 둔다.

---

## 13. BERT

### BERT 이전 pretrained model

#### Feature-based 방식
- 사전 훈련된 모델의 파라미터를 고정한다.
- ELMO
- shallow한 양방향
- ELMO는 양방향이지만 진짜 깊은 양방향은 아님

#### Fine-tuning 방식
- 사전 훈련된 모델 파라미터까지 함께 학습한다.
- GPT는 단방향 모델

### BERT 방식
- GPT와 다르게 양방향 모델
- understanding에 초점
- 문맥 파악이 강함

- GPT는 잘 만들어내는 쪽
- BERT는 문맥 이해 쪽

---

## 14. Unidirectional vs Bidirectional

### Unidirectional
- 이전 단어들을 보고 다음 단어 예측

### Bidirectional
- 주변 단어를 보고 마스크된 단어 예측

---

## 15. BERT 학습 방식

BERT는 두 가지 방법으로 학습한다.

### 1) Masked Language Model
- 문장에 15% 마스킹 후 마스크 단어를 예측

### 2) Next Sentence Prediction
- 문장 사이 관계를 학습하기 위해 다음 문장 예측 태스크 도입
- 붙어 있던 문장인지 맞추는 문제 수행

---

## 16. BERT 입력 토큰

- `[CLS]`
- `[SEP]`
- `[MASK]`

---

## 17. BERT 임베딩

Transformer는
- Input Embedding
- Positional Encoding

BERT는 여기에 Segment Embedding을 추가한다.

즉 총 3개 임베딩 사용
- Token Embedding
- Position Embedding
- Segment Embedding

### 참고
- Position Embedding은 Positional Encoding을 대체할 수 있다.

---

## 18. BERT Base vs BERT Large

### BERT Base
- Transformer Encoder 12층

### BERT Large
- Transformer Encoder 24층

- 허깅페이스에서 Base / Large가 몇 층인지 확인 가능

---

## 19. BERT 적용

- 방대한 데이터로 사전 훈련된 언어모델 BERT 사용
- 그 위에 풀고자 하는 태스크용 추가 신경망을 붙인다.
- BERT의 윗단 부분에 신경망을 추가해서 원하는 태스크 수행

예:
- Text Classification
- Named Entity Recognition
- Question Answering
- NLI

### CLS 토큰
- BERT는 사전학습 시 첫 번째 토큰 `[CLS]`를 사용한다.
- 문장 분류 등에서 최종 classification head 입력으로 사용한다.

---

## 20. BERT 이후

- 모순 / 중립 관계 같은 태스크도 있었음
- 하지만 이후 연구들은 모순 / 중립 자체보다 다른 방향도 중요하게 봄

---

## 21. Attention Mask

- 실제 BERT를 사용할 경우 필요한 입력
- 마스킹 학습이 끝난 뒤에는 나머지 패딩 토큰을 넣고
- 또 다른 입력으로 attention mask를 함께 사용한다.

### attention mask 값
- 실제 단어: 1
- 패딩 토큰: 0
