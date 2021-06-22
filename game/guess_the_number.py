import random

print("----------------------------------------")
print("          GUESS THE NUMBER              ")
print("----------------------------------------")

name = input("Enter your name: ")
print(f"Hello {name}, Welcome to the Guess The Number Game")

is_ready = input("\nAre you ready?(y/n) ")
print()

if is_ready == 'y':
    r = random.randint(1,100)       # generates random number between [1,100]
    attempts=0

    while True:
        inp = input("Guess a number between 1 and 100 [1,100]: ")

        # ensuring the entered number is integer, also ensuring that the program doesn't break on invalid inputs
        try:
            inp = int(inp)  # if ok, next line, otherwise go to except block
            break           # will be executed only if above line executes safely
        except: 
            while True:
                print("Oops!!, you entered something wrong. Try again.\n")
                inp=input("Guess a number between 1 and 100 [1,100]: ")
                try:
                    inp = int(inp)
                    break
                except:
                    continue

        attempts += 1

        if inp==r:
            # congratulate for right guess
            print("-------------------------------------------------")
            print(f"\nHurray!!, Great guess, yes the number is {inp}")
            print(f"You guessed it right in {attempts} attempts.")

            # see if it was in lowest attempt, overwrite the high score in file
            try:                                 # check if the file is present or not
                f = open("high_score.txt","r")
                
                # if present then
                high=f.readline()
                f.close()

                if high == '' or attempts < int(high):        # if file empty or less attempts then store it as high score
                    f = open("high_score.txt","w")
                    f.write(str(attempts))
                    f.close()
                    print(f"It was the highest score. Congratulations {name} !!")
           
            except:                               # create the file if not present
                f = open("high_score.txt","w")  # create
                f.write(str(attempts))          # write present score
                f.close()                       # close
            
            # continue?
            print("-------------------------------------------------")
            is_ready = input("\nWant to continue?(y/n) ")
            if is_ready == 'y':
                r = random.randint(1,100)       # generates random number between [1,100]
                attempts=0
                continue
            else:
                print(f"\nHave a nice day ahead {name} !!")
                print("Exiting ...")
                break

        else:
            print("A aa!!, it wasn't a right guess.")
            if r>inp:
                print("Guess a bigger one.\n")
            else:
                print("Guess a smaller one.\n")
else:
    print("Exiting")
