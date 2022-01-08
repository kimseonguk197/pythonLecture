#if문 기본
# trueornot = False
# if trueornot:
#     print("참입니다.")
# else:
#     print("거짓입니다.")


#돈이 만원 이상 있으면 “택시를 타라”, 그렇지 않으면 “걸어가라” 라 출력되도록  코딩. (현재 돈은 13000원)
# money = 13000
# if money >= 10000:
#     print("택시를 타라")
# else:
#     print("걸어가라")

# money = input("얼마가 있나요?")
# if int(money) >= 10000:
#     print("택시를 타시오")
# else:
#     print("걸어가시오")


#파이썬에서는 들여쓰기가 매우 중요하다. 들여쓰기를 통해 논리의 흐름을 따진다.
# money = 13000
# hungryornot = True
# if money >= 10000:
#     print("택시를 타라")
# else:
#     print("걸어가라")
# if hungryornot:
#     print("밥을 사먹어라")
# else:
#     print("TV를 봐라~")

# #A and B >> A, B모두 True 일때 True
# a = True
# b = False
# if not a:
#     print("참입니다.")
# else:
#     print("거짓입니다.")
#
# #A or B >> A, B 둘중하나라도 True 일때 True
# a = True
# b = False
# if not a:
#     print("참입니다.")
# else:
#     print("거짓입니다.")


#not A : A가 참인경우, not A는 false
# a = True
# if not a:
#     print("참입니다.")
# else:
#     print("거짓입니다.")

#A & B : A and B와 동일
#A | B : A or B와 동일

#in, not in : a가 변수 이고, b가 리스트 일 경우, a가 b에 속하면 True
#
# a = 1
# b = [1,2,3]
#
# if a in b:
#     print("a는 b에 속한다")
# else:
#     print("a는 b에 속하지 않는다")

#조건 pass문, 최소한의 자격을 갖췄는지를 파악하고 싶을때 사용.

# busspass = ['money', 'smartphone', 'card']
# mypass = 'paper'
# if mypass in busspass:
#     pass
# else:
#     print("카드를 꺼내시오")

# #다중 조건문
# money = int(input("가지고 있는 금액을 입력하시오."))
# if money >= 10000:
#     print("택시를 타시오")
# elif 10000>money >=2000:
#     print("버스를 타시오")
# elif 2000> money >=1000:
#     print("킥보드를 타시오")
# else:
#     print("걸어가라")

#조건부표현식, 다른언어에서는 3항연산자라 표현
# a=3
# print("성공했을때 실행문") if a > 10 else print("실패했을때 실행문")
# a=30
# message = "성공했을때 실행문" if a > 10 else "실패했을때 실행문"
# print(message)
