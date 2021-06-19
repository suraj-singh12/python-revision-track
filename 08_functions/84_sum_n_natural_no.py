def sum(n):
    if(n==0):
        return 0
    return sum(n-1)+n

n = int(input("Enter the number of terms: "))
print(f"Sum of first {n} natural numbers is: ", sum(n))