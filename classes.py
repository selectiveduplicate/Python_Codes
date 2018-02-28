class Foo:
    def __init__(self, val):
        self.val = val

    def printVal(self):
        print(self.val)

    def __lt__(self, other, val):
        print(self.val)


obj1 = Foo(1)
obj2 = Foo(2)
obj3 = Foo(43)

obj1.printVal()
obj2.printVal()
obj3.printVal()

a = 2
b = a*4
print(b)
