numbers = [11, 22, 33, 22, 44]
num = int(input("찾고자 하는 값은? "))
if num in numbers:
	print("%d는 리스트 요소 %d입니다." % (num, numbers.index(num)))
else:
	print("%d는 리스트에 없습니다." % (num))
