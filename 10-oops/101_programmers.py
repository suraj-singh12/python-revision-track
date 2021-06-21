class Programmers:
    company = "Microsoft"
    def __init__(self, name, field):
        self.name=name
        self.field=field
    def printDetails(self):
        print(f"Name: {self.name}")
        print(f"Company: {self.company}")
        print(f"Field: {self.field}")
        print()

prog = [
        Programmers("Fury","Software Engineering"),
        Programmers("Nick","Hardware Engineering"),
        Programmers("Banner","Hardware Engineering"),
        Programmers("Tony","Software Engineering")
    ]
for programmer in prog:
    programmer.printDetails()

