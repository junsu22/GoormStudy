# 프랙탈 트리 구현을 터틀 모듈을 이용해서 구현하세요

import turtle


# branch_length: 가지의 길이
# t: 터틀 객체


def draw_tree(branch_length, t):
    # 재귀 종료 조건: 가지가 너무 작아지면 멈춤
    if branch_length > 5:  # 가지 길이가 5보다 크면 계속 그리기
        # 가지 그리기
        t.forward(branch_length)

        # 오른쪽 가지 그리기
        t.right(20)  # 오른쪽으로 20도 회전
        draw_tree(branch_length - 15, t)  # 재귀호출 (가지 길이 줄이기)

        # 왼쪽 가지 그리기
        t.left(40)  # 왼쪽으로 40도 회전 (20도 되돌리기 + 20도 더)
        draw_tree(branch_length - 15, t)  # 재귀호출

        # 원래 위치로 돌아가기
        t.right(20)  # 각도 원위치
        t.backward(
            branch_length
        )  # 뒤로 이동, 원래 위치로 돌아와야 다음 가지 그릴 수 있음


# 실행 예시
if __name__ == "__main__":
    # turtle 설정
    my_turtle = turtle.Turtle()
    my_window = turtle.Screen()

    my_turtle.left(90)  # 거북이를 위쪽으로 향하게
    my_turtle.up()  # 펜 들기
    my_turtle.backward(100)  # 아래쪽으로 이동 (시작 위치 조정)
    my_turtle.down()  # 펜 내리기
    my_turtle.color("green")  # 초록색

    # 프랙탈 트리 그리기
    draw_tree(75, my_turtle)  # 초기 가지 길이 75

    my_window.exitonclick()  # 클릭하면 종료
