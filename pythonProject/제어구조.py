# if, for, while

# if
a = 10
b = 0
if (a or b) and 2:
    print('True')
else:
    print('False')

if not b:                       # b가 참이 아니면 false print
    print('False')

if a:
    print('a true')
elif b:
    print('b true')
else:
    print('a b false')

print()



# --------------------------------------------------------
# for
for i in 'abc':
    if i == 'b':
        continue
    print(i)
print()

for i in 'abc':
    print(i)
else:
    print('for else')       # 거짓일 때 실행된다.
print()

for i, v in {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}.items():
    print(i)
    print(v)  # 거짓일 때 실행된다.
else:
    print(v)  # 거짓일 때 실행된다.
print()





# --------------------------------------------------------
# while
b = [1, 2, 3, 4]
while b:
    print('*')
    b.pop()
print()

b = [1, 2, 3, 4]
while b:
    print('*')
    if b.pop() == 2:
        continue
print()

b = [1, 2, 3, 4]
while b:
    print('*')
    if b.pop() == 2:
        continue
else:
    pass

b = [1, 2, 3, 4]
while b:
    if b.pop() == 0:
        pass
        print("pass")
else:
    pass





