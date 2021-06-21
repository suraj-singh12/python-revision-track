import random

def game():
    r = random.random()
    r = int(r*100)
    return r

score = game()
try:
    fi = open("history.txt",'r')
except:
    with open("history.txt",'w'):
        pass

with open("history.txt",'r') as f:
    high_score = f.read()

if high_score=='':
    with open("history.txt",'w') as f:
        f.write(str(score))
elif int(high_score) < score:
    with open("history.txt",'w') as f:
        f.write(str(score))
        print("Your Score is: {} and HIGHEST!!".format(score))
else:
    print("The highest score is {}".format(high_score))
