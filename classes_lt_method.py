# defining class

class Foobar:
    def __init__(self, numb):
        self.numb = numb        # the value of the parameter sent via numb is stored in method variable numb

    def __lt__(self, other):
        return self.numb < other.numb   # rich comparision between two objects and their member variables


obj1 = Foobar(1)
obj2 = Foobar(2)




