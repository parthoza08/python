class programmer():
    company = "microsoft"
    Salary = 30

    def __init__(self, name, company) :
        self.name=name
        self.company=company
        print(name, company)
    

    def getinfo(self):
        print(f"hey, {self.name} is working in {self.company} ") 
    

harry= programmer("harry", "microsoft")
harry.getinfo()
    