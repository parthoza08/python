# fact(n) = 1 x 2 x 3 x 4 x n 
# fact(4) = 1 x 2 x 3 x 4 = 24
# product = 1
# num = int(input("enter the number \n"))
# while num > 0 :
#     product *= num 
#     num -= 1

# print(product)



num = int(input("enter the number"))
product = 1

for num in range(1, num +1 ):
    product *= num 
    num-=1

print(product)