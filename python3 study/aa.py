pathname="temp.txt"
fp = open(pathname, "r")
inList = fp.readlines()
for inStr in inList:
	inStr = inStr.split('\n')[0]
	print(inStr, end="")
fp.close()
