# 🐾 Pet Similarity Recommendation System
Kaggle Dataset을 활용한 정규화 기반 추천 시스템 실습

---

## 📌 Project Overview
본 프로젝트는 Kaggle의 **PetFinder Adoption Prediction Dataset**을 활용하여  
동물의 특성 정보를 기반으로 유사한 동물을 추천하는 시스템을 구현하였다.

Content-Based Recommendation 방식으로 Cosine Similarity를 활용하여
가장 유사한 동물 Top‑K를 추천한다.

---

## 📂 Dataset
Kaggle Competition Dataset:
https://www.kaggle.com/competitions/petfinder-adoption-prediction/data

주요 컬럼:
- Type (동물 종류)
- Breed1 (품종)
- Gender (성별)
- Age (나이)
- MaturitySize
- FurLength
- Vaccinated
- Dewormed
- Sterilized
- Health
- Color1

---

## ⚙️ Data Processing
1. Feature 선택
2. 결측치 처리 (fillna)
3. One‑Hot Encoding (pd.get_dummies)
4. StandardScaler 정규화
5. Cosine Similarity 계산

---

## 🧠 Recommendation Logic
유사도 높은 순으로 정렬 후 자기 자신을 제외하고 Top‑K 추천을 수행한다.

---

## 📊 Example
recommend_pet(0)

동일한 종(Type)과 유사한 특성을 가진 동물이 추천되는 것을 확인하였다.

---

## 💡 Improvement Ideas
- BreedLabels.csv를 활용하여 품종 ID → 품종명 변환
- Similarity Score 출력
- Streamlit 기반 웹 서비스 확장

