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



#함수안에 선언된 변수의 효력 범위, 일전에 설명한 while문 안과 밖의 a와 비교.
# a = 2
# def sum(a):
#     a += 1
#     return a
# result = sum(a)
# print(result)
# print(a)


#함수는 메모리에 별도로 저장되며, 그 함수내의 변수 또한 별개의 값.
#함수를 쓰는 이유를 이해하면, 왜 이러한 구조로 돼 있는지 이해 할 수 있다. 함수는 기본적으로 주어진 매개변수를 mix하여 return하는것.
# result = 2
# def sum(a):
#     result += a
#     return result
# sumvalue = sum(1)
# print(sumvalue)

#a에 영향을 줄 수 있는 방법 2가지 1.a에 다시 담아둔다.
# a = 2
# def sum(a):
#     a += 1
#     return a
# a = sum(a)
# print(a)
# print(a)

#a에 영향을 줄 수 있는 방법 2가지 2.global 선언
result = 2
def sum(a):
    global result
    result += a
    return result
sumvalue = sum(1)
print(sumvalue)