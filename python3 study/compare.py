def compare(a, b):
	if a is b:
		print("a와 b는 동일한 객체")
	if a == b:
		print("a와 b는 동일한 값")
	if type(a) is type(b):
		print("a와 b는 동일한 타입")

a = 42
b = 30
compare(a, b)
