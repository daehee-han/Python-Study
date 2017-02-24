def printStar(n):
	for x in range(1, n + 1):
		print("*", end="")
	print()

def displayTriangle(height):
	for h in range(1, height + 1):
		printStar(h)

h = int(input("삼각형의 높이 입력: "))
displayTriangle(h)
