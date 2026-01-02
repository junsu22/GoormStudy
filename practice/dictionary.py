"""
dictionary.py
딕셔너리(Dictionary) 기초 실습 파일

- key : value 구조
- 설정값(config) 관리에 자주 사용
"""

# 딕셔너리는 중괄호 {}로 만든다.
# config는 딕셔너리를 담는 변수다.
config = {
    "host": "localhost",
    "port": 8080,
    "debug": True
}

# key를 사용해 value에 접근한다.
print(config["host"])   # localhost
print(config["port"])   # 8080
print(config["debug"])  # True


# value는 변경할 수 있다.
config["port"] = 3000
print(config["port"])   # 3000


# 새로운 key-value 추가
config["version"] = "1.0"
print(config)


# key 목록 확인
print(config.keys())

# value 목록 확인
print(config.values())

# key와 value 쌍 확인
print(config.items())


# 존재하지 않는 key를 바로 접근하면 에러가 발생한다.
# print(config["password"])  # KeyError

# 안전하게 가져오는 방법
print(config.get("password"))        # None
print(config.get("password", "없음"))  # 기본값 설정
