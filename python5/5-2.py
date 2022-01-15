#while문의 기본구조는 while 조건문: 실행문 의 구조로서 while안의 조건문이 true인한 계속 반복된다.
# number = 10
# while number == 10:
#     print("숫자는 10입니다.")

#기본 while문 예제
# treeHits = 0
#
# while treeHits < 10:
#
#     treeHits += 1 #뒤와 같이 표현도 가능. treeHits = treeHits +1
#     print("나무를 %s번 찍었습니다" % treeHits)
#     if treeHits == 10:
#         print("나무가 넘어갑니다.")

# #리스트 연습문제2 A형  110p.
# listNum = int(input("리스트의 크기를 입력하세요"))
# a = 0
# lst =[]
# while a < listNum:
#     listNum1 = int(input("임의이 값을 입력하세요"))
#     lst.append(listNum1)
#     a += 1
#
# print(lst)

# #리스트 연습문제2 A형 또다른 풀이.
# import random
# listNum = int(input("리스트의 크기를 입력하세요"))
# a = 0
# lst =[]
# while a < listNum:
#     lst.append(random.randint(1, 10))
#     a += 1
#
# print(lst)

# # #리스트 연습문제2 B형  110p.
# listNum = int(input("리스트의 크기를 입력하세요"))
# a = 0
# lst =[]
# while a < listNum:
#     listNum1 = int(input("임의이 값을 입력하세요"))
#     lst.append(listNum1)
#     a += 1
# if int(input("찾을 값을 입력하시오")) in lst:
#     print("yes")
# else:
#     print("no")

#while문 break문 예제
# treeHits = 0
# while True:
#     treeHits += 1 #뒤와 같이 표현도 가능. treeHits = treeHits +1
#     print("나무를 %s번 찍었습니다" % treeHits)
#     if treeHits == 10:
#         print("나무가 넘어갑니다.")
#         break

#연습문제 3장 문제2.
# import random
#
# print("숫자 맞추기 게임")
# com = random.randint(1, 10)
# while True:
#     my = int (input('예상 숫자를 입력 하세요'))
#     if com == my:
#         print('성공하셨습니다.')
#         break
#     elif com > my:
#         print('더큰 숫자를 입력하세요')
#     elif com < my:
#         print('더 작은 숫자를 입력하세요')


#while문 continue문 홀수만 출력 예제
#
# number = 0
# while number < 100:
#     number = number +1
#     if number % 2 ==0:
#         continue
#     print(number)

#while문 continue문 나무찍기 예제
# treeHits = 1
# while True:
#     if treeHits <= 10:
#         print("나무를 %s번 찍었습니다" % treeHits)
#         treeHits += 1  # 뒤와 같이 표현도 가능. treeHits = treeHits +1
#         continue
#     print("나무가 넘어갑니다.")
#     break


# #for문 기본 예제1
# lista = ['one', 'two', 'three']
#
# for a in lista:
#     print(a)


##for문 예제2
# lista = [90, 25, 67, 45, 80]
# number = 0
# for a in lista:
#     number +=1
#     if a>=60:
#         print("%s 번째 학생은 합격입니다." % number)
#     else:
#         print("%s 번째 학생은 불합격입니다." % number)



#튜플로 구성된 리스트

# tupleList = [(1,2), (3,4), (5,6)]
# for (a,b) in tupleList:
#     print(a + b)


##for문과 continue
# lista = [90, 25, 67, 45, 80]
# number = 0
# for a in lista:
#     number += 1
#     if a < 60:
#         print("%s 번째 학생은 불합격입니다." % number)
#         continue
#     print("%s 번째 학생은 합격입니다." % number)

# ##for문과 break >> a형을 찾는다. >> 선착순 1명만 찾는다고 한다고 할때
# lista = ['b', 'b', 'ab', 'a', 'b', 'b']
# number = 0
# for a in lista:
#     number += 1
#     if a == 'a':
#         print("%s 번째 고객이 이벤트에 당첨되었습니다." % number)
#         break

# #for문 range 예제
# sum =0
# for i in range(1, 101):
#     sum = sum +i
# print(sum)


