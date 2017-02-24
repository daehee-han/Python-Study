height = int(input("What is the height of triangle? "))
for h in range(1, height + 1):
	for x in range(1, h + 1):
		print(x, end="")
	print(end="\n")

