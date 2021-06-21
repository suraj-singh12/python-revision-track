class Employee:
    company = "Google"      # class instance
    salary = 100000         # class instance

striker = Employee()
michael = Employee()
print(striker.company)
print(striker.salary)
print()

michael.salary = 200000 # created a new instance attribute salary for michael.
# note class attribute- salary, and instance attribute- salary, both exist now
# but python first looks if the instance has the attribute or not
# if not it will go to check if class has that attribute
# if not then will throw an error 
print(michael.company)
print(michael.salary)

#print(michael.workingHours) # will throw error!, as neither michael(instance) has the 'workingHours' attribute nor the class has

michael.workingHours = 10       # here workingHours is instance attribute as can be seen clearly
print(michael.workingHours)
# print(striker.workingHours)     # will throw error!, as neither striker(instance) has the 'workingHours' attribute nor the class has