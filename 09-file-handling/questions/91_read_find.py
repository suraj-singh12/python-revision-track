try:
    file = open("myfile.txt","r")
except IOError:
    print("Error opening the file!!")
    exit()

file = file.read()
file = file.lower()     # converting all read content into lowercase, as we are ignoring the case in finding the word, 
                        # i.e. for us twinkle and Twinkle are same
word = "twinkle"

if word in file:
    print(f"YES!, {word} exists in the file.")
else:
    print(f"NO!, {word} does NOT exists in the file.")
