
#연습문제 풀이 6-1 183p.
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area_calc(self):
#         return self.width * self.height
#     def circum_calc(self):
#         return (self.width+self.height)*2
#
# print("사각형의 넓이와 둘레를 계산합니다.")
# w = int(input('사각형 가로 입력 :'))
# h = int(input('사각형 세로 입력 :'))
# cal1 = Rectangle(w, h)
# print("사각형의 넓이는:", cal1.area_calc())
# print("사각형의 둘레는:", cal1.circum_calc())

# #연습문제 풀이 6-3 183p.
# class Person:
#     def __init__(self, name, gender, age):
#         self.name = name
#         self.gender = gender
#         self.age = age
#
#     def display(self):
#         print("이름 : %s, 성별 : %s \n나이: %s"%(self.name, self.gender, self.age))
#
# name = input("이름 입력")
# age = input("나이 입력")
# gender = input("성별 입력")
#
# p1 = Person(name, gender, age)
# p1.display()

#연습문제 풀이 6-5 (189p)
# from mtCalcPackage import calcModule
#
# print(calcModule.Add(10, 5))

# #각종 내장함수
#절대값 구하기
# print(abs(-3))

#최대값
# lista = [1,10,5,2]
# print(max(lista))

# pow 제곱함수
# print(pow(2,3))

# #id 함수
# a = 3
# print(id(a))


# #map 함수 : 특정함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받아, 특정함수가 수행한 결과를 리턴.
# def two_times(x):
#     return x*2
# lista = map(two_times, [1, 2, 3, 4])
# print(lista)

# #함수를 통과하여 참인 value만 돌려주는 filter : 첫 번째 인수로 함수 이름을, 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형
# def trueorfalse(x):
#     if x > 0:
#         return True
#     else:
#         return False
# lista = list(filter(trueorfalse, [1,2,3, -1, -2]))
# print(lista)

# #파일최초생성하기
# #open을 하였으나, 해당 파일이 없으면 자동 생성
# #f는 변수이자 파일객체로서, 해당 파일에 대한 정보와 mode(w, r, a)를 갖고 있다.
# #이 변수를 통해 해당 파일을 컨트롤 하는것.
# f = open("test.txt", 'w')
# f.close()
#
# #파일 쓰기모드로 열어 내용삽입.
# f = open("test.txt", "w", encoding="UTF-8")
# for i in range(1,10):
# 	data = "%d번째 줄입니다. \n" %i
# 	f.write(data)
# f.close()
#
# # #아스키코드 출력
# # print(chr(97))

# #파일 읽기모드.
#readline으로 파일을 읽을경우
# f = open("test.txt", "r", encoding="utf-8")
# line = f.readline()
# print(line)
# f.close()
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)
# f.close()

# #readlines를 통해 리스트 형태로 담는경우
# f = open("test.txt", "r", encoding="utf-8")
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close()

# #strip을 통해 \n 제거
# f = open("test.txt", "r", encoding="utf-8")
# lines = f.readlines()
# for line in lines:
#     print(line.strip('\n'))
# f.close()

# #통째로 읽어 오기
f = open("test.txt", "r", encoding="utf-8")
data = f.read()
print(data)
f.close()


# #추가 모드로 읽어오기
# f = open("test.txt", "a", encoding="utf-8")
# for i in range(10,21):
# 	data = "%d번째 줄입니다. \n" %i
# 	f.write(data)
# f.close()

# #close 없이 파일 open 방법
# with open("test.txt", "w", encoding="UTF-8") as f:
#     for i in range(1,10):
#         data = "%d번째 줄입니다. \n" %i
#         f.write(data)

# #웹크롤링 예제
# #!/usr/bin/env python3
# # Anchor extraction from HTML document
# from bs4 import BeautifulSoup
# from urllib.request import urlopen
# #response = urlopen('https://en.wikipedia.org/wiki/Main_Page')
# # with urlopen('https://en.wikipedia.org/wiki/Main_Page') as response:
# #     soup = BeautifulSoup(response, 'html.parser')
# #     for anchor in soup.find_all('a'):
# #         print(anchor.get('href', '/'))
#
#
# print('  ○>> #오늘의 #날씨 #요약 \n')
# with urlopen('https://weather.naver.com/today/09140104') as response:
#     soup = BeautifulSoup(response, 'html.parser')
#     temps = soup.find('strong',"current")
#     cast = soup.find('span',"weather")
#     print('--> 서울 날씨 : ' , temps.get_text() , cast.get_text())

#많이 쓰이는 외장함수
#time
# import time
# # print(time.localtime())
# # print("현재 시각은 %d:%d:%d 입니다." %(time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec))
# print("타입슬립")
# time.sleep(5)
# print("타입슬립끝")

# #random
# import random
# print(random.randint(1, 10))
# lista = random.sample(range(1,46), 6)
# lista.sort()
# print(lista)
# print(sorted(random.sample(range(1,46), 6)))

#webbrowser
# import webbrowser
# webbrowser.open("https://www.naver.com/")
