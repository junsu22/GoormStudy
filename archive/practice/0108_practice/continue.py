# 반복문의 중첩
for i in range(1, 4):
    for j in range(1, 4):
        print(f'(i={i})+ (j = {j}) = {i *j}')
        print('===')

# 제어문 
# countinue
# 반복문 내부에서 continue 구문은 해당 루프(loop) 를 건너 뛰게 한다.
# continue 라는 구문을 만나면, 반복문에서 continue 아래 작성된 코드는 실행되지 않고 건너 뜀.
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 반복문과 조건문 그리고 continue 를 활용하여 짝수만 출력하라. 
for i in mylist:
    if i % 2 ==1:
        continue
    print(i)

# break 루프는 즉시 종료.
# break 를 사용하여  i 가 6 이상이면 stop
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in mylist:
    if i >=6:
        break
    print(i)

# break , continue 사용법
# for i in range(10):
#     if i == 5:
#         break 를 하게 되면 4 까지만 출력되지만 5랑 같아지면 중단으로 


# for i in range(10):
#     if i == 5:
#         continue # 0 부터 9까지 출력. 총 열개를 만들었기 때문에 5와 같아져도 이어서 끝까지 다 만들게 된다. 
#     print(i)
