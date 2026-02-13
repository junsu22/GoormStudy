# 이상탐지
# 협업 필터링
"""
dataset : Movielens 100k
https://grouplens.org/datasets/movielens/

u.data = 평점 데이터
u.item = 영화 정보
u.user = 유저 정보 (안 씀)
u1.base, u1.test 등 = train/test 분할 (안 씀)
"""


# 라이브러리 호출 ===================================

import pandas as pd
import numpy as np
from google.colab import files

# cosine_similarity
# 코사인 유사도 호출 / 두 벡터 사이의 각도로 유사도를 측정
# 값 : -1 ~ 1 (1에 가까울수록 비슷하다.)
# 용도 : 비슷한 취향의 유저가 좋아한 영화를 추천
from sklearn.metrics.pairwise import cosine_similarity  # 협업 필터링

# IsolationForest
# 다수와 다른패턴 (이상치) , ex.평균 평점 높은데 평가 적은 유저
from sklearn.ensemble import IsolationForest  # 이상탐지용

# 사이킷런에서 경고(알림) 끄기. 실행하는데 지장없음.깔끔하게 결과를 보기위해
import warnings

warnings.filterwarnings("ignore")
# =======================================================


# 데이터 로드 =============================================

print("=" * 50)
print("데이터 로드 중 (MovieLens 100k)")
print("=" * 50)

# 파일업로드 (코랩 실행시)
uploaded = files.upload()  # 안하면 파일 업로드 버튼이 안나옴

# u.data 로드 (ratings, 탭 구분)
# u.data 파일을 ratings 데이터 프레임으로 읽기
ratings = pd.read_csv(
    "u.data",
    sep="\t",  # 탭으로 나눈다
    names=[
        "userId",
        "movieId",
        "rating",
        "timestamp",
    ],  # 유저번호, 영화번호, 평점, 평가한 시간
)

# 테스트용 데이터 축소 (계산 속도 향상)
# 전체 943명 → 100명으로 축소 (제출 시 삭제 또는 943으로 변경)
print(f"원본: {ratings.shape}")
ratings = ratings[ratings["userId"] <= 100]
print(f"축소: {ratings.shape}")

# u.item 로드 (| 구분)
movies = pd.read_csv(
    "u.item",
    sep="|",  # 파이프로 나눈다
    encoding="latin-1",  # 특수문자 깨짐 방지
    names=[
        "movieId",
        "title",
        "release_date",
        "video_release_date",
        "imdb_url",
        "unknown",
        "Action",
        "Adventure",
        "Animation",
        "Children",
        "Comedy",
        "Crime",
        "Documentary",
        "Drama",
        "Fantasy",
        "Film-Noir",
        "Horror",
        "Musical",
        "Mystery",
        "Romance",
        "Sci-Fi",
        "Thriller",
        "War",
        "Western",
    ],
    usecols=["movieId", "title"],  # 필요한 컬럼만 (movieId, title)
)
# =======================================================


# 협업필터링 기반 추천시스템 =============================

print("\n" + "=" * 50)  # 줄바꿈 + ====
print("협업 필터링 기반 추천 시스템 구현")
print("=" * 50)

# User-Item Matrix 생성
# pivot_table : 유저별로 각 영화에 준 평점을 표 형태로 변환
user_item_matrix = ratings.pivot_table(
    index="userId",  # 행 (유저)
    columns="movieId",  # 열 (영화)
    values="rating",  # 값 (평점)
).fillna(
    0
)  # 결측값을 0으로 채움 (안 본 영화는 0점)

# fillna(0) 설명:
# - 코사인 유사도 계산시 NaN 데이터가 있으면 에러 발생
# - 안 본 영화는 0점으로 처리

print(f"\nUser-Item Matrix 크기 : {user_item_matrix.shape}")

# 유저 간 유사도 계산 (코사인 유사도)
# 각 유저의 평점 패턴이 얼마나 비슷한지 계산
user_similarity = cosine_similarity(user_item_matrix)
user_similarity_df = pd.DataFrame(
    user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index
)

print("유저 간 유사도 계산완료")


# 협업필터링 추천 함수 =====================================


def get_collaborative_recommendations(user_id, n_recommendations=5):
    """협업필터링 기반 추천 함수

    Args:
        user_id: 추천받을 유저 번호
        n_recommendations: 추천할 영화 개수

    Returns:
        추천영화 ID list
    """

    # 해당 유저가 없으면 빈 리스트 반환
    if user_id not in user_item_matrix.index:
        return []

    # 1. 유사한 유저들 찾기 (상위 10명)
    # sort_values(ascending=False) : 유사도가 높은 순으로 정렬
    # [1:11] : 자기 자신(0번째) 제외, 1~10번째 유저 선택
    similar_users = user_similarity_df[user_id].sort_values(ascending=False)[1:11]

    # 2. 타겟 유저가 본 영화 목록
    user_ratings = user_item_matrix.loc[user_id]
    watched_movies = user_ratings[user_ratings > 0].index  # 평점이 0보다 큰 영화들

    # 3. 유사 유저들이 높게 평가한 영화 중 타겟 유저가 안 본 영화 찾기
    recommendations = {}

    # 유사한 유저들을 순회
    for similar_user_id in similar_users.index:
        similar_user_ratings = user_item_matrix.loc[similar_user_id]

        # 유사 유저가 본 영화들 순회
        for movie_id in similar_user_ratings[similar_user_ratings > 0].index:
            # 타겟 유저가 안 본 영화만 추천 대상
            if movie_id not in watched_movies:
                if movie_id not in recommendations:
                    recommendations[movie_id] = 0
                # 가중치 = 평점 × 유사도
                # 유사도가 높은 유저의 평점에 더 큰 가중치
                recommendations[movie_id] += (
                    similar_user_ratings[movie_id] * similar_users[similar_user_id]
                )

    # 4. 상위 N개 추천
    # sorted() : 점수가 높은 순으로 정렬
    top_recommendations = sorted(
        recommendations.items(),
        key=lambda x: x[1],  # 점수 기준
        reverse=True,  # 내림차순
    )[
        :n_recommendations
    ]  # 상위 N개만

    return [movie_id for movie_id, score in top_recommendations]


# 테스트: User 1에게 추천
test_user = 1
collab_recs = get_collaborative_recommendations(test_user, n_recommendations=10)

print(f"\n협업필터링 - User {test_user}에게 추천하는 영화:")
for i, movie_id in enumerate(collab_recs, 1):
    # 영화 ID로 영화 제목 찾기
    movie_title = movies[movies["movieId"] == movie_id]["title"].values
    if len(movie_title) > 0:
        print(f"{i}. {movie_title[0]}")


# 협업 필터링 정리
# - 나와 비슷한 사람들이 좋아한 영화 추천
# - 코사인 유사도로 유사 유저 찾기
# - 예: User A, B, C가 스타워즈를 좋아함 → 취향이 비슷한 사람들 → 스타워즈 추천


# 이상탐지 정리
# - 독특한 취향을 가진 유저들이 좋아한 영화 추천
# - 평균 평점이 높은데 평가가 적은 유저 등
# - 완전히 다른 방법론


# 이상탐지 시스템 ==========================================

print("\n" + "=" * 50)
print("이상탐지 기반 추천시스템")
print("=" * 50)

# 각 유저의 평가 패턴을 특징으로 사용
user_features = []  # 유저별 특징을 저장할 리스트
user_ids = []  # 유저 ID를 저장할 리스트

# 모든 유저에 대해 특징 추출
for user_id in user_item_matrix.index:
    user_ratings = user_item_matrix.loc[user_id]
    rated_movies = user_ratings[user_ratings > 0]  # 평가한 영화들만

    # 최소 10개 이상 평가한 유저만 (데이터 신뢰성)
    if len(rated_movies) >= 10:
        features = [
            rated_movies.mean(),  # 평균 평점
            rated_movies.std(),  # 표준편차 (평점 변동성)
            len(rated_movies),  # 평가한 영화 수
            (rated_movies >= 4).sum(),  # 높은 평점(4~5점) 개수
            (rated_movies <= 2).sum(),  # 낮은 평점(1~2점) 개수
        ]
        user_features.append(features)
        user_ids.append(user_id)

# DataFrame으로 변환
user_features_df = pd.DataFrame(
    user_features,
    columns=["mean_rating", "std_rating", "n_ratings", "high_ratings", "low_ratings"],
)

print(f"\n유저 특징 데이터: {user_features_df.shape}")
print(user_features_df.head())

# Isolation Forest로 이상 유저 탐지
iso_forest = IsolationForest(
    contamination=0.1,  # 전체의 10%를 이상치로 간주
    random_state=42,  # 재현성 (같은 결과)
)
# fit_predict : 학습과 예측을 동시에 수행
# -1 = 이상치(독특한 유저), 1 = 정상
anomaly_labels = iso_forest.fit_predict(user_features_df)

# 이상 유저들 (독특한 취향)
# label이 -1인 유저들만 선택
anomaly_users = [user_ids[i] for i, label in enumerate(anomaly_labels) if label == -1]
print(f"\n이상 유저 (독특한 취향) 수: {len(anomaly_users)}")


# 이상탐지 기반 추천 함수
def get_anomaly_based_recommendations(user_id, n_recommendations=5):
    """이상탐지 기반 추천: 독특한 취향의 유저들이 좋아하는 영화 추천

    Args:
        user_id: 추천받을 유저 번호
        n_recommendations: 추천할 영화 개수

    Returns:
        추천영화 ID List
    """

    # 해당 유저가 없으면 빈 리스트 반환
    if user_id not in user_item_matrix.index:
        return []

    # 타겟 유저가 본 영화
    user_ratings = user_item_matrix.loc[user_id]
    watched_movies = user_ratings[user_ratings > 0].index

    # 이상 유저들이 높게 평가한 영화들
    anomaly_recommendations = {}

    # 이상 유저들 순회
    for anomaly_user in anomaly_users:
        if anomaly_user in user_item_matrix.index:
            anomaly_user_ratings = user_item_matrix.loc[anomaly_user]
            # 4점 이상 준 영화들만
            high_rated = anomaly_user_ratings[anomaly_user_ratings >= 4.0]

            # 높게 평가한 영화들 순회
            for movie_id in high_rated.index:
                # 타겟 유저가 안 본 영화만
                if movie_id not in watched_movies:
                    if movie_id not in anomaly_recommendations:
                        anomaly_recommendations[movie_id] = 0
                    # 평점 누적 (이상 유저들의 평점 합산)
                    anomaly_recommendations[movie_id] += high_rated[movie_id]

    # 상위 N개 추천
    top_recommendations = sorted(
        anomaly_recommendations.items(),
        key=lambda x: x[1],  # 점수 기준
        reverse=True,  # 내림차순
    )[:n_recommendations]

    return [movie_id for movie_id, score in top_recommendations]


# 테스트: 유저1에게 추천
anomaly_recs = get_anomaly_based_recommendations(test_user, n_recommendations=10)

print(f"\n이상탐지 기반 - User {test_user}에게 추천하는 영화 (독특한 취향):")
for i, movie_id in enumerate(anomaly_recs, 1):
    # 영화 ID로 영화 제목 찾기
    movie_title = movies[movies["movieId"] == movie_id]["title"].values
    if len(movie_title) > 0:
        print(f"{i}. {movie_title[0]}")


# ==== 결과 비교 ====
# 협업필터링: 대중적 영화 (Batman, Speed, Tombstone)
# 이상탐지: 참신한 영화 (Rear Window, Casablanca, It's a Wonderful Life)
# → 두 방법론의 차이가 명확히 드러남


"""
실행 결과:

==================================================
데이터 로드 중 (MovieLens 100k)
==================================================
원본: (100000, 4)
축소: (10638, 4)

==================================================
협업 필터링 기반 추천 시스템 구현
==================================================

User-Item Matrix 크기 : (100, 1450)
유저 간 유사도 계산완료

협업필터링 - User 1에게 추천하는 영화:
1. Schindler's List (1993)
2. Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb (1963)
3. Stand by Me (1986)
4. E.T. the Extra-Terrestrial (1982)
5. Batman (1989)
6. One Flew Over the Cuckoo's Nest (1975)
7. Heathers (1989)
8. True Lies (1994)
9. Speed (1994)
10. Tombstone (1993)

==================================================
이상탐지 기반 추천시스템
==================================================

유저 특징 데이터: (100, 5)
   mean_rating  std_rating  n_ratings  high_ratings  low_ratings
0     3.610294    1.263585        272           163           53
1     3.709677    1.030472         62            40            5
2     2.796296    1.219026         54            15           24
3     4.333333    0.916831         24            19            1
4     2.874286    1.362963        175            58           64

이상 유저 (독특한 취향) 수: 10

이상탐지 기반 - User 1에게 추천하는 영화 (독특한 취향):
1. Schindler's List (1993)
2. One Flew Over the Cuckoo's Nest (1975)
3. Rear Window (1954)
4. Casablanca (1942)
5. Titanic (1997)
6. To Kill a Mockingbird (1962)
7. E.T. the Extra-Terrestrial (1982)
8. Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb (1963)
9. True Lies (1994)
10. It's a Wonderful Life (1946)
"""
