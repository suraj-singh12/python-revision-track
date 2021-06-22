class Employee:
    company="Google"

    def printDetails(self):
        print("Hello Employee")
    
    def getCompany(self):
        print(f"Your company is: {self.company}")


class Programmer(Employee):     # Programmer class has inherited the Employee class
    language="Python"
    
    def getLanguage(self):
        print(f"The language is: ",self.language)
    
    def printDetails(self):
        print(f"Hello {self.language} Programmer")


e = Employee()
p = Programmer()

e.printDetails()
p.printDetails()
p.getCompany()
p.getLanguage()

