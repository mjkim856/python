# 파이썬 함수
# 함수의 필요성 1. 단계별로 프로그램을 작성할 필요존재.  2. 코드의 재 사용성을 높일 필요 있음(동일한 기능 한번에 수정 가능).  3. 코드의 안정성을 높일 수 있다.
# 파이썬 함수식 및 람다(lambda)
# 함수를 사용하는 이유 : 재사용성이 좋아지고, 유지보수가 편리해지고, 가독성이 좋아진다.

# 함수를 사용하지 않은 경우
print("안녕하세요. ㅁㅁ님")
print("현재 프리미엄 서비스 사용기간이 30일 남았습니다.")

# 함수를 사용한 경우
def printMessage(name, date):
    print("안녕하세요. ", name, "님")
    print("현재 프리미엄 서비스 사용기간이 ", date, "일 남았습니다.")

printMessage("ㅁㅁ", 30)
printMessage("ㅇㅇ", 15)

#1.  함수의 기본 형태
# 정의하기
# def function_name(parameter):      
#     code 

# 호출하기
# 함수이름()  # function_name()
print("\n출력 : 함수 예제 1")
def printHello():
	print("Hello")

printHello()

def printHello2(a):
	print(a)

printHello2("Hello2")

#2.  매개변수가 있는 함수
def sum(a, b):
    print(a + b)

sum(3, 4)

#3.  반환값이 있는 함수
import random
def getRandomNumber():
    number = random.randint(1,10)
    return number

print(getRandomNumber())

#4.  매개변수와 반환값이 있는 함수 
def add(a, b):
    result = a + b
    return result

print(add(5,6))

# 다양한 매개변수
# 1. 위치 매개변수(자주 사용하던거) , 2. 기본 매개변수 ( 매개 변수가 받을 기본값을 미리 선언하는것)
# 3. 키워드 매개변수      sum(x=3,y=4)    def sum(y,x) 

# 1. 위치 매개변수(positional parameter)
# 가장 기본적인 매개변수, 함수를 호출할 때 순서대로 데이터(인자) 를 넘겨줘야 한다.
# 다른 매개변수화 함께 쓸 때는 항상 맨 앞에 써야 한다.
# 함수 정의
def my_func(a,b):
	print(a,b)

# 함수 호출
my_func(1,2)

#2. 기본 매개변수(default parameter)
# 매개변수의 기본적인 (Default)값을 지정할 수 있다.
print("\n출력 : 매개변수 있는 함수")
# 함수 정의 
def post_info(title,content='내용없음'):   # content 매개변수의 default 값을 정의 해줌
	print('제목 :', title)
	print('내용 :', content)

# 함수 호출 
post_info('출석합니다!')

#3.  키워드 매개변수(keyword parameter)
# 함수 호출 시에 키워드를 붙여 호출한다.
# 매개변수의 순서를 지키지 않아도 된다.
print("\n출력 : 키워드 매개변수")
# 함수 정의
def post_info(title,content):
	print('제목 : ', title)
	print('내용 : ', content)

# 함수 호출
post_info(content='없어요',title='여자친구 만드는 방법')  # 인자값을 매개변수에 각각 매핑하여 전달

# 4. 위치 가변 매개변수(positional variable length parameter)
# 가변 매개변수 = 개수가 정해지지 않은 매개변수
# 매개변수 앞에 * 가 붙는다 (튜플형)
print("\n출력 : 위치 가변 매개변수")
# 함수 정의
def print_fruits(*args):
	for arg in args:
	     print(arg)

# 함수 호출
print_fruits('apple', 'orage', 'mango')

# 5. 키워드 가변 매개변수(positional variable length parameter)
# 가변 매개변수 = 개수가 정해지지 않은 매개변수
# 매개변수 앞에 ** 가 붙는다 (딕셔너리형)
print("\n출력 : 키워드 가변 매개변수")
# 함수 정의 1
def comment_info(**kwargs):
	print(kwargs)

# 함수 호출 1
comment_info(name='학생', content='쉽다 파이썬')
{'name': '학생', 'content': '쉽다 파이썬'}  # <--- 딕셔너리로 처리

# 함수 정의 2
def comment_info(**kwangs):
    for key, value in kwangs.items():
        print(f'{key} : {value}')

# 함수 호출 2
comment_info(name='학생', content='쉽다 파이썬')

# 매개변수 작성 순서
# 위치 - 기본 - 위치  가변 - 키워드(기본) - 키워드 가변
# 비교
'''
def post_info(*tags, title, content):   #위치 가변 > 위치 
	print(f'제목 : {title}')
	print(f'내용 : {content}')
	print(f'태크 : {tags}')

post_info('#파이썬', '#함수', '파이썬 함수 정리!', '다양한 매개변수')
'''
# f string? print 문법인 듯
# 비교
print("\n출력 : 비교1")
def post_info(title, content, *tags):
	print(f'제목 : {title}')
	print(f'내용 : {content}')
	print(f'태크 : {tags}')

post_info('파이썬 함수 정리!', '다양한 매개변수', '#파이썬', '#함수', )

print("\n출력 : 비교2")
# 비교
def post_info(*tags, title, content):
	print(f'제목 : {title}')
	print(f'내용 : {content}')
	print(f'태크 : {tags}')

post_info('#파이썬', '#함수', title='파이썬 함수 정리!', content='다양한 매개변수')

# 예제1
def first_func(w1):     # w1 인수 를 매개변수라고 한다.
    print("Hello, ", w1)

word = "Goodboy"
print("\n출력 : 매개변수 예제 1")
#firstfunc()            # 이렇게 선언하면 에러가 발생. 이유는  함수 자체에서 매개변수를 원하는데 입력 하지 않아서.
first_func(word)
#firstfunc              # 이렇게 선언하면   
#print(firstfunc)       # 했을때  함수가 id객체이기 때문에 (오프젝트이기 때문에) fistfunc()로 선언해야 한다.
print("\n출력 : 매개변수 예제 2")
# 예제2
def return_func(w1):
    value = "Hello, " + str(w1)
    return value           
#	    return "Hello, " + str(w1)    # 이 방법이 깔끔함 !!!

x = return_func('Goodboy2')
print(x)
    
#return이 있는 함수는 결과값으로 반환되는 값을 받을 변수를 선언해야 함
# 예제 1과 예제 2를 비교하면 예 

#함수형 프로그램 이란 우리가 수업 시간에 이용했던 reversed() 이런 건 함수 형태를 이용한 것 
#파이썬은 함수형 프로그램 그리고 함수형 프로그래밍이라는 방법이라는 기법이 존재함
#효과적인 코딩을 위해서 함수를 학습할 필요가 존재
print("\n출력 : 매개변수 예제 3 : 다중반환")
# 예제3(다중반환)
def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3    # 다운 리턴  

x, y, z = func_mul(10)   #  이것이 언패킹 

print(x, y ,z)
print("\n출력 : type과 list")
# 튜플 리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)      # 튜플로 패킹해서 묶어주면 

q = func_mul2(20)

print(type(q), q, list(q))     # 튜플로 패킹해서 묶어진채로 출력

# 리스트 리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]     # 리스트로 묶어줌

p = func_mul2(30)

print(type(p), p, set(q))    # 집합으로 출력도 가능

# 딕셔너리 리턴
def func_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'v1': y1, 'v2': y2, 'v3': y3}

d = func_mul3(30)

#print(type(d), d)
print(type(d), d, d.get('v2'), d.items(), d.keys())
#print(d.values())

# 중요
# *args, **kwargs
print("\n출력 : *args")
# *args(언팩킹)                          가변적인 매개변수( 갯수가 다양할 경우)를 처리 함. 보통 자료형 중 튜플 형태 처리 할 때 많이 함
def args_func(*args):                   # 매개변수 명 자유 *a 로 써도 됨
    for i, v in enumerate(args):        # i 는 0 번 부터 시작하는 index , v 는 실제 value 값
						                # enumerate 함수가 만들어줌  즉 튜플 형태의 값 생성
        print('Result : {}'.format(i), v)
    print('-----')

args_func('Lee')     # 여기서 중요한건 def args_func(*args) 정의 시  def args_func(args) 로 선언하면 lee를 문자로 받아서
				     # 문자 하나하나를 읽어들여서 처리
			         # 하지만 def args_func(*args)로 선언하면 튜플 형태의 0 번 index로 처리됨

args_func('Lee', 'Park')     # 여기는 인자가 2개 이기 때문에 그전에 함수정의에서는 
				             # 함수 정의 시 def args_func(args, args, args):  인자의 갯수 만큼 선언해야 하지만 
				             # 현재 *args 로 처리 함으로써 해결
args_func('Lee', 'Park', 'Kim')  # 튜플형태의 값을    *args 가변인자 값을 처리 하여 언패킹 하는 형태로 이해
print("\n출력 : **kwargs")
# **kwargs(언팩킹)    - 딕셔너리 자료형 언패킹은  ** 를 선언해서 사용함
def kwargs_func(**kwargs): # 매개변수 명 자유
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print('-----')

kwargs_func(name1='Lee')
kwargs_func(name1='Lee', name2='Park')
kwargs_func(name1='Lee', name2='Park', name3='Cho')
print("\n출력 : *args, **kwargs")
# 전체 혼합
def example(args_1, args_2, *args, **kwargs):  # 인수, 인수, 튜플, 딕셔너리
    print(args_1, args_2, args, kwargs)

example(10, 20, 'Lee', 'Kim', 'Park', 'Cho', age1=20, age2=30, age3=40)
			# 정말 매력적인 파이썬 처리 부분  인수의 갯수에 제한받지않고 사용 !!!

# 전체 혼합 2
# def example(*args, args_1, args_2, **kwargs):  # 인수, 인수, 튜플, 딕셔너리
#     print(args, args_1, args_2, kwargs)

# example(args_1=10, args_2=20, 'Lee', 'Kim', 'Park', 'Cho', age1=20, age2=30, age3=40)

print("\n출력 : 중첩함수")
# 중첩함수      클로저. 지역변수의 상태 유지를 이해 할 필요
def nested_func(num):
    def func_in_func(num):  
        print(num)   
    print("In func")
    func_in_func(num + 100)

nested_func(100)

# 실행불가
# func_in_func(1000)      # 함수 안에 정의된 함수를 호출하면 "not defined" 로 정의되지 않았다는 에러가 발생
# 정의되는 시점은  즉 메모리에 올라가서 사용될 수 있게 되는 시점은 nested_func 정의되고  호출 되었을때 기 때문
# 이걸 부모함수 자식 함수로 설명하면  부모함수자 정의되고 실행 되지 않았기 때문에 자식함수를 호출 할 수 없음

#1.   func_in_func(1000)   호출이 에러가 나는 이유는?
def nested_func(num):
    def func_in_func(num):  
        print(num)   
    print("In func")
    func_in_func(num + 100)

nested_func(100)
# func_in_func(1000) 오류
print("\n출력 : 예제?")
# 매개변수x , 반환값x
def vartest():
    a = 1
    a = a +1
    print(a)

vartest()

# 매개변수x , 반환값o
def vartest():
    a = 1
    a = a +1
    return a

print(vartest())
# 매개변수o , 반환값x

def vartest(a):
    a = a +1
    print(a)

vartest(1)

# 매개변수o , 반환값o
def vartest(a):
    a = a +1
    return a

print(vartest(1))



# -------------------------------------------------------
print("\n출력 : 람다식 예제")
# 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화
# 남발 시 가독성 오히려 감소

#def mul_func(x, y):
#    return x * y
    
#lambda x, y:x*y

# 일반적함수 -> 할당
def mul_func(x, y):
    return x * y

#x = mul_func(4,5)
#print(x)
print(mul_func(10, 50))

mul_func_var = mul_func     # 이름이 있기 때문에 객체가 만들어지고 메모리에 할당됨 
print(mul_func_var(20,50))

# 람다 함수 -> 할당
lambda_mul_func = lambda x,y:x*y   # 객체 이름이 정의 되지 않았지만 lambda 함수가 인수를 받아 처리
print(lambda_mul_func(50,50))

def func_final(x, y, func):
    print('>>>>', x * y * func(100, 100))

func_final(10, 20, lambda_mul_func)

func_final(10,20, lambda x,y:x*y)        # 즉시 lambda 로 정의해서 사용
#func_final(10, 20, lambda_mul_func)     # 자주 사용하는 함수를 lambda 로 정의 해두고 사용
#func_final(10, 20, mul_func_var)        # 일반적인 함수 정의 해서 사용
 
print("\n출력 : 냅다 힌트를 갈겨")
# Hint
def tot_length1(word: str, num: int) -> int:
    return len(word) * num

print('hint exam1 : ', tot_length1("i love you", 10))

def tot_length2(word: str, num: int) -> None:
    print('hint exam2 : ', len(word) * num)

tot_length2("niceman", 10)

def l_fun1(a):
     if a>0:
          return True
     else:
          return False

l_func1 = lambda a: True if a > 0 else False
print("\n출력:람다2",l_func1(3))

# ------------------------------------------
print("\n출력 : 실습")
# 실습문제 

# 세개의 숫자를 받아 합계와 평균을 출력하는 함수
# 문자열 포매팅
def printSumAvg(x, y, z):
    sum = x + y + z
    avg = sum / 3
    print(f"합계 : {sum} 평균 : {avg}")

printSumAvg(10, 20, 30)

#---------------------------------------------------------
print("\n출력 : 로또 번호")
# 로또 번호 추출기
import random

def get_random_number():
    number = random.randint(1, 45)
    return number

lotto_num = [] # 로또 번호를 저장할 리스트 

count = 0 # 현재 뽑은 숫자 개수

while True:
    if count > 5:
        break
    random_number = get_random_number()
    if random_number not in lotto_num:
        lotto_num.append(random_number)
        count += 1

lotto_num.sort()
for num in lotto_num:
    print(num, end=" ")
