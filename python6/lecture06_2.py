#클래스는 반복되는 변수 & 함수를 미리 정해 놓은 틀이자 설계도 이다.
#클래스가 왜 필요한가? 누적합계를 해주는 프로그램이 있다고 치자. 이걸 A사관련 계산에서도 사용하고, B사 관련 계산에서도 사용한다.
# result = 0
# def lumSum(a):
#     global result
#     result += a
#     return result
#
# #a사
# while True:
#     if xxx 조건:
#         lumSum(1000)
#
#
# #b사
# while True:
#     if xxx 조건:
#         lumSum(1000)
#틀린 합계가 발생. 왜냐하면 사용주체별로 별도로 사용해야 하는 프로그램인데, 위와 같이 사용하면 누적이 되어 문제 발생.

#이를 해결하기 위해 클래스가 등장. 붕어빵틀만 제공하고 각각 필요한 붕어빵을 그때 그때 만들어 쓰는것.
# class Calculator:
#     result = 0
#     def lumSum(a):
#         global result
#         result += a
#         return result
#
#
# #a사
# acompany = Calculator()
# aSum = acompany.lumSum(10)
# #b사
# bcompany = Calculator()
# bSum = bcompany.lumSum(20)

#클래스의 기본 구조와 활용법
# class Calculator:
#     def __init__(self):
#         self.result = 0
#     def lumSum(self, a):
#         self.result += a
#         return self.result
#
# acompany = Calculator()
# aSum = acompany.lumSum(10)
# print(aSum)
# #b사
# bcompany = Calculator()
# bSum = bcompany.lumSum(20)
# print(bSum)
# bSum = bcompany.lumSum(20)
# print(bSum)

#사칙연산 클래스 만들어보기.

# class Calculator:
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second
#     def add(self):
#         result = self.first + self.second
#         return result
#     def mul(self):
#         result = self.first * self.second
#         return result
#     print("클래스 입니다.")
# class1 = Calculator()
# class1.setdata(10, 20)
# result = class1.add()
# print(result)



#클래스의 상속 후 추가
# class CalculatorA(Calculator):
#     def div(self):
#         result = self.first / self.second
#         return result
# classA = CalculatorA()
# classA.setdata(20, 0)
# print(classA.div())


#클래스의 상속에 상속 후 수정
# class CalculatorB(CalculatorA):
#     def div(self):
#         if self.second == 0:
#             return 0
#         else:
#             result = self.first / self.second
#         return result
# classB = CalculatorB()
# classB.setdata(20, 0)
# print(classB.div())

#수정시 덮어씌우되, 부모의 것을 먼저 선언하고 덮어씌우고 싶은경우 super()
#Weapone 클래스 정의
# class Weapone:
#     def __init__(self):
#         self.what = "무기"
#         self.type = "근거리"
#     print("나는 무기 클래스다!")
# #Sword 클래스 정의 : Weapone 클래스 상속
# class Sword(Weapone):
#     def __init__(self, power, level):
#         self.power = power
#         self.level = level
# #Sword 속성(power,level) 및 부모 클래스 Weapon 의 속성 불러오기(what, type)
#     def info(self):
#         print("공격력 : ",self.power)
#         print("필요레벨 : ",self.level)
#         print("무기종류 : ", self.what)
#         print("공격타입 : ", self.type)
# #Sword 클래스 객체 short_sword 선언
# short_sword = Sword(10, 20)
# short_sword.info()



#클래스변수와 객체변수

# class Calculator:
#     # first = 20
#     # second = 30
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second
#     def add(self):
#         result = self.first + self.second
#         return result
#     def mul(self):
#         result = self.first * self.second
#         return result
#     print("클래스 입니다.")
# class1 = Calculator(10, 20)
# class1.first = 30
# print(class1.first)
# print(class1.first)


#모듈 : 함수, 클래스등 .py 안에 선언된 내용은 다른 py프로그램에서 import를 통해 활용할 수 있다.
#lecture06_2_1.py 참고.

#if __name__ == '__main__': 의 문법의 의미
#__name__ : 프로그램의 이름 을 의미
#__main__ : 실행의 주체가 되는 프로그램의 이름 을 의미
#그러므로, 위의 if문의 의미는 해당 프로그램이 실행의 주체가 될 때만 실행하라는 의미이다.

#패키지 = 모듈 여러개를 모아놓은 것. 라이브러리랑 같은 개념
