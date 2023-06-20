# 1. 자료형 -------------------------------------------------------------------
# 숫자 - 정수, 실수, 복소수
from builtins import print

i1 = 1
f1 = 1.0
j1 = 1j
j1 = 1J
# print(2/1)      실수를 원한다면
# print(2//1)    정수를 원한다면

# 문자열
# '' "" 가능
# print('escape\'')

# 문자열 슬라이싱
str1 = '1234567890'
# print(str1[3])
print(str1[-1])                 # 9
print(str1[0:2])                # 12
print(str1[:2])                 # 12
print(str1[:2:-1])              # 0987654
print(str1[:2:-2])              # 0864
print(str1[:2:-3])              # 074
print(str1[2:-1])               # 3456789
print(str1[1:])                 # 234567890
print(str1[:])                  # 1234567890
print(str1[::])                 # 1234567890
print(str1[::-1])               # 0987654321
print(str1.startswith("1"))
print()

# str1[0] = '2'       TypeError: 'str' object does not support item assignment
# 문자열은 변경 불가하다.

print('ab' + 'cd')
print('ab' * 10)
print('-'*50)
print('문자열'.center(50))
print('-'*50)

# 리스트
l1 = []
l1 = [1, '1', True]
print(l1)
l1.append('뒤에 넣기')
l1.insert(1, '원하는 곳에 넣기')
print(l1)
print(l1.pop())
print(l1.pop(1), ' : 1번째 값 POP')
print(l1)
print()

# 튜플
# 데이터 수정 불가
# 왜 굳이 나눴는지 >> 리스트는 불변성 없다. 튜플은 불변이라 데이터가 변경되지 않음을 만족시킨다.
t1 = (1, 2)
t2 = 3, 4
# t3 = (1)      이렇게 하면 튜플이 아니고 그냥 숫자이다.
t3 = (1, )
print(t1)
print()

# 사전
d1 = {'k1': 'v1', 'k2': 'v2'}
print(d1)
print(d1['k1'])
print(d1.keys())
print(d1.values())
print(d1.items())

# 딕셔너리 컴프리핸션
# print({x: x for x in range(3)})

print()

# 집합, 중복 불가!
st1 = {1, 2, 3}
st2 = {3, 4, 5}
st3 = {7, 8, 9, 9, 8, 0, 8}
print(st1 & st2)        # 교집합
print(st1 | st2)        # 합집합
print(st1 - st2)        # 차집합
print(st3 & st1)        # set()
print(len(st3))         # 4
print(st3)              # {8, 9, 0, 7}
print()

# None
# 이거 그대로 적어야 함. 초기화 용도로도 사용한다.

# Boolean
# 0, 0.0, 0j, 빈 문자열 / 튜플 / 리스트 / 사전 / 집합, None 모두 거짓이다.

