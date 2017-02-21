my_list = [1, 2, 3]

try:
    index = int(input("첨자를 입력하세요: "))
    print("my_list[{0}]: {1}".format(index, my_list[index]))
except Exception as error:
    print("예외가 발생했습니다. ({0})".format(error))
finally:
    print("어떤 일이 있어도 마무리합니다.")
