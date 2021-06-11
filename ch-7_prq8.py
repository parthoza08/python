n = int(input("enter the number\n"))
for i in range(n): 
    print(" " * (n-i-1), end="")#front space
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1))#back space 

    print(i, n)