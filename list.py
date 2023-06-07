# list

a = []
print("type(a) : ", type(a))
print("id(a) :   ", id(a))
b = list()
print("type(b) : ", type(b))
print("id(b) :   ", id(b))
b = a
print("type(b=a) :", type(b))
print("id(b=a) :  ", id(b))

#element 존재하는 리스트 선언
print()
c = [1, 2, 3, 4]
d = [1, "str", ["abc", True, 3.14]]
print(len(c))
print(len(d))
print(d[2][0:2])
print(d[2][0][2])       # 이렇게도 뽑아낼 수 있음!
print()

# type 변경 연습
d20 = d[2][0]
print('d[2][0]의 타입 : ', type(d20))
print('d[2][0]를 list형으로 변경 : ', list(d20))
# print('atr' + c[0]) TypeError: can only concatenate str (not "int") to str
print('atr' + str(c[0]))
# print(d[2][0, 1]) 이건 안 됨! TypeError: list indices must be integers or slices, not tuple
print()

# list 값 변경
c[0] = '123'
print('atr' + c[0])
print(c)
c[1:3] = [5, 6, 7]
print(c)
c[1:3] = [8, 9, 10]
print(c)
c[1:3] = []
print(c)
print()

# 문자열, 리스트 연습
print('My life is mine.'.upper())
print('My life is mine.'.lower())
print('My life is mine.'.isupper())
print('My life is mine.'.count('m'))
print('My life is mine.'.find('m'))
print('My life is mine.'.split())
print(','.join('My life is mine.'))
print('My life is mine.'.replace("e", "EEE"))
print(("192.168.100.40".split(".")))
print('  delete blank   '.strip())
print()

# 이지
print(list("abcdef"))

# 미들
c=' '.join("abcdef").split()
print(c)

# 하드
a="abcdef"
b='.'.join("abcdef")  # a.b.c.d.f
c=b.split('.')  # ['a','b','c','d','e','f']
print(c)

# ---------------------------------------------

# 리스트 연산
print("\n리스트 연산 예제")
l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
print("l1 + l2 = ", l1 + l2)
print("l1 * 3 = ", l1*3)
print(l1[:3])
print(l1[3:])

# append, sort, reverse, insert, remove, pop, extend
print("\nappend, sort, reverse, insert, remove, pop, extend")
l1.append(0)
print(l1.append(0)) # 특이하게 이 경우는 None이 뜬단 말이지?
print(l1)
l1.sort();                   print(l1)
l1.reverse();                print(l1)
l1.insert(0,1);              print(l1)
l1.remove(1);                print(l1)
l1.pop();                    print(l1)
l1.extend(['only', 'list']); print(l1)
del(l1[-1]);                 print(l1) # 인덱스 번호 확실히 알아야 함.


# 리스트 할당. 굉장히 특이하다. 자바도 이랬었나?
print("\n리스트 할당")
x = [1,2,3,4,5]
y = x 
y[2] = 0
print(x)        # [1, 2, 0, 4, 5]
print(y)        # [1, 2, 0, 4, 5]
print(id(x))    # 139695902380544
print(id(y))    # 139695902380544
x[3] = 123
print(x)        # [1, 2, 0, 123, 5]
print(y)        # [1, 2, 0, 123, 5]

# 리스트 복사
print("\n리스트 복사")
a = [5,6,7,8,9]
b = a.copy()
b[2] = 2
print(a)        # [5, 6, 7, 8, 9]
print(b)        # [5, 6, 2, 8, 9]
print(id(a))    # 139695902333184
print(id(b))    # 139695902380608

# 중첩 리스트 복사
print("\n중첩 리스트 복사")
import copy
c = [[1,2], [3,4,5]]
d = copy.deepcopy(c)
d[0][0] = 0
print(c)        # [[1, 2], [3, 4, 5]]
print(d)        # [[0, 2], [3, 4, 5]]
print(id(c))    # 139695902030144
print(id(d))    # 139695903207232

# 반복문 활용
print("\n반복문 활용")
while b:
    l = b.pop()
    print(2 is l)

# 리스트 내포 : for 문, if 문 들을 지정하여 리스트를 간편하게 만드는 것
# [표현식 for 변수 in 순회가능한 데이터]
print("\n리스트 내포 표현식")
nums = [i for i in range(5)]
print(nums)
nums = [100, 200, 300]
d_nums = [i*2 for i in nums]
print(d_nums)

# [표현식 for 변수 in  순회가능한 데이터 if 조건식]
print("\n리스트 내포 표현식과 if")
nums = [i for i in range(1, 20) if i%2 == 0]
print(nums)
nums= [100, 200, 300, 400, 500]
d_nums = [i for i in nums if i >= 300 & i%250 == 0]
print(d_nums)

# 리스트 내포를 사용해서 word_list 에 들어 있는 문자열 중 첫글자가 a 인것만 뽑아서 리스트로 만드세요.
print("\n 연습문제 1번")
word_list = ['apple', 'watch', 'apolo', 'star', 'abocado']

# 리스트 내포 미사용
result = []
for word in word_list:
    if word[0] == 'a':
        result.append(word)        
print(result)

# 리스트 내포 사용
result = []
result = [w for w in word_list if w[0] == 'a']
print(result)

# 두번째 문제
# 리스트 내포를 사용해서 다음과 같이 변경해보자
print("\n 연습문제 2번")

#변경 전 : ['오메가3',None,'비타민c500',None,'홍삼절편']
#변경 후 : ['오메가3','비타민c500','홍삼절편']
items = ['오메가3',None,'비타민c500',None,'홍삼절편']

# 리스트 내포 미사용
result = []
for i in items:
    if i != None:
        result.append(i)
print(result)

# 리스트 내포 사용
result = []
result = [i for i in items if i != None]
# result = [i if i != None else '' else '' for i in items]
print(result)

# ----------------------------------------------
# list 실습
print("\nlist 실습")
number=[1,2,3,4,5,6,7,8,9,10]
alpha=['a','b','c','d','e']

# 1 number 와 alpha 를 합쳐서 numalp 리스트 생성
numalp = number + alpha
print("1번:", numalp)

# 2 numalp 리스트에서 9번 자리부터 11 자리 삭제
numalp[9:12] = []
print("2번:", numalp)

# 3 8번 자리에 [11,12,13] 리스트 형태로 추가
numalp[8] = [11, 12, 13]
print("3번:", numalp)

# 4 1,2,3 번 자리에 구성요소를 21,22,23 으로 교체
numalp[1:4] = [21,22,23]
print("4번:", numalp)

# 5 numalp 리스트 끝에 100 추가 
numalp.append(100)
print("5번:", numalp)

# 7 numalp 리스트를 순서대로 정렬  (에러 발생)
# numalp.sort()
# TypeError: '<' not supported between instances of 'list' and 'int'
# print("7번:", numalp)

# 7.2 numalp 리스트를 역순서대로 정렬
numalp.reverse()
print("7-2번:", numalp)

# 8 ['ㄱ','ㄴ','ㄷ'] 리스트를 2번과 3번 사이에 삽입
numalp.insert(2, ['ㄱ','ㄴ','ㄷ'])
print("8번:", numalp)

# 9 ['ㄱ', 'ㄴ','ㄷ'] 을 뽑는 형태로 pop()로 추출
numalp.pop(numalp.index(['ㄱ','ㄴ','ㄷ']))
print("9번:", numalp)

# 6 number 리스트에서 모든 구성요소 모두 삭제 
numalp[:] = []
print("6번:", numalp)

# ------------------------------------------
# 번외 문제
# numalp 리스트의 순서를 거꾸로 바꿔서 numalp1을 만들어보시오.(단, 기존과 다른 방법=> reverse()를 이용하지 말고 (hint:for))
print("\n번외 문제")
numalp = [1, 2, 3, 4, 5, 6, 7, 8, [11, 12, 13], 'c', 'd', 'e']
numalp1 = []

for i in numalp:
      numalp1.insert(0, i)
print("1번:", numalp1)

# alpha 리스트를 3번 곱해서 alpha3을 만들고 해당 리스트를 이용해서 문자열 "aaabbbcccdddeee"를 만들어 보시오.
print("2번:", numalp)
string1=""

alpha=['a','b','c','d','e']

alpha3=alpha*3

alpha3=['a','b','c','d','e','a','b','c','d','e','a','b','c','d','e']

for x in alpha:
	for y in alpha3:
		if x == y :
			string1=string1+y
print("alpha3 : {}".format(alpha3)) 

print(string1)

string2=""

for x in alpha:
	while x in alpha3:
		string2=string2+alpha3.pop(alpha3.index(x))

print("alpha3 : {}".format(alpha3))

print(alpha3)
print(string1)
