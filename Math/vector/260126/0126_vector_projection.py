# 일반 파이썬에서는 실행되지 않으며, SageMath 환경에서 실행함


# 3차원 벡터 내적
v = vector([1, 2, 3])
w = vector([4, 5, 6])

v.dot_product(w)


# 4차원 벡터 정사영
a = vector([1, 2, 3, 4])
x = vector([4, 3, 2, 1])

proj = (x.dot_product(a) / a.dot_product(a)) * a
proj
