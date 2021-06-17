letter = '''Dear <|NAME|>
This is to inform you that
You are selected. 
Congratulations!!
Date: <|DATE|>'''

name = input("Enter your name : ")
dt = input("Enter date: ")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", dt)
print()
print(letter)