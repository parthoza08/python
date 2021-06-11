class Employe():
    def __init__(self, salary, increment):
        self.salary = salary
        self.increment = increment

    @property
    def salaryAfterIncrement(self):
        return f"you final salary is {self.salary * self.increment}Rs"

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sai):
        self.increment = sai/self.salary
sal= float(input("enter your salary:\n"))
inc = float(input("enter your increment:\n"))
e=Employe(sal, inc)
print(e.salaryAfterIncrement)