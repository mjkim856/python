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

# shell에서는
'''
a=1
echo $a     1
echo a      a
echo "$a"   1
echo '$a'   $a
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
print("\n함수 출력 예시")
print(add(10, 20))

# for문
print("\nfor문과 list 예시")
for a in [1, 2, 3]:
    print(a)

# --------------------------------------------------------------

# 숫자 자료형
# + - * / //(몫) %(나머지) **(제곱)
print("\n숫자 자료형 실습")
print("1/2 =", 1/2)
print("1//2 =", 1//2)
print("1%2 =", 1%2)
print("2**4 =", 2**4)

# 형 변환 실습
a = 3.
b = 6
c = .7
d = 12.7

# 타입 출력
print("\n형 변환 실습")
print(type(a), type(b), type(c), type(d))

# --------------------------------------


