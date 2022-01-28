#os 라이브러리를 활용한 디렉터리내 .py 파일검색
import os
#
# serchdir = 'D:\개발자료\PycharmProjects\pythonProject'
# dirlist = os.listdir(serchdir)
# print(dirlist)
# for dir in dirlist:
#     dirtuple = os.path.splitext(dir)
#     if(dirtuple[1] == '.py'):
#         print(os.path.join(serchdir, dir))

#디렉토리내 디렉토리 속의 모든 파일을 search하려면?
# serchdir = 'D:\개발자료\PycharmProjects\pythonProject'
# dirlist = os.listdir(serchdir)
# print(dirlist)
# for dir in dirlist:
#     filename = os.path.join(serchdir, dir)
#     if os.path.isdir(filename):
#         for dir2 in filename:
#             filename = os.path.join(serchdir, dir2)
#             dirtuple2 = os.path.splitext(dir2)
#             if (dirtuple2[1] == '.py'):
#                 print(filename)
#
#     dirtuple = os.path.splitext(dir)
#     if(dirtuple[1] == '.py'):
#         print(filename)

#재귀함수 필요
# def search(serchdir):
#     dirlist = os.listdir(serchdir)
#     for dir in dirlist:
#         filename = os.path.join(serchdir, dir)
#         if os.path.isdir(filename):
#             search(filename)
#         else:
#             dirtuple = os.path.splitext(dir)
#             if(dirtuple[1] == '.py'):
#                 print(filename)
# search('D:\개발자료\PycharmProjects\pythonProject')

#예외처리까지 해주면 더욱 좋다.
# def search(serchdir):
#     try:
#         dirlist = os.listdir(serchdir)
#         for dir in dirlist:
#             filename = os.path.join(serchdir, dir)
#             if os.path.isdir(filename):
#                 search(filename)
#             else:
#                 dirtuple = os.path.splitext(dir)
#                 if(dirtuple[1] == '.py'):
#                     print(filename)
#     except Exception as e:
#         print(e)
#         pass
# search('D:\개발자료\PycharmProjects\pythonProject')


