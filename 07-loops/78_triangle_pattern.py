n = int(input("Enter the height of the triangle: "))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print('*',end='')
#     print()


# Easier method
for i in range(n):
    print("*" * (i+1))