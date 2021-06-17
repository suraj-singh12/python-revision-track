sub1 = int(input("Enter marks in subject1: "))
sub2 = int(input("Enter marks in subject2: "))
sub3 = int(input("Enter marks in subject3: "))

avg = (sub1 + sub2 + sub3)/3
if(sub1>33 and sub2>33 and sub3>33 and avg > 40):
    print("Pass")
else:
    print("Fail")