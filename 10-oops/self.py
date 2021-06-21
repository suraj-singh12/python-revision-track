class Employee:
    company = "Google"
    def getSalary(self):
        print(f"{self.name} your salary is : {self.salary}")
    
    def greet():
        print("Welcome Back!!")

    @staticmethod
    def greet2():
        print("Welcome Back!!")

        
michael = Employee()
michael.salary=120000
michael.name="Michael"
michael.getSalary() # michael.getSalary() -> Employee.getSalary(michael)
                                                    # that's why parameter self is required.

# michael.greet() # gives error: greet() takes 0 positional arguments but 1 was given
                # because michael.greet() -> Employee.greet(michael)

                # but why do we need to have self in a function like greet? it is not using any value from instance
                # so in such cases we make static methods not normal ones
                # check greet2() method

michael.greet2()     # Employee.greet()
                # since greet() is a static method, so interpreter will convert this in this way
 