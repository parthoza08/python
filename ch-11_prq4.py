# (a+bi)(c+di) = ac + adi + bci + bdi2
# (a+bi)(c+di) = (acâˆ’bd) + (ad+bc)i

# class Complex:
#     def __init__(self, r, i):
#         self.real = r 
#         self.imaginary = i

#     def __add__(self, c):
#         return Complex(self.real + c.real, self.imaginary + c.imaginary)
    
#     def __mul__(self, c):
#         mulReal =  self.real*c.real - self.imaginary*c.imaginary
#         mulImg =  self.real*c.imaginary + self.imaginary*c.real
#         return Complex(mulReal, mulImg)

#     def __str__(self):
#         if self.imaginary<0:
#             return f"{self.real} - {-self.imaginary}i"
#         else:
#             return f"{self.real} + {self.imaginary}i"

# c1 = Complex(1, -4)
# c2 = Complex(331, -37)
# print(c1 + c2)
# print(c1 * c2)



class complex():
    def __init__(self, a, bi, c, di):
        self.a=a
        self.bi=bi
        self.c=c
        self.di=di

    def multiplyComplex(self):
        return print((self.a * self.c)+ str(self.a*self.di)+"i" +str(self.bi*self.c)+"i"+ (self.bi*self.di)  )



***********************not able to understand**************************