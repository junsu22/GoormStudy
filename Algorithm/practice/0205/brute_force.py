# 브루트 포스 비번 찾기(크래킹)
# 4자리 숫자
# 모든 경우의 수를 하나씩 시도한다.


def brute_force_crack(target_password):
    attemps = 0  # 시도횟수

    # 0000~9999 까지의 모든 경우의 수 시도
    for i in range(10000):
        attemps += 1
        guess = str(i).zfill(4)  # 4자리 문자열로 변환. (앞에 0으로 채우기)

        # 1000번 마다 진행상황 출력하기
        if attemps % 1000 == 0:
            print(f"찾는 중 {guess}")

        # 비밀번호가 일치
        if guess == target_password:
            print(f"\n찾음!!!!")
            print(f"찾은번호 : {guess}")
            print(f"시도 수 : {attemps}")
            return guess  # 찾으면 바로 종료
    # 범위가 4자리이기 때문에 사실상 출력될일 없음
    print("찾지 못했습니다.")
    return None


# 실행예시
if __name__ == "__main__":
    secret_password = "5244"

    print(f"크래킹 시작!")
    print(f"목표 :  {secret_password}")
    print("-" * 40)

    brute_force_crack(secret_password)

"""
크래킹 시작!
목표 :  5244
----------------------------------------
찾는 중 0999
찾는 중 1999
찾는 중 2999
찾는 중 3999
찾는 중 4999

찾음!!!!
찾은번호 : 5244
시도 수 : 5245


"""
