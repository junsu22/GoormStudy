# 학생들의 이름과 점수를 key와 value로 가지는 score 변수를 생성하세요.
# 하준 90점, 서윤 86점, 지아 80점
# [출력]
# {'하준': 90, '서윤': 86, '지아': 80}
score = {"하준": 90, "서윤": 86, "지아" : 80}

print(score)

# score 변수에 수지 95점을 추가하세요.
score["수지"] = 95 # append 로 추가해야 하는건지 좀 헤맴
print(score)

# score 변수에서 지아를 삭제하세요.(틀림. pop 을 떠올리지 못함. dictonary 아직 제대로 이해를 못한거 같음.)
score.pop("지아")
print(score)

# score 변수에 기창 98점, 남철 60점, 기성 75점을 한번에 추가하세요.
# update() 를 사용하세요
score.update({"기창": 98, "남철": 60, "기성" : 75}) # pop 메서드 써 보고 감 잡힘.
print(score)



