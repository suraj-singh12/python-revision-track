# Prime: if a number is not divisible by any number from 2->sqrt(num) then it is a prime number
# we take it 2->int(sqrt(n))+1 ; +1 because it may be n is number like 6.78 which is to be taken as 7 
# but int will truncate it to 6, so we add +1 to take such cases
# This logic is an efficient logic to find a number is prime or not
import math

n = int(input("Enter a number: "))

for i in range(2, int(math.sqrt(n))+1 ):
    if n%i==0:
        print("{} is NOT a prime number.".format(n))
        break
else:
    print("{} is a prime number.".format(n))
