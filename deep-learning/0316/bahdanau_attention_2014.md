# NEURAL MACHINE TRANSLATION BY JOINTLY LEARNING TO ALIGN AND TRANSLATE (2014)

정렬(Alignment)과 번역을 동시에 학습하는  
신경망 기반 기계 번역 모델

저자 : Dzmitry Bahdanau 외 2명

---

## ABSTRACT 원문
Neural machine translation is a recently proposed approach to machine translation. Unlike the traditional statistical machine translation, the neural machine translation aims at building a single neural network that can be jointly tuned to maximize the translation performance. The models proposed recently for neural machine translation often belong to a family of encoder–decoders and encode a source sentence into a fixed-length vector from which a decoder generates a translation. In this paper, we conjecture that the use of a fixed-length vector is a bottleneck in improving the performance of this basic encoder–decoder architecture, and propose to extend this by allowing a model to automatically (soft-)search for parts of a source sentence that are relevant to predicting a target word, without having to form these parts as a hard segment explicitly. With this new approach, we achieve a translation performance comparable to the existing state-of-the-art phrase-based system on the task of English-to-French translation. Furthermore, qualitative analysis reveals that the (soft-)alignments found by the model agree well with our intuition.

---

신경망 기계 번역(Neural Machine Translation, NMT)은  
최근 제안된 기계 번역 접근 방식이다.

기존의 통계 기반 기계 번역(statistical machine translation)과 달리  
신경망 기계 번역은 번역 성능을 최대화하도록 하나의 신경망 모델을  
**end-to-end 방식으로 학습**하는 것을 목표로 한다.

최근 제안된 대부분의 신경망 기계 번역 모델은  
**Encoder–Decoder 구조**를 사용하며,  
입력 문장을 **고정 길이 벡터(fixed-length vector)**로 인코딩한 뒤  
디코더가 이 벡터를 기반으로 번역 문장을 생성한다.

그러나 본 논문에서는  
이 **고정 길이 벡터가 Encoder–Decoder 구조의 성능 향상에 병목(bottleneck)** 이 될 수 있다고 가정한다.

이를 해결하기 위해  
모델이 번역 과정에서 **출력 단어를 예측할 때 입력 문장의 관련 부분을 자동으로 탐색하도록 하는 방법**을 제안한다.

이 방식은 입력 문장을 명시적으로 분할하지 않고도  
**soft alignment 방식으로 필요한 정보를 선택**할 수 있다.

이 접근 방법을 통해  
영어 → 프랑스어 번역 작업에서  
기존 **state-of-the-art phrase-based 시스템과 유사한 수준의 번역 성능**을 달성하였다.

또한 분석 결과 모델이 학습한 **soft alignment**가  
사람이 직관적으로 생각하는 번역 대응 관계와도 잘 일치함을 확인하였다.

# 3 LEARNING TO ALIGN AND TRANSLATE


모델은 다음 두 구성 요소로 이루어진다.
- **Encoder** : Bidirectional RNN을 사용하여 입력 문장을 인코딩한다.
- **Decoder** : 인코딩된 정보를 바탕으로 번역 문장을 생성하는 RNN이다.

Encoder는 입력 문장을 처리하여
각 단어에 대한 **hidden state(은닉 상태)**를 생성한다.

Decoder는 번역 단어를 생성할 때
입력 문장의 특정 부분에 집중하도록 Attention Mechanism을 사용한다.


# Context Vector

기존 Seq2Seq 모델은
입력 문장을 하나의 fixed-length vector로 압축한다.

하지만 Bahdanau Attention에서는
각 단어를 생성할 때 context vector를 다시 계산한다.

context vector는 다음과 같이 정의된다.
```
c_i = Σ α_ij h_j
h_j : encoder hidden state (입력 단어의 은닉 상태)
α_ij : attention weight (각 단어의 중요도를 나타내는 가중치)
```
context vector는 Encoder의 hidden state들을 attention weight로 가중합한 값이다.

# Conclusion 요약
기존 인코더-디코더 기반 신경계 기계번역모델은 벡터 길이가 고정되어 있어
병목현상이 발생하였다.

병목 현상을 해결하기 위해 
Attention Mechanism를 도입하였고, 
단어를 생성할 때 입력 문장의 관련 부분을 soft alignment 방식으로 탐색하는 새로운 RNN을 제안하였다.
실험 결과, 제안된 모델은 기존 Encoder–Decoder 모델보다
번역 성능이 향상되었으며
문장 길이에 더 **강건한 성능**을 보였다.