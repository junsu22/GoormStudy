
# sample1 에 6 추가
sample1 = {1, 2, 3, 4, 5}
sample2 = {2, 4, 5, 6, 7}

sample1 = set({1, 2, 3, 4, 5}) 
sample1.add(6) # set 문법 검색 


print(f'sample1: {sample1}')


# sample2에 2를 제거합니다.

sample2 = set({2, 4, 5, 6, 7}) # 혼자풀음
sample2.remove(2)
print(f'sample2: {sample2}')

# sample1과 sample2의 교집합을 출력합니다.
inter = set.intersection(sample1,sample2) # set 교집합 검색 , intersection 교집합
print(inter)


uni = set.union(sample1,sample2) # set 합집합 검색 , union 합집합
print(uni)

diff = set.difference(sample1,sample2) # set 차집합 검색 , difference 차집합
print(diff)


# 다음 리스트에서 중복된 항목을 제거하세요
# 최종 출력 값은 list 형태로 출력하세요
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numList = [1, 3, 2, 3, 7, 6, 8, 4, 10, 5, 3, 8, 9]
set_numList = set(numList)
list_numList = list(set_numList) # 많이 애먹음, 한줄차이인데 왜..? 리스트중복제거 검색, 문법 대조 해 가며 여러번 틀림 , 리스트 변환이 안돼서
print(list_numList)