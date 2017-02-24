number = int(input())
large = number
for number in range(0, 4):
	number = int(input())
	if large < number:
		large = number
print(large)
