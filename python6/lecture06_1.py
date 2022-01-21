#함수의 기본구조 def 함수명(매개변수)
# lista = [7,2,3,6]
# # lista.sort()는 list.sort(lista)와 같다.
# print(lista)
# print(1+1)은 print(int.__add__(1, 2)) 와 같다.

#list의 index를 직접 구현, 그러나 리스트가 find를 자체 내장하고 있지 않기 때문에, lst.find(6)의 형태로 사용불가.

# lst = [1, 4, 6]
# print(lst.index(6))
# def find(self, any):
#     a = 0
#     while a < len(self):
#         if any == self[a]:
#             return a
#         a += 1

# print(find(lst, 6))
# print(lst.find(6))

#입력값,출력값이 있는 함수 기본 구조
# def sum(a, b):
#     result = a + b
#     return result
#
# sumvalue = sum(1,2)
# print(sumvalue)

#입력값이 없는 함수 구조

# def hello():
#     return 'hello'
# print(hello)


# 출력값이 없는 함수 구조
# lista = [7,2,3,6]
# # print(lista.sort())
# lista.sort()
# print(lista)

# *args 매개변수 구조
# def sum(*args ):
#     result =0
#     for i in args:
#         result += i
#     return result
# sumvalue = sum(1,2, 3, 4,5 )
# print(sumvalue)


#2개 이상의 리턴값이 있을경우
# def sum(a, b):
#     result = a + b
#     result2 = a*b
#     result3 = a//b
#     return result, result2, result3
# sumvalue = sum(1,2)
# print(sumvalue)

#default값 미리 세팅하기
# def sum(a, b, test='dev'):
#     if(test == 'dev'):
#         result = a + b
#         return result
#     elif test == 'real':
#         result = a + b
#         result2 = a*b
#         result3 = a//b
#         return result, result2, result3
# sumvalue = sum(1,2, test='real')
# print(sumvalue)

#함수의 매개변수의 순서를 맞춰야 하는가? 안맞춰도 되는 방법은?
# def whoareyou(name, age, gender):
#     print("제 이름은 %s 이고 나이는 %d 살, 그리고 성별은 %s 입니다." %(name, age, gender))
# whoareyou(age=19, name='홍길동', gender= '남자')
# whoareyou(19,'홍길동',  '남자')


#lamda 함수의 사용
# def add(a, b):
#     return a+b
# add = lambda a, b: a+b
# print(add(1,2))

#람다를 왜 사용하느냐? list같은 형태로 담는 등, 자유도가 높다.
# addLst =[lambda a, b: a+b]
# lst = []
# lst.append(addLst[0](1,2))
# lst.append(addLst[0](3,4))
# print(lst)
#람다를 왜 사용하느냐? list같은 형태로 담는 등, 자유도가 높다. 곱하기까지 추가해서 사용가능.

# addLst =[lambda a, b: a+b, lambda a, b:a*b]
# lst = []
# lst.append(addLst[0](1,2))
# lst.append(addLst[1](1,2))
# lst.append((addLst[0](1,2), addLst[1](1,2)))
# print(lst)

#지역변수와 전역변수 란 무엇인가
#지역변수의 예 : 함수안의 변수 a 전역변수의 예 : 함수밖의 a
# a = 2
# def sum(a):
#     a += 1
#     return a
# result = sum(a)
# print(result)
# print(a)

#아래와 같은 프로그램은 아에 빨간줄이 뜬다.
# result = 2
# def sum(a):
#     result += a
#     return result
# sumvalue = sum(1)
# print(sumvalue)

#함수안에서의 변수들은 함수가 호출이 끝나면 사라진다.  메모리 호출 구조를 보면 더 편하다
#https://pythontutor.com/live.html#mode=edit 참고
#모든 변수는 메모리에 담긴다. 그러나 메모리의 어떤 영역에 담기느냐에 따라, 그 효력 범위가 달라진다.
#파이썬의 메모리 구조 참고 http://www.tcpschool.com/c/c_memory_structure


#그렇다면 파이썬에서는 왜 지역변수를 함수호출이 끝나면 사라지도록 설계 하였을까? 파이썬 뿐만아니라 대부분의 프로그램에서
#예를 들어 아래 프로그램에서 add는 여러번 사용이 가능하다.
#아래와 같은 프로그램에서 add의 결과값이 누적이 된다면 말이 되겠는가?
# result = 0
# def add(a, b):
#     result = a + b
#     return result
# academywork = 10
# academymoney = 0
# cash = 10000
# card = 10000
# if academywork >= 10:
#     academymoney = add(cash,  card)
# companywork = 20
# companymoney = 0
# cash = 30000
# card = 30000
# if companywork >= 20:
#     companymoney = add(cash,  card)

# 담아두고 싶으면 아래 2가지 방법을 써야 한다.
#a에 영향을 줄 수 있는 방법 2가지 1.a에 다시 담아둔다.
# a = 2
# def sum(a):
#     a += 1
#     return a
# a = sum(a)
# print(a)
# print(a)

#a에 영향을 줄 수 있는 방법 2가지 2.global 선언
# result = 2
# def sum(a):
#     global result
#     result += a
#     return result
# sumvalue = sum(1)
# print(sumvalue)

#그런데 특이한 자료 구조가 있다. list를 생각해보자. 이게 어찌된일일까?
#이건 아래와 같은 자료구조의 특성을 보면 이해할 수 있다.
#함수도 메모리에 주소가 할당되어 저장되지만, 함수 내의 지역변수는 스택에 저장되어 휘발되도록 한다.
#그에 반해 list의 append는 object로서 heap 메모리라는 휘발되지 않는 공간에 변수값을 추가 하는 것므로 날아가지 않는다.
# b = (2,3,4)
# print("리스트 b의 id ", id(b))
# b = (1,2)
# def test(b):
#     b = (1,2)
# test(b)
# print("리스트 b는?", b)

# a=1
# print("a의 id ", id(a))
# a=2
# print("a의 id ", (id(a)))
# b = [2,3,4]
# print("리스트 b의 id ", id(b))
# def test(b):
#     b = b.append(1)
# test(b)
# print("리스트 b의 id ", id(b))
# print("리스트 b의 [2]의 id ", id(b[2]))
# print("리스트 b의 [1]의 id ", id(b[1]))
# print("함수 test의 id ", id(test))

#mutable immutable
#위에서 말한 일반적인 자료형들은 모두함수를 통해서 전역변수를 변화 시킬수 없는 불변의 값이다. 즉  immutable 하다.
#그러나 리스트, 집합과 같은 자료형은 함수내에서도 특정 함수를 통해 해당 값을 변화시킬 수 있는, mutable한 자료형이 되는 것이다.




