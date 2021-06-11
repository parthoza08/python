

def star(num):
    for i in range(0,num):
        print(" * " * num )
        num = num-1

n = int(input("enter the numaber: \n"))
star(n)