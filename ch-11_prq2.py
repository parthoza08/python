class Animals():
    pass


class Pets(Animals):
    pass

class dog(Pets):
    @staticmethod
    def bark():
        print("bow bow!!")

class cat(Pets):
    pass

e = dog()
e.bark()