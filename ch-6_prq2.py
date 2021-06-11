m1 =int(input("enter 1st subject marks:\n"))
m2 = int(input("enter 2nd subject maks:\n"))
m3 = int(input("enter 3rd subject marks:\n"))

percent = (m1 + m2 + m3)/3

if (m1<33 or m2<33 or m3<33):
    print("you are fail due less than 33 marks in any subject")
elif (percent<40):
    print ("you are fialed due to low percentage")
else:
    print("congratulations! you passed this exam")