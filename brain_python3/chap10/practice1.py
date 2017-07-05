my_list = [1, 2, 3, 4, 5]
def print_element(arg, index):
    try:
        print(arg[index])
    except IndexError as error:
        print("잘못된 첨자를 입력했습니다. ({})".format(error))

print_element(my_list, 2)
print_element(my_list, 4)
print_element(my_list, 5)
