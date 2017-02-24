numbers = list()

for x in range(0, 10):
	a = int(input("? "))
	numbers.append(a)
for x in numbers:
	star = x // 10
	if x % 10 >= 5:
		star += 1
	for y in range(1, star + 1):
		print("*", end="")
	print()

   			
