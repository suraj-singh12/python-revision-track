# nice

def max(n1,n2,n3):
    if n1>n2:
        if n1>n3:
            return n1
        else:
            return n3
    elif n2>n3:
        return n2
    else:
        return n3

n1 = int(input("Enter the number1: "))
n2 = int(input("Enter the number2: "))
n3 = int(input("Enter the number3: "))
print(max(n1,n2,n3))
