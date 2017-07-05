my_list = [1, 2, 3]

try:
    index = int(input("첨자를 입력하세요: "))
    print(my_list[index]/0)
except Exception as error:
    print("예외를 발생했습니다. ({0})".format(error))
except ZeroDivisionError as error:
    print("0으로 나눌 수 없습니다. ({0})".format(error))
except IndexError as error:
    print("잘못된 첨자입니다. ({0})".format(error))