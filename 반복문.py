# 파이썬 반복문 : FOR 실습
# for i in <collection>
#       <loop body>

# range 치면 code assistance에 start, stop, step 정보가 보임
for v1 in range(10):         # 0~9  9 까지 표현
    print("v1 is :", v1)
print()

for v2 in range(1, 11):      # 1 ~10
    print("v2 is :", v2)
print()

for v3 in range(1, 11, 2):   # 1 ~ 10 , 2 step
    print("v3 is :", v3)
print()

# 1 ~ 1000합
sum1 = 0

for v in range(1, 1001):
    sum1 += v    # sum1 = v + 1
print('1 ~ 1000 Sum : ', sum1)   # print 가 선언된 위치 확인
print('1 ~ 1000 Sum : ', sum(range(1, 1001)))  # range함수를 통해 generator 해서 리스트형태로 구성후 sum 함수 사용
print(type(range(1,11)))
print(list(range(1,11)))
print('1 ~ 1000 안에 4의 배수의 합 : ', sum(range(1, 1001, 4)))

# Iterables 자료형 반복, 파이썬에서 Iterables 라고 하는것은 반복하는 객체를 의미
# 문자열, 리스트, 튜플, 집합, 사전
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제1
print("\n예제 1")
names = ["Kim", "Park", "Cho", "Lee", "Choi", "Yoo"]

for name in names:
    print("You are", name)

# 예제2
print("\n예제 2")
lotto_numbers = [11, 19, 21, 28, 36, 37]

for number in lotto_numbers:
    print("Current number : ", number)

# 예제3
print("\n예제 3")
word = 'Beautiful'   # 문자열도 시퀀스 형이기 때문에 Iterable 하기 때문에 사용가능

for s in word:
    print('word : ', s)

# 예제4
print("\n예제 4")
my_info = {
    "name": "Lee",
    "Age": 33,
    "City": "Seoul"
}

for key in my_info:
    print(key, ":", key)

for key in my_info:
    print(key, ":", my_info[key])

for key in my_info:
    print(key, ":", my_info.get(key))

for val in my_info.values():
    print(val)

# 예제5
print("\n예제 5")
name = 'FineApplE'

for n in name:
    if n.isupper():     # isupper를 대문자인지를 체크 islower는 소문자인지 체크
        print(n)        #맞으면 그냥 대문자 출력
    else:               #아니면
        print(n.upper())    #소문자를 대문자로 변경해서 출력

for n in name:
    if n.islower():     # isupper를 대문자인지를 체크 islower는 소문자인지 체크
        print(n)        #맞으면 그냥 대문자 출력
    else:               #아니면
        print(n.lower())  

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

# break   for 문 탈출 
print("\n예제 break")
for num in numbers:
    if num == 34:
        print("Found : 34!")
        break
    else:
        print("Not found : ", num)

# continue  을 만나면  조건 부분으로 넘어감    
# bool 불린형을 처리하고 싶지 않을때 이용
print("\n예제 continue")
lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is bool:    # is 는 자료 형을 비교할 때 사용  is not , is
        continue

    print("current type : ", type(v))
    print("multiply by 2:", v * 3)

# for ~ else 구문   파이썬에서 지원하는 특이한 구문
print("\n예제 for else 구문")
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 45:  # 45
        print("Found : 34!")
        break
else:
    print("Not Found 45...")

# 구구단 출력
print("\n예제 구구단")
for i in range(2, 10):
    for j in range(1, 10):
        print('{:4d}'.format(i * j), end='')  
        # 간격4를 주고 format 함수가 처리한 정수를 우측부터 출력 그리고end 옵션을 # 통해 이어서 출력	
    print()

# 구구단 출력 2
print("\n예제 구구단 2")
for i in range(2, 10):
    for j in range(1, 10):
        print('{0}*{1}={2}'.format(i, j, i*j), end='  ')
    print()    

# 변환 예제
print("\n예제 변환")
name = 'Aceman'
print('Reversed : ', reversed(name))
print('List : ', list(reversed(name)))
print('Tuple : ', tuple(reversed(name)))
print('Set : ', set(reversed(name)))        # 순서X

# ------------------------ while -------------------------
# while <expr>:      #expression   표현식
#    <statement(s)>   #코드
print("\n---------------------------- while -----------------------------")

# 예제1
print("\n예제 1")
n = 5
while n > 0:
    print(n)
    n = n - 1   # n -= 1
#    print(n) 를 아래에 두면? 
    
# 예제2
a = ['foo', 'bar', 'baz']
print("\n예제 2")
while a:
    print(a.pop())
#    print(a) 만약  이렇게 출력 하면 위험한 코드가 된다. 이유는?     a = ['foo', 'bar', 'baz']   ==  True 측  while True:  로 무한하게 반복된다.  pop 함수를 사용하지 않으면 문제가 될 수 있다.

# if 중첩
# 예제3
# break , continue
print("\n예제 if 중첩")
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop Ended.')  
print()

# 예제4
print("\n예제 4")
m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m)
print('Loop Ended.')   

# 예제5
i = 1
print("\n예제 5")
while i <= 10:
    print('i:',i)
    if i == 6:
        break
    i += 1

# While - else 구문
print("\n예제 While - else 구문")
# 예제6
n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break
else:
    print('else out.')
# 예제7 
print("\n예제 7")
a = ['foo', 'bar', 'baz', 'qux']
s = 'qux'

i = 0

while i < len(a):
    if a[i] == s:
        break
    i += 1
else:
    print(s, 'not found in list.')
    
    
# 무한반복
# while True:
#     print('Foo')

# 예제8
print("\n예제 8")
a = ['foo', 'bar', 'baz']
while True:
    if not a:
        break
    print(a.pop())

# while 실습
# 변수명 num으로 지정하고 최대 100까지 증가. 55 일 경우에만 '일치' 가 출력되고 나머지는 '불일치'가 불일치가 출력되도록 코딩해보시오.
# (5씩 증가하도록 하시오.)
print("\n예제 while 실습")
num =0
while num <= 100:
	if num==55:
		print("{} : 일치".format(num))
	else:
		print("{} : 불일치".format(num))
	num=num+5
