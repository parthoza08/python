# sum=0
# num = int(input("enter how many no.s sum you want\n"))
# while(num > 0):
#        sum += num
#        num -= 1
# print("The sum is", sum)
def su(num):
    product = 1
    for num in range(1, num +1 ):
        product *= num 
        num-=1
    print(product)        


number = int(input("enter how many no.s sum you want\n"))

su(number)


