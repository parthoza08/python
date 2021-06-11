from ast import Num


class calculator:
    def __init__(self,number):
        self.number=number

    def square(self):
        print(f"the sqaure of {self.number} = {self.number**2}")

    def cube (self):
        print(f"the cube of {self.number}={self.number**3} ")

    def squareroot(self):
        print(f"the sqaureroot of the {self.number}={self.number**0.5} ")
    @staticmethod
    def greet():
        print("***done***")


what=input("enter function(sq, c, sr)")
Num=int(input("enter the number:\n"))
a = calculator(Num)
if what == "sq":
    a.square()
    a.greet()
elif what == "c":
    a.cube()
    a.greet()
elif what == "sr":
    a.squareroot()
    a.greet()

