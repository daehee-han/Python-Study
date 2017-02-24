number = list()
while True:
	x = int(input("양의 정수 입력(-1 입력시 종료): "))
	if x == -1:
		break
	number.append(x)
print("입력값: ", end="")

for x in number:
	print(x, end=" ")
print()
