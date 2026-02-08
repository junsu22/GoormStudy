# 하노이의 탑을 재귀 알고리즘을 이용해서 구현하고 예시코드와 비교해보세요
"""
반복문 을 이용하여 해결하기 어려운 문제를 재귀 알고리즘으로 푸는 방법
한번에 한 판만 옮긴다 . 큰 원판이 작은 원판 위로 올 수없다.

4개 원판 > 3개 한번에 > 큰원판 최종 목적지 > 3개 옮기기 >완성
"""


def move_tower(height, from_pole, to_pole, with_pole):
    # height : 옮길원 판의 개수 , from_pole: 출발기둥, to_pole 목적지 기둥, with_pole : 보조 기둥
    if height >= 1:  # 원판이 1개 이상이면
        move_tower(
            height - 1, from_pole, with_pole, to_pole
        )  # (n -1)개의 원판을 보조 기둥으로 옮기기
        move_disk(from_pole, to_pole)  # 탑 원판 옮기기(가장 큰 원판을 목적지로 옮기기)
        move_tower(
            height - 1, with_pole, to_pole, from_pole
        )  # 보조 기둥의(n-1)개 원판을 목적지로 옮기기


def move_disk(from_p, to_p):
    print(f"{from_p} 에서 {to_p}로 탑 원판 옮기기")


# 실행 예시
if __name__ == "__main__":  # 이 파일이 직접 실행 될 떄 아래 코드를 실행
    print("하노이의 탑 (4개 원판)")
    print("=" * 40)  # "=================="
    move_tower(4, "A", "B", "C")

"""
하노이의 탑 (4개 원판)
========================================
A 에서 C로 탑 원판 옮기기
A 에서 B로 탑 원판 옮기기
C 에서 B로 탑 원판 옮기기
A 에서 C로 탑 원판 옮기기
B 에서 A로 탑 원판 옮기기
B 에서 C로 탑 원판 옮기기
A 에서 C로 탑 원판 옮기기
A 에서 B로 탑 원판 옮기기
C 에서 B로 탑 원판 옮기기
C 에서 A로 탑 원판 옮기기
B 에서 A로 탑 원판 옮기기
C 에서 B로 탑 원판 옮기기
A 에서 C로 탑 원판 옮기기
A 에서 B로 탑 원판 옮기기
C 에서 B로 탑 원판 옮기기
"""
