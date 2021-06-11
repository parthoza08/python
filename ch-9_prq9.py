with open("file.txt") as F:
    F1 = F.read()

with open("copy.txt") as s:
    F2 = s.read()


if F1 == F2:
    print("both are same files")
else:
    print("not same")