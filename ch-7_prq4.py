num = int(input("enter the number\n"))
prime = True
for i in range(2, num):
    if(num%i == 0):
        prime=False

if prime:
    print(num, "is prime")
else:
    print(num, "is  not prime")