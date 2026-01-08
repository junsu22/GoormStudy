# while 문은 while문과 함꼐 정의한 조건이 참인 동안 반복 루프를 수행

count = 5

while count > 0 :
    print(count)
    count -= 1


# 많이 사용하는 방법 중 하나 while True 로 지정하여
# 무한 루프를 생성 후 
# 탈출 구문 루프내에서 설정  

# 내 생각 정리 : for 정해진 반복, while 무한루프 ..? 
# 개념 : 조건이 참인경우 계속 실행

count = 1
while True:
    print(count)
    count+= 1
    # 탈출 구문(break)
    if count > 5: 
        break

    