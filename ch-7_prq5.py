# sum = 1 + 2 + 3 +4 ... n
# sum(n)= sum(n-1) + n 
# sum(4) = 1 + 2 + 3 + 4 = 10

sum=0
num = int(input("enter how many no.s sum you want\n"))
while(num > 0):
       sum += num
       num -= 1
print("The sum is", sum)