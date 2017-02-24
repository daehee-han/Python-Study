def compareList(lis1, list2):#compareList 함수 정의
	if len(list1) != len(list2):#list1과 list2 길이가 다르면 다른 list이므로 False 리턴
		return False
	#list1과 list2의 길이가 같은 경우 
	for i in range(0, len(list1)):#0번부터 리스트 길이 - 1 까지 차례로 비교한다
		if(list1[i] != list2[i]):#list1과 list2 각각에 대응되는 값끼리 비교해서 값이 하나라도 다르면 False
			return False
	return True#여기까지 왔다는 것은 list1과 list2가 같다는 의미이므로 True 리턴

#이 부분은 list의 값을 받아오는 부분으로 아까 말했던 for문을 이용해서 받아와도 됨
list1 = [int(x) for x in input("list1 원소입력: ").split()]
list2 = [int(x) for x in input("list2 원소입력: ").split()]
#isSame에 두 리스트가 같은지 다른지 받음 
isSame = compareList(list1, list2)
if isSame == True:#같으면 
	print("두 리스트는 동일함")#이거 출력
else:#다르면 이거 출력
	print("두 리스트는 다름")

