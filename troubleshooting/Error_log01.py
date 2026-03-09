# 1 각 변수의 타입을 출력하라 
a = 10
print(type(a))
b = 10.0
print(type(b))
c = '10'
print(type(c))
d = True
print(type(d))


# 2 x를 출력하고, 이 값이 언제쓰이는지 설명
x = None
print(x) # 값이 아직없음 

# 3 (1) 첫 글자 출력, (2) 마지막글자 출력
word = "Python"
print(word[0])
print(word[-1])

# 4 "velop"만 슬라이싱으로 출력하라
word = "developer"
print (word[2:7])

# 5 (1)앞뒤 공백 제거, (2)전부 소문자 출력 (3)결과 출력
# 감은 오지만 문법이 기억나지 않아 구글링 하고 옴. (AI 사용안하기!)
text = "      Python Study      "
print(text.strip()) # 문제의도는 strip , 검색해온 건 replace (" ","") 공백을 다지워 버리는 차이가 있다!
print(text.lower())
print(text.upper())

# 6 010-1234-5678 형태로 출력
# 문법이 헷갈려 검색해서 풀음
tel = ['010', '1234', '5678']
print('-'.join(tel))

# 7 
# "01" 로 시작하는지 출력
# ".png" 로 끝나는지 출력

file = "01_profile.png"
print(file.startswith("01"))
print(file.endswith(".png"))

# 8 
# 4, 5 를 순서대로 추가한 뒤 출력하라
nums = [1, 2, 3]
nums.append(4) # ([4, 5]) 로 하면 리스트 안에 리스트가 들어감
nums.append(5) 
print(nums)

# 9
# (1) 오름차순 정렬 결과 출력(원본유지)
# (2) 내림차 순 정렬 결과 출력 
nums = [3, 1, 5, 2, 4]
nums.sort() # 오름차순 정렬(원본 변경)
print(nums)
nums.reverse() # 현재 리스트를 뒤집음 (내림차순 효과)
# 원본 유지를 요구한 문제 의도와는 다름 (이 부분에서 헷갈림)
print(nums)

# 10 
# sorted() 사용 결과 출력
# 원본 리스트 출력

nums = [5, 2, 4, 1]
nums_sorted = sorted(nums) # 문법이 sort 와 비슷하겠다 싶어 풀다 안풀려서 검색, 변수 추가, 실질적인 데이터 안바뀜
print(nums_sorted) # 문제에서 요구하는건 두가지였는데, 이부분을 안했었음.
print(nums)

# 11
# 50출력
# 20을 99로 변경
# 전체 리스트 출력
box = [[10, 20, 30],[40,50,60]]
print(box[1][1]) 
# [1],[1]로 작성해서 오류가 났음 (연결되지 않음)
# 중첩 리스트는 box[행][열] 형태로 접근해야 함
# 꼭 다시 풀어볼 필요 있음

# 12 
# 각 숫자의 제곱 리스트를 만들어 출력하라
# 이상한 문법 만들다가 결국 못풀었다.
nums = [1, 2, 3, 4, 5] # 문제 코드
result = []

for n in nums:
    result.append(n * n)

print(result)

# 종료하려는데 에러가 해결되지 않아 당황
# SyntaxError: invalid syntax
# >>> 상태 
# 커맨드를 몰라서 한참 헤메다가 ctrl+z 눌렀더니 겨우 빠져 나왔다... 
