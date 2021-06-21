import random

def win(comp,player):
    if comp == player:
        return None
    if comp == 's':
        if player == 'w':
            return False
        else:
            return True
    elif comp == 'w':
        if player == 'g':
            return False
        else:
            return True
    elif comp == 'g':
        if player == 's':
            return False
        else:
            return True

comp = random.randint(1,3)
print("Computer's Turn: Snake(s) Water(w) Gun(g)? ")
if comp == 1:
    comp = 's'
elif comp == 2:
    comp = 'w'
else:
    comp = 'g'

player = input("Player1's Turn: Snake(s) Water(w) Gun(g)? ")

print("You entered: ",player)
print("Computer entered: ", comp)

result = win(comp,player)
if result is None:
    print("Tie!!")
elif result == True:
    print("You WON!")
else:
    print("You Lose!")