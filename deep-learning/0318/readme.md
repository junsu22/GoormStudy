# 🧠 KLUE BERT 기반 NER / NLI 구현 및 학습 환경 개선

## 📖 Overview

본 프로젝트는 KLUE 데이터셋을 기반으로 BERT 모델을 활용한 다양한 NLP 태스크를 구현하고,
실습 과정에서 발생한 학습 환경 문제를 해결하며 프레임워크 차이를 비교한 프로젝트입니다.

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

## 📂 Project Structure

```
├── KLUE_BERT_NER.ipynb  
├── KLUE_BERT_NER_pytorch.ipynb  
├── KLUE_BERT_NLI_pytorch.ipynb  
├── nsmc_bert.ipynb  
├── KLUE_BERT_practice.ipynb  
├── ner_label.txt  
```

---

## 🚀 Tasks

### 1. NER (Named Entity Recognition)

* Token Classification 기반 BERT 모델 구현
* BIO tagging 방식 적용
* 커스텀 라벨 매핑 구성

### 2. NLI (Natural Language Inference)

* 문장 쌍 입력 기반 분류 모델
* entailment / contradiction / neutral 분류

### 3. Sentiment Analysis

* NSMC 데이터셋 기반 감성 분류
* BERT fine-tuning 실습

---

## ⚠️ Issue

TensorFlow 기반으로 학습을 진행하는 과정에서
GPU는 정상적으로 인식되었지만, 실제 학습 속도가 기대보다 느린 문제가 발생했습니다.

* GPU 사용률 저조 (≈ 5~10%)
* 일부 연산 CPU fallback 의심
* 학습 속도 비효율

---

## 🔥 Solution

문제 해결을 위해 PyTorch 기반으로 모델을 재구현했습니다.

* HuggingFace + PyTorch 환경으로 전환
* GPU 활용률 개선
* 학습 속도 향상
* 디버깅 용이성 증가

---

## 📊 Result

| 항목      | TensorFlow | PyTorch |
| ------- | ---------- | ------- |
| GPU 활용률 | 낮음         | 높음      |
| 학습 속도   | 느림         | 개선      |
| 디버깅     | 어려움        | 쉬움      |

---
## 🧾 Conclusion

본 프로젝트를 통해 단순 모델 구현을 넘어,

**문제 발생 → 원인 분석 → 프레임워크 전환 → 성능 개선**

이라는 실제 개발 과정을 경험할 수 있었습니다.
