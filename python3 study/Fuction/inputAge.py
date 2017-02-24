def inputAge(prompt):
	age = int(input(prompt));
	while age < 0:
		age = int(input(prompt))
	return age

age = inputAge("나이를 입력하세요: ")
if age >= 19:
	print("성년")
else:
	print("미성년")
