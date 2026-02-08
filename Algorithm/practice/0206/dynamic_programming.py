# DP의 상향식, 하향식 구조의 차이에 따른 구현방식을 정리하고 재귀적 알고리즘을 예시로 구현해보세요 (피보나치 제외)

"""상향식 접근법 : 가장작은 하위 문제들로부터 시작하여 점차적으로 큰 문제로 나아가는 방식
일반적으로 작은 반복문을 사용하여 구현, 작은 문제의 해를 테이블에 저장하며 진행

하향식접근법 : 큰 문제를 시작하여 필요한 작은 문제로 나누어 가는 방식 . 일반적으로 재귀호출을 사용하며 메모이제이션을 통해
이미 해결한 문제를 저장하여, 중복계산을 방지.
"""
import sys

sys.setrecursionlimit(15000)  # 임시 방편 : 15000으로 늘리기
# 파이썬의 기본 재귀 깊이는 1000이다.


# 예시 문제: 동전 거스름돈 (Coin Change)
# 주어진 동전들로 특정 금액을 만들 때 필요한 최소 동전 개수는?
# 1. 하향식 (Top-Down) - 재귀 + 메모이제이션
def coin_change_top_down(coins, amount, memo=None):
    """
    coins: 사용 가능한 동전 리스트
    amount: 만들어야 할 금액
    memo: 메모이제이션용 딕셔너리
    """
    if memo is None:
        memo = {}  # 재사용을 위해 만듬

    # 기저 조건
    if amount == 0:  # 0원 만들기: 동전 0개 필요
        return 0
    if amount < 0:  # 0보다 작을 수는 없다.(음수는 존재하지 않음)
        return float("inf")

    # 이미 계산했으면 저장된 값 반환
    if amount in memo:  # 동전을 앞에서 만든 딕셔너리에 담아
        return memo[amount]  # 반환

    # 모든 동전에 대해 시도
    min_coins = float(
        "inf"
    )  # 처음에 금액을 알 수 없기 때문에 무한대로 설정(무한대보다 큰 수는 없다)
    for coin in coins:
        # 현재의 동전을 하나 사용하면, 남은 금액을 만드는데 몇 개가 필요할까?
        # 재귀, 현재의 동전(coin)을 하나 사용했으니 남은금액(amount - coin)
        # 을 만들 때 몇 개가 필요할까?
        result = coin_change_top_down(coins, amount - coin, memo)
        # 만들 수 있는 금액만
        if result != float("inf"):  # 불가능
            min_coins = min(min_coins, result + 1)  # +1은 현재 동전

    # 결과 저장
    memo[amount] = min_coins
    return memo[amount]


# 2. 상향식 (Bottom-Up) - 반복문 + 테이블
# 상향식을 재귀로 사용하게 되면
# 순차적 계산을 하기 때문에 재귀를 사용하게 되면 코드가 복잡해진다.
# 상향식에는 되돌아갈 필요없이 반목문을 사용하는것이 효과적이다.
def coin_change_bottom_up(coins, amount):
    """
    coins: 사용 가능한 동전 리스트
    amount: 만들어야 할 금액
    """
    # DP 테이블 초기화 (0원부터 amount원까지)
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0  # 0원 만들기: 동전 0개

    # 1원부터 amount원까지 차례대로 계산
    for i in range(1, amount + 1):
        # 각 동전에 대해 시도
        for coin in coins:
            if i - coin >= 0:  # 동전을 사용할 수 있으면
                # i원 = min(기존값, (i-coin)원 + 1개)
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # 만들 수 없으면 -1 반환
    return dp[amount] if dp[amount] != float("inf") else -1


# 실행 예시
if __name__ == "__main__":
    coins = [10, 100, 1000, 10000]  # 10원, 100원, 1000원, 10000원
    amount = 12340  # 12340원 만들기

    print(f"{amount}원 거스름돈 (동전: {coins})")
    print("=" * 40)

    # 하향식
    result_top_down = coin_change_top_down(coins, amount)
    if result_top_down == float("inf"):
        print("하향식(재귀): 만들 수 없음")
    else:
        print(f"하향식(재귀): 최소 {result_top_down}개")

    # 상향식
    result_bottom_up = coin_change_bottom_up(coins, amount)
    if result_bottom_up == -1:
        print("상향식(반복): 만들 수 없음")
    else:
        print(f"상향식(반복): 최소 {result_bottom_up}개")

    print("\n계산 과정 (12340원):")
    print("10000원 × 1 = 10000원")
    print("1000원 × 2 = 2000원")
    print("100원 × 3 = 300원")
    print("10원 × 4 = 40원")
    print("총 10개 동전")

"""

12340원 거스름돈 (동전: [10, 100, 1000, 10000])
========================================
하향식(재귀): 최소 10개
상향식(반복): 최소 10개

계산 과정 (12340원):
10000원 × 1 = 10000원
1000원 × 2 = 2000원
100원 × 3 = 300원
10원 × 4 = 40원
총 10개 동전

"""
