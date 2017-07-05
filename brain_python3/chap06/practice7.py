import sys
x = int(input('반복횟수를 입력하세요 : '))

if x <= 0:
    print('0보다 작거나 같은 수는 입력할 수 없습니다.')
    sys.exit()

for i in range(1, x + 1):
    for j in range(i):
        print('*',  end='')
    print()