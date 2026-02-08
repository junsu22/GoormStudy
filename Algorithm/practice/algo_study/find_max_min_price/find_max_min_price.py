# 합리적 소비
"""
N 개의 물품의 물품과 가격이 주어짐
가장 비싼 물품과 가장 저렴한 물품을 찾아야 함.

N개의 물품을 하나씩 흝으면서 가장 낮은 가격과 높은 가격의 물품을 갱신해나가는 구현문제
시간복잡도 O(N)

"""
# input 함수 초기화
import builtins

input = builtins.input

# 상품 개수 입력
N = int(input("상품 개수: "))

# 상품명, 가격을 담을 리스트 초기화
name = []
price = []

# N개의 상품 정보 입력받기
print(f"{N}개의 상품 정보를 입력하세요 (형식: 상품명 가격)")
for i in range(N):
    line = input(f"{i+1}번째 상품: ")  # 한 줄 입력받기
    S, P = line.split()  # 공백으로 분리
    name.append(S)  # 상품명을 리스트 추가
    price.append(int(P))  # 가격 정수로 변환

# 첫번째 상품으로 최대/최소 초기화
ans_max_name = name[0]  # 최고가 상품명
ans_max_price = price[0]  # 최고가
ans_min_name = name[0]  # 최저가 상품명
ans_min_price = price[0]  # 최저가

# 두 번째 상품부터 비교 시작
for i in range(1, N):
    if price[i] > ans_max_price:  # 현재 가격이 최고가보다 크다면
        ans_max_name = name[i]  # 최고가 상품명을 갱신
        ans_max_price = price[i]  # 최고가 가격을 갱신
    if price[i] < ans_min_price:  # 현재 가격이 최저가보다 작다면
        ans_min_name = name[i]  # 최저가 상품명을 갱신
        ans_min_price = price[i]  # 최저가 가격을 갱신

# 결과 출력
print(f"\n최고가: {ans_max_name} {ans_max_price}원")
print(f"최저가: {ans_min_name} {ans_min_price}원")

"""
상품 개수: 5
5개의 상품 정보를 입력하세요 (형식: 상품명 가격)
1번째 상품: watch 2000
2번째 상품: scarf 1500
3번째 상품: boots 4000
4번째 상품: coat 10000
5번째 상품: perfume 7000

최고가: coat 10000원
최저가: scarf 1500원
"""
