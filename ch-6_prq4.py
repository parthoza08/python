usrname = input("enter your username\n")

if (len(usrname)>10):
    print("it contains more than 10 characters")
elif(len(usrname)==10):
    print("it contian 10 characters")
else:
    print("it contains less than 10 characters")