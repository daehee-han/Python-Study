rh = input("오른쪽 공 색깔은? ")
lh = input("왼쪽 공 색깔은? ")
print("오른쪽에 %s, 왼손에 %s 공을 갖고 있습니다."%(rh, lh))
print("저글링하여 두 손의 공을 맞바꿉니다.")
temp = rh
rh = lh
lh = temp
print("오른쪽에 %s, 왼손에 %s 공을 갖고 있습니다." %(rh, lh))
