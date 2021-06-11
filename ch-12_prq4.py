import sys # a biuld in module 
try:
    a=int(input("enter 1st no.:\n"))
    b=int(input("enter the second no.:\n"))
except Exception:
    sys.exit  #in sys module there is fuction of exit so we can exit by this code
    

try :
    c=a/b
    print(c)
except ZeroDivisionError:
    print("infinite")
except :
    print("invalid input")




