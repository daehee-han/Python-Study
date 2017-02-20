class A:
    def methodA(self):
        print('methodA() call')

class B:
    def __init__(self):
        self.instance_of_A = A()

    def call_methodA(self):
        self.instance_of_A.methodA()

if __name__ == '__main__':
    b = B()
    b.call_methodA()