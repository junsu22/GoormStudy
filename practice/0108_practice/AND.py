# AND
# 모든 조건이 참 일때 True 아니면 다 false

if (0<1) and (0<2):
    print('모두 참')
else:
    print('거짓')

if (0<1) and (0>2):
    print('모두 참')
else:
    print('허참')


# OR
# 조건 중 하나라도 만족할때 참으로 인식

if(0<1) or (1<0):
    print('하나라도 참')
else:
    print('허참')


if(10<1) or (1<0):
    print('하나라도 참')
else:
    print('허참')


# NOT
# bool 을 반전
if not True:
    print('not True')

if not False:
    print("not false")