# 파이썬 사용자 입력 : Input
# 2.x 때에는 input_raw 같은 함수가 있었는데 저희는 3.x  버전이니까 input 사용
# 기본 타입(str)

# 예제1 : 터미널 환경에서 실행. 인터프리터 언어의 특징
print("\n예제 1")
name = input("Enter Your Name : ")
grade = input("Enter Your Grade : ")
company = input("Enter Your Company name : ")

print(name, grade, company)

# 예제2
print("\n예제 2")
number = input("Enter number : ")
name = input("Enter name : ")

#print("type of number", type(number))
print("type of number", type(number), number * 3)        # 기본 타입(str)       123123123
print("type of number", type(number), int(number) * 3)   # 위 라인과 결과 비교    369
print("type of name", type(name))

# 예제3(계산)
print("\n예제 3")
first_number = int(input("Enter number1 : "))
second_number = int(input("Enter number2 : "))

total = first_number + second_number
print("first_number + second_number : ", total)

# 예제4
print("\n예제 4")
float_number = float(input("Enter a float number : "))

print("input float : ", float_number)
#print("input float : ", float_number * 1.2113)     # 만약 형변환이 안되었다면 에러가 발생
print("input type : ", type(float_number))

# 예제5
print("\n예제 5")
print("FirstName - {0}, LastName - {1}".format(input("Enter first name : "), input("Enter second name : ")))
# input 함수는 변수로 할당 하지 않아도 필요한 부분에서 선언해서 함수의 안에서도 사용가능

