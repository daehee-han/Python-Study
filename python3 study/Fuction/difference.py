def difference(n1, n2):
	if n1 > n2:
		big = n1
		small = n2
	else:
		big = n2
		small = n1
	return big - small

n1 = int(input("피연산자1 입력: "))
n2 = int(input("피연산자2 입력: "))
res = difference(n1, n2)

if n1 > n2:
	print("%d - %d = %d" %(n1, n2, res))
else:
	print("%d - %d = %d" %(n2, n1, res))

