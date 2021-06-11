def game ():
    pass
usrscore = int(input("enter your score\n"))
with open("highscore.txt") as f:
    hiscore=f.read()

if hiscore=="":
    with open("highscore.txt", "w") as new:
        new.write(str(usrscore))

    print("congo got first highscore", usrscore)

elif usrscore>int(hiscore):
    with open("highscore.txt", "w") as new:
        new.write(str(usrscore))

    print("you got highscore" , usrscore)
else:
    print("try next time")

