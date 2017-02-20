class MyClass:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

my_class = MyClass()
my_class.increment()

print(my_class.count)