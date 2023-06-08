# 별 5개 기준
# 직선 -------------------------------------------------
print()
print("*****")
print("*"*5)



# 세로 -------------------------------------------------
print()
for i in range(5):
	print("*")
        


# 정사각형 ---------------------------------------------
print()
for i in range(5):
	print("*****")



# 직각삼각형 -------------------------------------------
print()
for i in range(5):
    for j in range(i+1):
        print('*', end='')
    print()

print()
for i in range(5):
    print('{:<5}'.format('+' * (i+1)))



# 좌우대칭 직각삼각형 -----------------------------------
print()
for i in range(1,6):
     for j in range(5-i):
          print(' ', end='')     
     for j in range(i):
          print('*', end='')
     print()

print()
for i in range(5):
     print('{:>5}'.format('+'*(i+1)))



# 상하대칭 직각삼각형 -----------------------------------
print()
for i in range(5, 0, -1):
    for j in range(i):
        print('*', end='')
    print()

print()
for i in range(5,0,-1):
     print('{:<5}'.format('+' * (i)))



# 상하좌우대칭 직각삼각형 -------------------------------
print()
for i in range(5):
    for j in range(i):
        print(' ', end='')
    for j in range(5-i):
        print("*", end='')
    print()
    
print()
for i in range(5):
    print('{:>5}'.format('+'*(5-i)))

    


# 별 9개 기준 ------------------------------------------
# 피라미드
print()


print()
for i in range(0, 9, 2):
    print('{:^9}'.format('+'*(i+1)))



# 역피라미드 -------------------------------------------
print()

print()
for i in range(0, 9, 2):
    print('{:^9}'.format('+'*(9-i)))


# 다이아몬드 -------------------------------------------
print()

print()



# 모래시계 ---------------------------------------------
print()

