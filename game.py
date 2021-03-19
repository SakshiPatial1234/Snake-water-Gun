import random


def gameWin(comp, b):
    if comp == b:
        return None

    elif comp == 's':
        if b == 'w':
            return False
        elif b == 'g':
            return True

    elif comp == 'w':
        if b == 'g':
            return False
        elif b == 's':
            return True

    elif comp == 'g':
        if b == 's':
            return False
        elif b == 'w':
            return True

print("Computer's:snake(s), water(w) or gun(g)")
randno = random.randint(1, 3)
if randno == 1:
    comp = 's'
elif randno == 2:
    comp = 'w'
elif randno == 1:
    comp = 'g'

b = input("Your Turn: Select snake(s), water(w) or gun(g)")
a = gameWin(comp, b)

print(f"Computer chose {comp}")
print(f"You chose {b}")
if a == None:
    print("The Game is Tie")
elif a:
    print("You win!!")
else:
    print("You,Lose!")
