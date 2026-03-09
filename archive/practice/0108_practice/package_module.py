# <!-- 함수 변수 클래스 들이 뭉쳐진 하나의 py 파일 안에 이루어진 것을 모듈이라고 함.
# 여러개의 모듈 이 모여 패키지
# 라이브러리는 패키지와 모듈의 집합체 -->

import random

a = [1, 2, 3, 4, 5]
# random 모듈의 shuffle 함수를 실행
random.shuffle(a)


# import 모듈을 rd 별칭 (alias) 지정 
import random as rd
# 계속 random. / random. /rd 이런식으로 불러오기 방지
# 전체 모듈을 가져와서 alias 지정하는 식으로 많이 사용 

b = [1, 2, 3, 4, 5]



# 파이썬에서 주로 많이 쓰이는 모듈

# numpy : 과학분석을 위한 패키지
# pandas : 데이터 분석을 할때 가장 많이 쓰이는 모듈
# matplotlib : 시각화를 위한 모듈
# seaborn : 시각화를 위한 모듈 (mataplotlib을 더 쉽게 사용할 수 있도록 도와주는 패키지)
# random : 난수생성 관련 모듈 