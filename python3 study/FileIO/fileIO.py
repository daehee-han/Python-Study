import os
import sys # exit()을 쓰려고 import 함

def inputMenu(number):
	if number == 1:
		dic = {}
		dic = readWords()
		print(dic)
	elif number == 2:
		word = input("입력할 단어: ")
		meaning = input("입력할 단어 뜻: ")
		writeWord(word, meaning)
	elif number == 3:
		sys.exit()
	else:
		print("No such menu number")

def writeWord(word, meaning):
	pathname = "output.txt"
	if os.path.exists(pathname):
		fp = open(pathname, "a")
		fp.writelines(word + ':' + meaning + '\n')
		fp.close()
	else:
		print("ERROR: 경로면 %s가 유효하지 않습니다." % pathname)
def readWords():
	dic = {}
	pathname = "output.txt";
	if os.path.exists(pathname):
		fp = open(pathname, "r")
		dicList = fp.readlines()
		for i in range(0, len(dicList)):
			word, meaning = dicList[i].split(":")
			meaning = meaning.replace('\n', '')
			dic[word] = meaning
		fp.close()
	else:
		print("ERROR: 경로면 %s가 유효하지 않습니다." % pathname)
	return dic

while True:
	number = int(input("1.불러오기 2.새 단어 등록하기 3.종료하기: "))
	inputMenu(number)
