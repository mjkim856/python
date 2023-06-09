# 계산기 구현
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
print(cal2.sub(1))

# ---------------------------------------------
print()
# 메서드 추가하기 
class Unit:
    def __init__(self, name, hp, shield, demage):   # __init__  이런 선언부를 생성자라고 한다.
        self.name = name   # self 는 객체 자기 자신을 의미
        self.hp = hp
        self.shield = shield
        self.demage = demage
    def __str__(self):    # 정보 출력 메서드
        return f"[{self.name}] 체력 : {self.hp} 실드 : {self.shield}  공격력 : {self.demage}"

probe = Unit("프로브", 20, 20, 5)
zealot = Unit("질럿", 100,60,16)
dragoon = Unit("드라군", 100,80,20)
print(probe)
print(zealot)
print(dragoon)

# ----------------------------------------------------
print()
# 여러가지 속성(인스턴스 속성, 클래스 속성, 비공개 속성)
# 1. 인스턴스 속성 : 객체마다 다르게 가지는 속성

# 클래스 안 : self.속성명       ex) self.name
# 클래스 밖 : 객체명.속성명      ex) probe.name

class Unit:
    """
    인스턴스 속성 : 이름, 체력, 방어막, 공격력   -> 객체마다 다른값을 가지는 속성
    """
    def __init__(self, name, hp, shield, demage):   # __init__  이런 선언부를 생성자라고 한다.
        self.name = name        # self 는 객체 자기 자신을 의미    # 인스턴스 속성
        self.hp = hp		    # 인스턴스 속성
        self.shield = shield    # 인스턴스 속성
        self.demage = demage    # 인스턴스 속성
    def __str__(self):          # 정보 출력 메서드
        return f"[{self.name}] 체력 : {self.hp} 실드 : {self.shield}  공격력 : {self.demage}"

probe = Unit("프로브", 20, 20, 5)           # 인스턴스 속성은 객체마다 다른 속성을 가진다.
zealot = Unit("질럿", 100,60,16)            # 인스턴스 속성은 객체마다 다른 속성을 가진다.
dragoon = Unit("드라군", 100,80,20)         # 인스턴스 속성은 객체마다 다른 속성을 가진다.
# Unit("프로브", 20, 20, 5) 같이 객체를 선언할 때  각 객체 마다 다른 속성을 가진다.

# 인스턴스속성 수정
probe.demage += 1
print(probe)
