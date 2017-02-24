salary = int(input("연간 총 근로 소득을 입력하세요: "))
if salary <= 1200:
	print("근로 소득세: ", salary * 0.06)
elif salary <= 4600:
	print("근로 소득세: ", salary * 0.15)
elif salary <= 8800:
	print("근로 소득세: ", salary * 0.24)
elif salary <= 15000:
	print("근로 소득세: ", salary * 0.35)
else:
	print("근로 소득세: ", salary * 0.38)

