# 기본 조건문 if else
x = 10

if x > 5 :
    print("x는 5보다 큽니다.")
else:
    print("x는 5 이하입니다.")


# if ellip else 여러조건

score = 80

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C") 
else:
    print("D")  


# 비교 연산자

num = 0

if num > 0:
    print("양수")
elif num < 0:
    print("음수")
else:
    print("0")

# 논리연산 (AND) 모든 조건이 True 

age = 19
has_id = True

if age >= 20 and has_id:
    print("성인 인증 완료")
else:
    print("인증에 실패 하였습니다.(미성년자) ")  


# 논리연산 (OR) 둘 중 하나라도 True
is_weekend =  True
is_holiday = False

if is_weekend or  is_holiday:
    print("오늘은 쉬는 날 ! ")
else:
    print("오늘도 화이팅!") 



# 논리연산 NOT

is_raining = False

if not is_raining : 
    print("우산 안 챙겨도 됌")
else:
    print("우산 챙겨야 함.")

# 복합 조건 (and + or)

age = 17
has_ticket  = True

if(age >= 19 and has_ticket) or age >= 65:
    print("입장 가능")
else:
    print("입장 불가")



# input + 조건문 

num = int(input("숫자를 입력 하세요. : "))
if num % 2 == 0 :
    print("짝수입니다.")
else:
    print("홀수입니다.") 



