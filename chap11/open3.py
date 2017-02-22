from contextlib import contextmanager

@contextmanager
def open3(path):
    print('opening file...')
    file = open(path)

    try:
        print('yielding file...')
        yield file
    finally:
        print('closing file...')
        file.close()

with open3('test.txt') as file:
    str = file.read()
    print(str)