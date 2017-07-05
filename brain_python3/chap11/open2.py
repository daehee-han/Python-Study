class open2(object):
    def __init__(self, path):
        print('initialized')
        self.file = open(path)

    def __enter__(self):
        print('enter')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')
        self.file.close()
        return True

with open2('test.txt') as file:
    str = file.read()
    print(str)