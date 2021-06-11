# a.b=a1a2+b1b2+c1c2

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

class Dotproduct(vec3d):
     def __init__(self, i, j, k, i2, j2, k2):
         super().__init__(i, j, k)
         self.i2 = i2
         self.j2 = j2
         self.k2 = k2
         
         

     def dotProduct(self):
        return f" {i*i2}i + {j*j2}j + {k*k2}k "
     
     


        
i=int(input("enter icap:\n"))
j=int(input("enter jcap:\n"))
k=int(input("enter kcap:\n"))
i2=int(input("enter i2cap:\n"))
j2=int(input("enter j2cap:\n"))
k2=int(input("enter k2cap:\n"))



d= Dotproduct(i, j, k, i2, j2, k2 )
print(d)