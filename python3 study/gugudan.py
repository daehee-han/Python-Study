print("<구구단 출력>")
print("-------------")
number = int(input("알고싶은 단은? "))

for i in range(1, 10):
	print("%d * %d = %2d" %(number, i, number * i))


