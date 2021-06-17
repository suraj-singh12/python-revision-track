n1 = int(input("Enter number1: "))
n2 = int(input("Enter number2: "))
n3 = int(input("Enter number3: "))
n4 = int(input("Enter number4: "))

if n1>n4:
    f1=n1
else:
    f1=n2

if n2>n3:
    f2=n2
else:
    f2=n3

if f1>f2:
    print(f1,"is the greatest.")
else:
    print(f2,"is the greatest.")

# if(n1>n2 and n1>n3 and n1>n4):
#     print(n1,"is greatest.")
# elif (n2>n1 and n2>n3 and n2>n4):
#     print(n2,"is greatest.")
# elif (n3>n1 and n3>n2 and n3>n4):
#     print(n3,"is greatest.")
# else:
#     print(n4,"is greatest.")
