# 파이썬 지원 자료형
'''
int : 정수
float : 실수
complex : 복소수
bool : 불린   참 거짓 
str : 문자열(시퀀스)   
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전
'''

# 데이터 타입
float = 10.0
int = 7
str1 = "Python"
bool = True
list = [str1, int]      # 배열과 매우 유사
dict = {
    "name": "Machine Learning",
    "version": 2.0
}
tuple = 3, 5, 7
set = {7, 8, 9}

# 데이터 타입 출력
print(type(str1))
print(type(bool))
print(type(bool))
print(type(float))
print(type(int))
print(type(dict))
print(type(tuple))
print(type(set))
print()

# 함수
def add(a, b):
    return a+b

# 출력
print(add(10, 20))
print()

# for문
for a in [1, 2, 3]:
    print(a)

# --------------------------------------------------------------


