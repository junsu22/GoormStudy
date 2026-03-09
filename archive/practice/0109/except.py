# try - except 예외 처리 실습

# try 에러 날 수 있는 코드
# except 에러 났을때 실행
# finally 무조건 실행


# 1 Zerodivision (0으로 나누기)
try:
    x = 10
    y = 0 
    result = x / y
    print(result)
except ZeroDivisionError:
    print("Error : 0으로 나눌 수 없습니다.")



# 2 ValueError ( 형 변환 오류 )

try: 
    num = int("abc") # 문자형이므로 , 숫자로 변경이 불가하다.
    print(num)
except ValueError:
    print("Error : 숫자로 변환 할 수 없는 값입니다.")    


#3 IndexError (리스트 인덱스 초과)

try:
    nums = [1, 2, 3]
    print(nums[5])
except IndexError:
    print("Error : 인덱스 범위를 초과하였습니다.")


# 4 KeyError

try:
    data = {"a":1, "b":2}
    print(data["c"])
except KeyError:
    print("Error : 존재하지 않는 키 입니다.")


# 5 여러 예외 동시처리
try:
    x = int(input("숫자 입력 : "))
    result = 10 / x
    print(result)
except ValueError:
    print("Error : 숫자를 입력해야 합니다.") 
except ZeroDivisionError:
    print("Error : 0으로 나눌 수 없습니다.") 


# else / finally 사용

try:
    x = int(input("숫자 입력 : "))
    result  = 10 / x
except Exception as e:
    print("Error : 에러 발생", e)
else:
    print("실행 결과 : ", result) 
finally: # 무조건 실행 
    print("예외처리 종료 됨.")


# 모든 예외 잡기 (최후의 수단으로 권장)

try:
    lst = []
    print(lst[0])
except Exception as e:
    print("Error : 예외 발생", type(e),e)













