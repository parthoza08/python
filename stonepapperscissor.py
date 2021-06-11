import random

def whowins(comp, you):
    if comp==you:
        print("the game is tie")
    elif comp == "s" :
        if you == "p":
            print("you won!")
        elif you == "sc":
            print("you loose")
    elif comp == "p":
        if you == "s":
            print("you loose")
        elif you == "sc":
            print("you won!")

    elif comp == "sc":
        if you == "s":
            print("you won!")
        elif you == "p":
            print("you loose")


randomno=random.randint(1, 3)
if randomno==1:
    comp="s"
elif randomno == 2:
    comp="p"
elif randomno == 3:
    comp = "sc"


you = input("your turn: stone(s), papper(p),  scissor(sc)\n")



print("comp chooce ", comp)
print("you chooce", you)

whowins(comp, you)