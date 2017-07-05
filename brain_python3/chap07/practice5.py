def print_star(num):
    for i in range(num, 0, -1):
        for j in range(i):
            print('*', end='')
        print()

print(print_star(5))