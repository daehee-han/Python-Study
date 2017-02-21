my_list = [1, 2, 3]

try:
    index = int(input("첨자를 입력하세요: "))
    print(my_list[index]/0)
except ZeroDivisionError as err:
    print("0으로 나눌 수 없습니다. ({0})".format(err))
except:
    print("예외가 발생했습니다.")
    