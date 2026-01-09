# 반복문
# for + range()

for i in range(5):
    print(i)


# for , range (start:end)
for i in range(1, 6):
    print(i)

# for list
nums = [1, 2, 3, 4, 5]

for n in nums:
    print(n)



# for character
word = "Junsu"

for ch in word:
    print(ch)


# for if else

nums = [1, 2, 3, 4, 5]

for n in nums:
    if n % 2 == 0:
        print(n, "짝")
    else:
        print(n, "홀")


# while 

count = 0

while count< 5:
    print(count)
    count += 1


# while + 조건 부 종료
num = 1

while num <= 10: # 10 도달 하면 반복 종료
    print(num)
    num += 1    


# break 

for i in range(10):
    if i == 5: # 5가 직전
        break   #종료
    print(i)


# continue

for i in range(5): # [0] ~ [4] 5개의 리스트를 만들어서
    if i == 2:  # 반복을 2 씩 건너 뜀
        continue   
    print(i)


# 0을 입력하면 종료

while True:
    num = int(input("숫자를 입력하세요. (0을 입력하면 종료)"))

    if num == 0:
        print("종료되었습니다.")
        break
    print("입력한 값 : ", num)