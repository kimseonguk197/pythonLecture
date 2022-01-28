
#sys 함수 : 인터프리터에 의해 실행된 명령에 접근할수 있도록 해주는 함수.
import sys

#메모장 만들기 프로그램 만들어보기 python lecture07_2.py -a "hello pyhon"
import sys
textfirst = sys.argv[1]
textsecond = sys.argv[2]

# print(option)
# print(memo)
#
# if option == '-a':
#     with open("memo.txt", 'a', encoding='UTF-8') as f:
#         f.write(memo)
#         f.write('\n')

#특정 파일내에 값을 치환하기 python lecture07_2.py "memo.txt" "textsecond.txt"
with open(textfirst, 'r', encoding='UTF-8') as f:
    textfirsttemp = f.read()
textsecondtemp = textfirsttemp.replace("python", "java")
with open(textsecond, 'w', encoding='UTF-8') as f:
    textfirsttemp = f.write(textsecondtemp)


