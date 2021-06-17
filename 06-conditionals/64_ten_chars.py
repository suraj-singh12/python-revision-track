username = input("Enter username: ")
if (len(username) < 10):
    print("Error!!",username,"is less than 10 characters long.")
else:
    print(username,"meets conditions.")