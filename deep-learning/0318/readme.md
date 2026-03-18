# 🧠 KLUE BERT 기반 NER / NLI 구현 프로젝트

## 📖 Overview

본 프로젝트는 KLUE 데이터셋을 활용하여 BERT 기반 NLP 모델을 직접 구현하고,


각 태스크별 구조를 이해하는 것을 목표로 진행되었습니다.

* NER (Named Entity Recognition)
* NLI (Natural Language Inference)
* Sentiment Analysis (NSMC)

---

## 🛠 Tech Stack

* Python
* TensorFlow 2.10
* PyTorch
* HuggingFace Transformers
* CUDA / GPU (RTX 3060)

---

## 🚀 Implementation

### 1. NER (Named Entity Recognition)

* BERT 기반 Token Classification 모델 구현
* BIO tagging 방식 적용 (PER, ORG, LOC 등)
* 토큰 단위 라벨 정렬 및 패딩 처리

👉 핵심 포인트

* 입력 토큰과 라벨 길이를 맞추는 과정에서 전처리 중요성 이해
* 시퀀스 기반 분류 구조 경험

---

### 2. NLI (Natural Language Inference)

* 문장 쌍 입력 구조 기반 분류 모델 구현
* `[CLS] sentence1 [SEP] sentence2 [SEP]` 구조 사용

👉 핵심 포인트

* 두 문장 간 관계를 학습하는 방식 이해
* Sequence Classification 구조 적용

---

### 3. Sentiment Analysis (NSMC)

* 영화 리뷰 데이터 기반 감성 분석 모델 구현
* BERT fine-tuning 실습

👉 핵심 포인트

* 텍스트 분류 기본 파이프라인 경험
* 학습/평가 구조 이해

---

## ⚠️ Issue (학습 과정에서 발생한 문제)

실습 과정에서 TensorFlow 기반 모델 학습 시
GPU는 인식되지만 학습 속도가 비정상적으로 느린 문제가 발생했습니다.

* GPU 사용률 저조 (≈ 5~10%)
* 일부 연산 CPU fallback 의심

---

## 🔥 Improvement

문제 해결을 위해 PyTorch 기반으로 모델을 재구현했습니다.

* HuggingFace + PyTorch 환경 적용
* GPU 활용률 개선
* 학습 속도 향상

---

## 📊 Comparison

| 항목      | TensorFlow | PyTorch |
| ------- | ---------- | ------- |
| GPU 활용률 | 낮음         | 높음      |
| 학습 속도   | 느림         | 개선      |

---

## 💡 What I Learned

* BERT 기반 다양한 NLP 태스크 구조 이해
* Token Classification vs Sequence Classification 차이 학습
* 데이터 전처리의 중요성 체감
* GPU는 단순 인식이 아닌 실제 활용이 중요함

---

## 🧾 Conclusion

본 프로젝트를 통해
단순 실습을 넘어 **모델 구조 이해와 학습 환경 문제 해결 경험**을 함께 얻을 수 있었습니다.
