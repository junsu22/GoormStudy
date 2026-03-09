# lamda : 익명함수 
# 이름없이 정의된 함수
# 단일문장 1줄의 코드로 작성되어야 함
# 함수 내부에서는 return 문이 포함하지 않지만 값을 반환


# 단일 인수를 가지는 lambda 
a = lambda x : x * 2

# 2개의 인수를 가지는 lambda 
a = lambda x, y : x * y
a(4, 8)

# 기본 값이 지정된인수를 가지는 lamda
a = lambda x, y = 10: x*y
a(3)


# 기본 값이 지정된 인수를 가지는 lamda
a = lambda x, y : x * y
a(3)

# 키워드 인수를 지정하는 lamda 함수
a(y=5, x=3)

# lambda 함수 내부에서 조건문 사용
a = lambda x, y: x * y if x > 0 else y
a(4, 8) # 32
a(-1, 8) # 8

# elif 구문 억지 생성가능하나, 복잡한 조건문을 사용하기 위해서는 일반 함수 권장



