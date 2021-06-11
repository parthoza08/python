'''
class C2dVec:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"

class C3dVec(C2dVec):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k
    
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"
    
    
v2d = C2dVec(1, 3)
v3d = C3dVec(1, 9, 7)
print(v2d)
print(v3d)


'''
class vec2d():
    
    def __init__(self, i, j):
        self.icap= i 
        self.jcap= j
        
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"

class vec3d(vec2d):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap=k


    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k "
        
i=int(input("enter icap:\n"))
j=int(input("enter jcap:\n"))
k=int(input("enter kcap:\n"))

e= vec2d(i, j)
f= vec3d(i, j, k)
print(e)
print(f)
