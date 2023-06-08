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
