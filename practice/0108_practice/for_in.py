# 순회 가능한 객체 이터러블 객체


# for 와 in 구문 (반복문)
# for 하나씩 꺼내올 변수 in [꺼내올 집합]:
# lsit , tuple, set, dictionary ,문자열 형태 모두가능
# range 와 결합 하여 사용 가능 


mylist = [1, 2, 3, 4, 5]

for i in mylist:
    print(i)

    # 튜플 + list
    person = ('제이콥스',10)
    print(person)
    print(person[0])
    print(person[1])



# tuple의 요소를 개별로 받아주는 경우
name, age = ('제이콥스', 10)
print(name)
print(age)


# 반복문에서의 활용
mytuplelist = [('제이콥스', 10),('피터', 20),('타이거',30)]
for mytuple in mytuplelist:
    print(mytuple[0],mytuple[1])

# 방법2 
mytuplelist = [('제이콥스', 10), ('피터', 20),('타이거',30)]
for name, age in mytuplelist: # 이게 좀 더 깔끔한 방식
    print(name, age)     

# 딕셔너리
mydict = {'헐크': 50, '아이언맨': 60, '펭수': 70}
for key in mydict.keys():
    print(key)
for value in mydict.values():
    print(value)
for name, age in mydict.items():
    print(name, age)  

# 문자열
for c in "Hello":
    print(c)
