def intAbs(n):
	if n < 0:
		return -n
	else:
		return n	

def intMax(n1, n2):

	if n1 < n2:
		return n2
	else:
		return n1

number = [int(x) for x in input("정수 10개를 입력하시오: ").split()]

maxnum = intAbs(number[0])
res = number[0]
for i in range(1, len(number)):
	oldmax = maxnum
	maxnum = intMax(maxnum, intAbs(number[i]))	
	if oldmax != maxnum:
   		res = number[i]	
print("절댓값이 가장 큰 수: ", res)
