# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용

# 선언
# () 튜플  [] 리스트 {} 집합, 딕셔너리
# a = {'name': 'Kim', 'name': '01012345678' }  <-- 키가 중복되면 안된다.
# key : value   ,키는 숫자 문자 다된다. 
# 키만 존재 하면  value 엔 어떤 자료형이라도 좋다. 

a = {'name': 'Kim', 'phone': '01012345678', 'birth': '870124'}
b = {0: 'Hello python!'}
c = {'arr': [1, 2, 3, 4]}
d = {
	 'Name' : 'Niceman',
	 'City'   : 'Seoul',
	 'Age': '33',
	 'Grade': 'A',
	 'Status'  : True
}

# dict 리스트에 튜플 형태로 선언 . 자주 사용하는 형태가 아니다. 가독성이 떨어진다. 
e =  dict([			
	 ( 'Name', 'Niceman'),
	 ('City', 'Seoul'),
	 ('Age', '33'),
	 ('Grade', 'A'),
	 ('Status', True)
])

f =  dict(
	 Name='Niceman',
	 City='Seoul',
	 Age='33',
	 Grade='A',
	 Status=True
)

# 만약 f1 부터 f100 까지 있다면  리스트 안에 a = [ f1, f,2 ... f100 ]  형태로 자료를 저장하고 관리 하면 효율적으로 사용
# java 에서는 맵, 웹에서 자주 사용하는 json 형태로 많이 사용
print("\n출력 1")
print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# 출력
print("\n출력 2")
print('a - ', a['name'])  # 존재X -> 에러 발생
print('a - ', a.get('name'))  # 존재X -> None 처리.  
print('b - ', b[0]) 
print('b - ', b.get(0))
print('c - ', c['arr'])
print('c - ', c['arr'][3])
print('c - ', c.get('arr'))
print('d - ', d.get('Age'))
print('e - ', e.get('Grade'))
print('f - ', f.get('City'))

# 딕셔너리 추가
a['address'] = 'seoul'  #address 키가 존재 하지 않는데  추가를 하면  등록됨
a['name'] = 'seoul'   # 키가 존재하면 값을 수정
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)

# 딕셔너리 길이  - 시퀀스 형이기 때문에 len 을 이용한 길이를 쓸수 있다.  
# 키의 갯수를 확인 할 수 있다.
print("\ndictionaty 길이")
print(len(a))
print(len(b))
print(len(d))
print(len(e))

# dict_keys, dict_values, dict_items : 반복문(iterate) 사용 가능
# dir 함수로  __iter__ 있으면 반복문에서 사용할 수 있다.
print("\n출력 keys")
print('a - ', a.keys())
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())

print("\n출력 list keys")
print('a - ', list(a.keys()))   # 리스트로 변환 
print('b - ', list(b.keys()))
print('c - ', list(c.keys()))
print('d - ', list(d.keys()))

print("\n출력 values")
print('a - ', a.values())
print('b - ', b.values())
print('c - ', c.values())
print('d - ', d.values())

print("\n출력 list values")
print('a - ', list(a.values()))
print('b - ', list(b.values()))
print('c - ', list(c.values()))
print('d - ', list(d.values()))

print("\n출력 items")
print('a - ', a.items())  # 키와 밸류가 한쌍의 튜플로 감싸고 리스트 형태로 출력
print('b - ', b.items())
print('c - ', c.items())
print('d - ', d.items())

print("\n출력 list items")
print('a - ', list(a.items()))
print('b - ', list(b.items()))
print('c - ', list(c.items()))
print('d - ', list(d.items()))

print("\n출력 pop")
print('a - ', a.pop('name'))
print('a - ', a)
print('b - ', b.pop(0))
print('c - ', c.pop('arr'))
print('c - ', c)
print('d - ', d.pop('City'))

print("\n출력 popitem")
print('f - ', f.popitem())  # popitem 는 무작위로 추출 . 딕셔너리는 순서가 없어서
print('f - ', f.popitem())
print('f - ', f.popitem())
print('f - ', f.popitem())
print('f - ', f.popitem())

# 예외
# print('f - ', f.popitem())

print("\n출력 in {}")
print('a - ', 'name' in a)  # 키가 존재하는지 체크 
print('a - ', 'birth2' in a)
print('a - ', 'addr' in a) 
print('a - ', 'City' in d)  #

# 수정 
print("\n출력 a")
a['test'] = 'test_dict'
print('a - ',  a)

a['address'] = 'dj'
print('a - ',  a)

a.update(birth='900101')  # 메소드를 이용한  수정
print('a - ',  a)

temp = {'address': 'Busan'}
a.update(temp)
print('a - ',  a)

print("\n출력 f")
f.update(Age=36)   

temp = {'Age': 27} 
print('f - ', f)

f.update(temp)

print('f - ', f)

# 딕셔너리 실습
srp={'가위':'보','바위':'가위','보':'바위'}
list(srp.keys())
list(srp.values())
list(srp.items())
srp['가위']
srp['찌']='빠'
srp['묵']='찌'
srp['빠']='묵'

# srp 보자기 라는 키가 있는지 확인
'보자기' in srp

# '가위'라고 하는 value값에 해당하는 key 값을 찾도록 함수를 만들어보시오.
# 첫번째 방법
def valuetokey(b):
	if b in srp.value():
		i=list(srp.keys())[list(srp.values()).index[b]]
		return i

# 두번째 방법
def valuetokey(b):
	for i in srp.keys():
		if srp.get(i) == b:
			return i

# 세번째 방법
def valuetokey(b):
	for i,j in srp.items():
		if j==b:
			return i

value='보'
key=valuetokey(value)
print("\n{}의 key 값은 {} 입니다.".format(value,key))

# -------------------------[ 집합 ]------------------------
# 집합(Sets) 특징   
# 딕셔너리, 리스트, 튜플에서 각 각 특징을 가짐   
# 선형대수학, 데이터 분석에서 numpy, scipy (싸이파이) 를 이용해서 사용
# 집합(Sets) 자료형(순서X, 중복X)  집합에서는 어떤 원소가 존재하는 지가 더 중요

# 선언
# () 튜플  [] 리스트  {} 딕셔너리, 집합
a = set()   
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])  # 서로 다른 자료형 선언 가능
e = {'foo', 'bar', 'baz', 'foo', 'qux'}  # 딕셔너리와 다른부분은 키가 없고 리스트 처럼  { } 안에서 나열
f = {42, 'foo', (1, 2, 3), 3.14159}

print("\n--------------------------------- 집합 시작 ----------------------------------")
print('a - ', type(a), a)
# b = set([1, 2, 3, 4, 4, 4, 4])    # 중복을 허용 하지 않는다.
print('b - ', type(b), b)
# print('b - ', type(b), b, 2 in a)    # in 연산자도 사용할 수 있다.  
# print('b - ', type(b), b, 2 in b)    # 튜플이나 , 리스트, 딕셔너리에서 사용할 수 있는다 다할 수 있다. 
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# 튜플 변환
t = tuple(b)
print("\n출력 튜플로 변환")
print('t - ', type(t), t)
print('t - ', t[0], t[1:3])  # 튜플이 되었다는 것은 슬라이싱 할 수 있다는것

# 리스트 변환
l = list(c)
l2 = list(e)
print("\n출력 리스트로 변환")
print('l - ', type(l), l)
print('l - ', l[0], l[1:3])
print('l2 - ', type(l2), l2)

# 길이
print("\n출력 길이")
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))

# 집합 자료형 활용  (교집합(&), 합집합( |). 차집합(-) )
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print("\n출력 집합 자료형 활용")
print('s1 & s2 : ', s1 & s2)
print('s1 & s2 : ', s1.intersection(s2))  

print('s1 | s2 : ', s1 | s2)
print('s1 | s2 : ', s1.union(s2))

print('s1 - s2 : ', s1 - s2)
print('s1 -  s2 : ', s1.difference(s2))

# 중복 원소 확인 (교집합인지 확인)
print("\n출력 중복 원소 확인")
print('l - ', s1.isdisjoint(s2))   # false 가 나올때 중복원소가 존재함을 의미 

# 부분 집합 확인 
#s1 = set([1, 2, 3, 4, 5, 6])
#s2 = set([4, 5, 6])
print("\n출력 부분 집합 확인")
print('subset ', s1.issubset(s2))   # False   부분집합 체크
print('subset', s2.issubset(s1))   # True
print('superset', s1.issuperset(s2))  

# 추가 & 제거
# set 에서는  add, remove , discard, clear 메소드 하용
print("\n출력 add remove discard clear")
s1 = set([1, 2, 3, 4])  
s1.add(5)
print('s1 - ', s1)

s1.remove(2)
print('s1 - ', s1)
# s1.remove(7)   # 없는 원소를 삭제 하려면 keyerror 메시지 발생

s1.discard(3)
print('s1 - ', s1)

#s1.discard(7)    #[중요] 없는 원소를 삭제 하려 해도 에러가 발생하지 않는다.  결국 remove 보다는 discard 사용

# 모두 제거
s1.clear()
print('s1 - ', s1)

a = [1, 2, 3] #리스트도 clear로 삭제 가능
a.clear()
print(a)

# 집합 실습
# a = [1,2,3,4] 로 set s1을 생성하시오.
print("\n집합 실습")
s1=set(a)

# b = "aabbccddeeff"로 set s2를 생성하시오.
s2=set(b)

# s1 에 a,b,c 를 추가하시오.
s1.add('a')
s1.add('b')
s1.add('c')
# 혹은
s1.update(['a','b','c'])

# s2 에 1,2를 추가하시오.
s1.update([1,2])

# s1과 s2의 교집합을 구하시오.(2가지 방법 모두 )
print("교집합:",s1 & s2)
print("교집합:",s1.intersection(s2))

# s1과 s2의 합집합을 구하시오.(2가지 방법 모두)
s1 | s2
print("합집합:",s1.union(s2))

# s1과 s2의 차집합을 구하시오.(기호)
print("차집합:",s1-s2)

# s2와 s1의 차집합을 구하시오.(함수)
print("차집합:",s2.difference(s1))

# s2에서 1을 빼보시오.
s2.remove(1)
print("remove:",s2)
