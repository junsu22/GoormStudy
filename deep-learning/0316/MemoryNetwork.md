# MEMORYNETWORKS (2015)
저자 :  Jason Weston, Sumit Chopra 

ABSTRACT 원문 
We describe a new class of learning models called memory networks. Memory
networks reason with inference components combined with a long-term memory
component; they learn how to use these jointly. The long-term memory can be
read and written to, with the goal of using it for prediction. We investigate these
models in the context of question answering (QA) where the long-term mem
ory effectively acts as a (dynamic) knowledge base, and the output is a textual
response. We evaluate them on a large-scale QA task, and a smaller, but more
complex, toy task generated from a simulated world. In the latter, we show the
reasoning power of such models by chaining multiple supporting sentences to an
swer questions that require understanding the intension of verbs.



Memory Network는 새로운 형태의 학습 모델이다.

이 모델은 **추론(inference) 구성 요소와 장기 메모리(long-term memory)**를 결합하여 작동하며,
두 요소를 함께 활용하는 방법을 학습한다.

장기 메모리는 **읽기(read)와 쓰기(write)**가 가능하며
이를 활용하여 예측(prediction)을 수행한다.

본 연구에서는 질문 응답(Question Answering, QA) 문제에
Memory Network를 적용하였다.

이때 장기 메모리는 **동적인 지식 베이스(dynamic knowledge base)**처럼 동작하며
모델의 출력은 텍스트 형태의 응답이다.

실험은

- 대규모 QA 데이터셋

- 시뮬레이션 환경에서 생성된 더 복잡한 toy task

에서 수행되었다.

특히 두 번째 실험에서는
여러 문장을 연결하여 추론하는 과정을 통해
동사의 의미까지 이해해야 하는 질문에 답할 수 있음을 보여주었다.



## 1 INTRODUCTION 

기존의 많은 머신러닝 모델은 장기 메모리(long-term memory)를 효과적으로 활용하는 구조가 부족하다.


예를 들어

어떤 이야기나 사실을 입력받고

그 내용에 대해 질문에 답하는 문제

에서는 과거 정보를 기억하고 활용하는 능력이 필요하다.

RNN 같은 모델은 예를 들어

어떤 이야기나 사실을 입력받고

그 내용에 대해 질문에 답하는 문제

에서는 과거 정보를 기억하고 활용하는 능력이 필요하다.

특히, 

- 긴 정보 기억

- 사실 저장

- 복잡한 추론

과 같은 작업에서는 성능이 제한된다.

이러한 문제를 해결하기 위해 본 논문에서는 Memory Network라는 새로운 모델을 제안한다.


Memory Network의 핵심 아이디어는
읽기와 쓰기가 가능한 장기 메모리(long-term memory)를 모델에 추가하고
추론(inference) 과정과 결합하는 것이다.
모델은 학습 과정에서 메모리를 활용하여 정보를 저장하고 검색하는 방법을 학습한다.



2 MEMORY NETWORKS 

Memory Network는 메모리(memory)와 네 가지 구성 요소로 이루어진 모델이다.
모델은 메모리에 정보를 저장하고

필요한 정보를 읽어 추론을 수행한 뒤 응답을 생성한다.

## Memory Network 네 가지 구성 요소

### I (Input feature map)
입력 데이터를 **모델 내부 표현(feature representation)**으로 변환한다.

### G (Generalization)
새로운 입력이 들어오면 메모리를 업데이트하는 역할을 한다.
### O (Output feature map)
현재 입력과 메모리를 기반으로 출력에 필요한 정보를 계산한다.

### R (Response)
O 단계에서 생성된 출력 특징을 이용해 최종 응답을 생성한다.



# 모델 동작 과정
```
1 입력 x → I(x)로 변환

2 메모리 업데이트
mi = G(mi, I(x), m)

3 메모리를 활용하여 출력 계산
o = O(I(x), m)

4 최종 응답 생성
r = R(o)
```
(실험 내용 중략 ..)

# Conclusion 요약

Memory Network는 장기 메모리(long-term memory)를 활용하여 추론을 수행하는 새로운 신경망 모델이다.

본 연구에서는 Memory Network를 질문 응답(Question Answering) 문제에 적용하여
메모리에 저장된 정보를 기반으로 여러 문장을 연결해 추론할 수 있음을 보여주었다.

향후 연구에서는 

- 더 어려운 QA 문제
- 복잡한 문장 구조 이해 
- 다단계 추론(multi-hop reasoning)

과 같은 문제에 Memory Network를 적용할 필요가 있다.

또한

- 더 정교한 메모리 관리 방법
- 더 강력한 문장 표현 방식 

을 통해 모델 성능을 향상시킬 수 있다.

Memory Network는 텍스트뿐 아니라 컴퓨터 비전 등 다양한 분야에도 적용될 가능성이 있다.

