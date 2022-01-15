# #1~100까지의 숫자중에 3의 배수를 리스트에 담은 후 해당 리스트를 print 하여라.
# lst = []
# for i in range(1,101):
#     if i%3==0:
#         lst.append(i)
#
# print(lst)

# ##for문 예제3 연습문제3 1~100사이에서 3의 배수이면서 2의 배수가 아닌 수를 한줄에 출력하고, 누적합을 출력.
# result = 0
# print('수열 = ', end=" ")
# for i in range(1,101):
#     if ((i%3 ==0) and ((i%2) !=0)) :
#         print(i, end=" ")
#         result += i
# print("누적합 = ", 867)

#2중 for문 구구단으로 구현 예제.

# for left in range(2,10):
#     for right in range(1,10):
#         result = left*right
#         print("%d x %d = %d" %(left, right, result))


#112p. 연습문제 4번.
#순서는 상관없음에 유의
#
# lst = ['과장', '부장', '대리', '사장', '대리', '과장']
# setlst = set(lst)
# lst2 = list(setlst)
# diclst = {}
# print(lst2)
# for a in lst2:
#     count=0
#     for b in lst:
#         if a == b:
#             count += 1
#     diclst[a] = count
#
# print(diclst)

#알고리즘
#최대값 최소값 을 for문을 이용하여 구하라
# lst = [93, 45, 21, 30, 20, 94, 66, 71, 45]
# max = lst[0]
# min = lst[0]
#
# for i in lst:
#     if max < i:
#         max = i
#     if min > i:
#         min = i
# print("최대값 : ", max)
# print("최소값 : ", min)


#알고리즘
#선택정렬 몸풀기 문제 lst = [1,4]가 있다. 1과 4의 위치를 바꾸어, lst=[4,1]로 바꾸는 방법은?
# lst = [1,4]
# tmp = lst[0]
# lst[0] = lst[1]
# lst[1] = tmp
# print(lst)

# lst = [1,4]
# (lst[0], lst[1]) = (lst[1], lst[0])
# print(lst)

#선택정렬 알고리즘을 2중 for문을 이용하여 구현하라.
# lst = [93, 45, 21, 30, 20, 94, 66, 71, 45]
# #오름차순
# for a in range(0,len(lst)-1):
#     for b in range(a+1,len(lst)):
#         if lst[a] > lst[b]:
#             (lst[a], lst[b]) = (lst[b], lst[a])
#             tmp = lst[a]
#             lst[a] = lst[b]
#             lst[b] = tmp
# 
# print(lst)
# lst = [93, 45, 21, 30, 20, 94, 66, 71, 45]
# #내림차순
# for a in range(0,len(lst)-1):
#     for b in range(a+1,len(lst)):
#         if lst[a] < lst[b]:
#             (lst[a], lst[b]) = (lst[b], lst[a])
#             # tmp = lst[a]
#             # lst[a] = lst[b]
#             # lst[b] = tmp
# print(lst)

