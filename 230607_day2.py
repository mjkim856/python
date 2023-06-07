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

