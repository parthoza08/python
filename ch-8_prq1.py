a = int(input("enter 1st no.\n"))
b = int(input("enter 2nd no.\n"))
c = int(input("enter 3rd no.\n"))
F = "x"
if a>b:
    F = a
else:
     F = b

if F > c:
    print(F, "is the greatest no.")
else:
    print(c, "is the greatest no.")

