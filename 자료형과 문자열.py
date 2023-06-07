# 자료형, 구구단, 문자열, string, indexing 인덱싱 연습
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

print("\n빈 문자열 만들기\n변수 타입과 길이 출력")
b_str1 = ''
b_str2 = str()

print(type(b_str1), len(b_str1))
print(type(b_str1), len(b_str1))


# 문자열 연산
str_o1 = "Python "
str_o2 = "Apple"
str_o3 = "How are you doing?"
str_o4 = "Seoul Deajeon Busan Jinju"

print("\n문자열 연산")
print(3 * str_o1)
print(str_o1 + str_o2)
print(dir(str_o1))
print(len(str_o1))
print('y' in str_o1)
print('n' in str_o1)
print('P' not in str_o2)

# ip주소로만 시작해라(grep), 정렬해라(sort), 카운트해라(uniq), 20개 이상
# awk '{print $3}' lastb.txt | grep ^[0-9] | sort -n | uniq -c
# awk '{print $3}' lastb.txt | grep ^[0-9] | sort -n | uniq -c | awk '$1 >=20{print $0}'
# 이걸 사용해서 방화벽이랑 뭐... 브루트포스 공격 방어 가능하다. 

print("\n문자열 냅다 곱하기")
print("="*50)

# 냅다 문자열 인덱싱
str_index="Plz Index Str"
#          0123456789012
print(str_index[4])
print(str_index[0:5])
print(str_index[0] + str_index[4] + str_index[10])
print(str_index[-1])
print(str_index[-2])
print("str_index[1:-1:2]", str_index[1:-1:2]) # 1에서 -1까지 가는데 2개 단위로 출력
print("str_index[::2]", str_index[::2])
print()

for i in str_index:
    print(ord(i))   # 아스키코드로 변환하기

print()

for i in range(2, 10):
    print('%d단 시작!' % i)
    for j in range(1, 10):
        print('%d * %d = %d' % (i, j, i*j))
    print('%d단 끝! \n' % i)

# shell에서 반복문 사용하기
# for i in $(echo $str_index)
