


# 1 끝에 엑스맨 을 추가하세요
movie =  ['어벤져스', '아이언맨', '토르', '스파이더맨']
movie.append('엑스맨')
print(movie)

# 2 movie 1번 index 에 데드풀을 추가
movie = ['어벤져스', '아이언맨', '토르', '스파이더맨', '엑스맨']
movie.insert(1, '데드풀')
print(movie)

# 3 movie에서 아이언맨을 삭제 하세요.
movie = ['어벤져스', '데드풀', '아이언맨', '토르', '스파이더맨', '엑스맨']
movie.remove('아이언맨')
print(movie)

# 4 kr_movie = ['승리호', '신세계', '타짜']
movie = ['어벤져스', '데드풀', '토르', '스파이더맨', '엑스맨']
kr_movie = ['승리호', '신세계', '타짜']
movie = movie+kr_movie
print(movie)



#5 movie를 가나다 순으로 정렬하세요
movie = ['어벤져스', '토르', '스파이더맨', '엑스맨', '승리호', '신세계', '타짜']
movie.sort()
print(movie)



