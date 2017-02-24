a = [11, 22, 33, 44]
b = [11, 22, 33, 44]
c = [11, 22, 33]
d = [11, 22, 55, 44]

print("리스트1:", a)
print("리스트2:", d)
check = True
if len(a) == len(d):
	for i in range(0, len(a)):
		if a[i] != d[i]:
	   		check = False	
else:
	check = False
if check == True:
	print("두 리스트는 같습니다.")
else:
	print("두 리스트는 다릅니다.")
