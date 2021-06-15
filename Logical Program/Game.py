# Program for Z pattern
'''
    Author : Samadhan Gaikwad.
    Software Developer
    Location: Pune.
'''
import random


def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == "s":
        if you == "w":
            return False
        elif you == 'g':
            return True
    elif comp == "w":
        if you == "g":
            return False
        elif you == 's':
            return True
    elif comp == "g":
        if you == "s":
            return False
        elif you == 'w':
            return True

a = random.randint(1, 3)
if a == 1:
    comp = 's'
elif a == 2:
    comp = 'w'
else:
    comp = 'g'
print("Computer turn : Snake(s) Water(w) or Gun(g)? ")
you = input("Your turn : Snake(s) Water(w) or Gun(g)? ")
result = gameWin(comp, you)
print(f"Computer choosen {comp}")
print(f"Computer choosen {you}")
if result == None:
    print("The game is tie...")
elif result:
    print("You win the game....")
else:
    print("You lose the game....")
