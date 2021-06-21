class Employee:
    company = "Google"

    # def __init__(self):
    #     print("Hi!!, I am constructor.")
    #     print("I am automatically called whenever an object is created.")
    #     print("Object created")

    def __init__(self, name="", salary="", subunit=""):
        self.name=name
        self.subunit=subunit
        self.salary=salary
        print("Object successfully created.")
    
    def printDetails(self):
        print(f"Hello {self.name}")
        print(f"Your company is: {self.subunit}")
        print(f"Your salary is: {self.salary}")


emp1 = Employee()
emp1.name = "Michael"
emp1.salary=120000
emp1.subunit="YouTube"
emp1.printDetails()

print()
emp2 = Employee("Fury",150000,"Google Cloud")
emp2.printDetails()