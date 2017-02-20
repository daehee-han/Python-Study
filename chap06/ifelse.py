print('수를 입력하세요 : ')
a = input()
if a.isnumeric() == True:
    a = int(a)
    if a == 0:
        print('0은 나눗셈에 사용할 수 없습니다.')
    else:
        print('3 /', a, '=', 3/a)
else:
    print("정수가 아닌 수는 나눗셈에 사용할 수 없습니다.")