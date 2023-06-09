# map 
# 함수는 입력을 받아 기능을 처리 합니다. 
# 다른 입력으로 함수 결과를 보려면 보통 입력을 바꿔서 함수를 다시 호출하는 형태를 가집니다.
# 만약 입력이 여러개라면 for 문을 돌려서 함수를 여러번 호출할 수 있지만 
# map을 이용하여 좀 더 쉽게 활용 할 수 있습니다.

# map 함수 사용방법 
# - 사용이유 : 기존 리스트를 수정해서 새로운 리스트를 만들때
# - 사용방법 : map(함수, 순서가 있는 자료형)    #<--- 리스트, 튜플, 딕셔너리, range 객체 

# map 형식
# map(함수, 입력들)

# 동작 과정
map(int, ['3','4','5','6'])
# ['3','4','5','6'] -------------->int ------------> map object ( 3,4,5,6)

list(map(int, ['3','4','5','6']))
print(list(map(int, ['3','4','5','6'])))

#ex)
def calc(x):
    return x*x

for i in range(1,6):
    print(calc(i))

#map( 함수, 입력값)  활용
map(calc, range(1,6))
# lambda 변환
map(lambda x: x*x, range(1,6))

# calc 함수를 정의하고  for 문을 통해 입력 값을 변경하며 함수를 호출 하는 식입니다.
# 이를 map 을 이용하여 입력 개수만큼 함수를 여러번 호출 할 수 있습니다.
def calc(x):
    return x*x
list(map(calc, range(1,6)))

# 이걸 람다함수로 변경하면? 
list(map(lambda x: x*x, range(1,6)))

# 구구단
list(map(lambda x:(x//10)*(x%10), range(10,100)))
print(list(map(lambda x:str(x//10) + 'x' + str(x%10) + '=' + str((x//10)*(x%10)), range(10,100))))

# 369
list(map(lambda x: '짝' if x % 3 == 0 else x, range(1,10)))  # 이건 진짜 369 아님 10 이상부터 문제

list(map(lambda x: '짝' if str(x).find('3') >= 0 or str(x).find('6') >= 0 or str(x).find('9') >= 0 else x, range(1,20)))

# 리스트 형 객체를 인자값으로 각 각 받아서 처리
in1 = [1,3,5,7]
in2 = [2,4,6,8]
list(map(lambda x,y: x+y, in1, in2)) 

lambdaList = [lambda a,b:a+b, lambda a,b:a*b, lambda a,b: a-b, lambda a,b: b/a ]
print(list(map(lambdaList[0], in1, in2)))
print(list(map(lambdaList[1], in1, in2)))
print(list(map(lambdaList[2], in1, in2)))
print(list(map(lambdaList[3], in1, in2)))



# 리스트 모든 요소의 공백 제거  <--- 실제로 크롤링 한 데이터는 이런 상황이 비일비제 발생 

# 1. for문 사용
#a = "   test "
#print(a)
#print(a.strip())

items= ['  로지덱마우스    ', '앱솔키보드    ']
# 리스트 수정  <---  원본 데이터 변경
for i in range(len(items)):
	items[i]=items[i].strip()
print(items)

# 2. map 사용
items= ['  로지덱마우스    ', '앱솔키보드    ']
def strip_all(x):
	return x.strip()
# 출력 시 형변환 
items = ['    로지덱마우스 ', '앱솔키보드    ']
items = list(map(strip_all,items))   
# <----  이 방법은  출력시 형변환을 하는 것으로 원본 수정이 일어나지 않는다.
items_after = list(map(strip_all,items))  
print(items_after) 
print(items)

# 3. 람다 함수 사용
items = [' 로지덱마우스 ', '앱솔키보드 ']
items = list(map(lambda x:x.strip(), items))


# filter
# filter 함수 사용방법
# - 사용이유 : 기존 리스트에서 조건을 만족하는 요소만 뽑고 싶을 때
# - 사용방법 : filter(함수, 순서가 있는 자료형)

def func(x):
	return x<0

print(list(filter(func, [-3,-2,0,5,7 ])))


# 순서가 있는 자료형 
# [-3,-2,0,5,7 ]		----------------->    x < 0 --------------> filter object (-3, -2)


# 리스트에서 길이가 3이하인 문자들만 필터링 

# 1. for문 사용
animals = ['cat', 'tiger', 'dog', 'bird', 'monkey']
result = []
for i in animals:
	if len(i) <= 3:
		result.append(i)
print(result)
# filter 사용했을때 
animals = ['cat', 'tiger', 'dog', 'bird', 'monkey']
def word_check(x):
	return len(x) <=3
result = list(filter(word_check, animals))
print(result)
# lambda 사용
animals = ['cat', 'tiger', 'dog', 'bird', 'monkey']

result = list(filter(lambda x: len(x) <=3, animals))
print(result)