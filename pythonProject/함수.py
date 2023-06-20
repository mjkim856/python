# 가변인자(arg)는 튜플, 가변 키워드 인자(kwarg)는 딕셔너리로 받는다.
# 일반적으로 함수는 소문자, 클래스는 대문자

def hello(a, b=123):
    print('hello1')
    print(a, b)
    return 1234

print(hello(1, 123))
print()

def hello2(a, *b):          # *b는 튜플이다. 바뀌지 않았음을 증명해야 하기 때문이다.
    print(hello2)
    print(a, b)
    return 1234

print(hello2(1, 123, 'ㅁ', 'ㅇ', 'ㄴ'))
print()

def hello3(a, *b, **c):     # 딕셔너리?
    print(hello3)
    print(a)
    print(b)
    print(c)
    return 1234

print(hello3(a=6, b3=4, c8=8))
print()


def hello4(a, *b, **c):
    print(hello4)
    print(a)
    print(b)
    print(c)
    return 1234

a = (1, 2, 3, 4, 5)
print(hello4('a', *a))                  # 아래와 같은 결과
print(hello4('a', 1, 2, 3, 4, 5))       # 위와 같은 결과
print(hello4('a', 1, 2, 3, 4, 5, y=0, u=0))
print(hello4('a', y=0, u=0))
# print(hello4('a', y=0, u=0, 1, 2, 3, 4, 5))  순서 바꾸면 안 됨
print()
print()
print()

# 데코레이터 : 함수 안의 함수. 함수가 다른 함수를 받아서 장식해준다 (?????)
# 사용법 : 함수와 함수 사이에 이러면 실행해 저러면 멈춰 이런 식으로 사용한다.
def deco(func):
    def inner(*args, **kwargs):              # 뭘 받을지 모르니까 이렇게 적는다.
        return func(*args, **kwargs)
    return inner

hello5 = deco(hello4)                        # 함수 객체를 가진다? NameError: name 'h1232ello4' is not defined
print(hello5('a', 1, 2, 3, 'k1=v1', 'k2=v2'))

@deco
def hello6(*args, **kwargs):
    pass

def outdeco(route1, route2):
    def innerdeco(func):
        def inner(*args, **kwargs):
            return inner
        return inner
    return innerdeco

@outdeco(1, 2)
def hello3():
    pass

