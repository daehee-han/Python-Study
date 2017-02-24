while True:
	year = int(input("윤년을 확인하고자 하는 연도는? "))
	if year % 400 == 0:
		print("윤년입니다.")
	elif year % 100 == 0:
		print("평년입니다.")
	elif year % 4 == 0:
		print("윤년입니다.")
	else:
		print("평년입니다.")
	
	y_n = input("다른 연도도 확인하겠습니까?(Y/N) ")
	if y_n == 'y' or y_n == 'Y':
		continue
	elif y_n == 'n' or y_n == 'N':
		break
			
