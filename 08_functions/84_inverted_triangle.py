def inv_tri(n):
    for i in range(n,0,-1):
        print("*"  * (i))

n = int(input("Enter the number of rows: "))
inv_tri(n)