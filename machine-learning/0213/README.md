# 🎬 Anomaly Detection Movie Recommendation

**협업 필터링 vs 이상탐지 기반 영화 추천 시스템 비교**

MovieLens 100k 데이터를 활용하여 두 가지 추천 알고리즘의 차이를 실험하고 비교한 프로젝트입니다.

---

## 📊 프로젝트 개요

### 🎯 목표
- **협업 필터링**: 나와 비슷한 취향의 사용자들이 좋아한 영화 추천
- **이상탐지**: 독특한 취향을 가진 사용자들이 높게 평가한 참신한 영화 추천

### 📈 주요 결과
- **협업 필터링**: 대중적이고 인기 있는 영화 추천 (Batman, Speed, Tombstone)
- **이상탐지**: 고전적이고 참신한 영화 추천 (Rear Window, Casablanca, It's a Wonderful Life)

---

## 🛠️ 기술 스택

### 🐍 Python Libraries
- **pandas**: 데이터 처리 및 분석
- **numpy**: 수치 연산
- **scikit-learn**: 
  - `cosine_similarity`: 협업 필터링용 유사도 계산
  - `IsolationForest`: 이상탐지 알고리즘

### 📊 데이터셋
- **MovieLens 100k**: 943명 사용자, 1,682개 영화, 100,000개 평점
- 실험용으로 100명 사용자로 축소하여 진행

---

## 🔍 구현 방법론

### 1. 협업 필터링 (Collaborative Filtering)
```python
# 사용자-아이템 매트릭스 생성
user_item_matrix = ratings.pivot_table(
    index="userId", columns="movieId", values="rating"
).fillna(0)

# 코사인 유사도로 유사 사용자 탐지
user_similarity = cosine_similarity(user_item_matrix)
```

**핵심 아이디어**: 나와 비슷한 평점 패턴을 가진 사용자들이 좋아한 영화를 추천

### 2. 이상탐지 기반 추천 (Anomaly Detection)
```python
# 사용자별 특징 추출
features = [
    rated_movies.mean(),     # 평균 평점
    rated_movies.std(),      # 표준편차
    len(rated_movies),       # 평가한 영화 수
    (rated_movies >= 4).sum(), # 높은 평점 개수
    (rated_movies <= 2).sum()  # 낮은 평점 개수
]

# Isolation Forest로 독특한 취향 사용자 탐지
iso_forest = IsolationForest(contamination=0.1)
```

**핵심 아이디어**: 독특한 평가 패턴을 가진 사용자들이 높게 평가한 영화를 추천

---

## 📈 실행 결과

### User 1에 대한 추천 결과

#### 🤝 협업 필터링 추천
1. Schindler's List (1993)
2. Dr. Strangelove (1963)
3. Stand by Me (1986)
4. E.T. the Extra-Terrestrial (1982)
5. Batman (1989)

#### 🔍 이상탐지 기반 추천  
1. Schindler's List (1993)
2. One Flew Over the Cuckoo's Nest (1975)
3. **Rear Window (1954)** ⭐
4. **Casablanca (1942)** ⭐
5. Titanic (1997)

**차이점**: 이상탐지는 고전 명작들을 더 많이 추천하는 경향



---

## 📚 학습 포인트

### 💡 협업 필터링의 특징
- **장점**: 대중적 취향 반영, 안정적인 추천
- **단점**: 인기 편향, 새로운 장르 발견 어려움

### 🔍 이상탐지의 특징  
- **장점**: 참신한 추천, 숨겨진 명작 발굴
- **단점**: 예측 불가능, 취향에 안 맞을 수 있음

### 🎯 실무 적용
- **서비스 초기**: 협업 필터링으로 안정적 추천
- **개인화 고도화**: 이상탐지로 다양성 추가
- **하이브리드**: 두 방법을 조합하여 균형 잡힌 추천

---

## 🔗 참고 자료

- [MovieLens Dataset](https://grouplens.org/datasets/movielens/)
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Isolation Forest Paper](https://cs.nju.edu.cn/zhouzh/zhouzh.files/publication/icdm08b.pdf)

---

