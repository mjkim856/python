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
