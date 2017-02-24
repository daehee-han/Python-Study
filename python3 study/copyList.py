data1 = [11, 22, 33]
data2 = list()
print("== 복사 전 ==")
print(data1)
print(data2)

for x in data1:
	data2.append(x)
print("== 복사 후 ==")
print(data1)
print(data2)
