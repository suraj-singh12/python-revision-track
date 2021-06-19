
def print_sqr(n):
    print("*" * n)
    for i in range(n-2):
        print("*",end = "")
        print(" " * (n-2),end="")
        print("*")
    print("*" * n)

n = int(input("Enter the number of rows: "))
while n==1 or n==2:
    print("Enter a value greater than 2 !!")
    n = int(input("Enter the number of rows: "))
print_sqr(n)