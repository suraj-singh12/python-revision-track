# Factorial is represented by ! eg 5! and is defined like this:
# n! = n*(n-1)*(n-2)*(n-3)*.....*1
# 5! = 5*4*3*2*1

n = int(input("Enter the number: "))
fact = 1
for i in range(1,n+1):
    fact = fact*i
# print("Factorial of {} is {}".format(n,fact))
print(f"The factorial of {n} is {fact}")