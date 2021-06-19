
def sum(n):
    if(n==0):
        return 0
    else:
        return sum(n-1)+n
def main():
    n = int(input("Enter the range: "))
    print(sum(n))

if __name__ == "__main__":
    main()