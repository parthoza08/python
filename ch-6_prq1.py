num1 = input("enter 1 number:\n")
num2 = input("enter 2 number:\n")
num3 = input("enter 3 number:\n")
num4 = input("enter 4 number:\n")

if(num1>num4):
     F1 = num1
else:
    F1 = num4 
if (num2>num3):
     F2 = num2 
else:
     F2 = num3

if (F1>F2):  
    print("the greatest of four is", F1)  
else:
    print("the greatest of four is", F2)