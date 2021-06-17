marks = []
for i in range(0,6):
    m = int(input("Enter marks of student "+str(i+1)+" : "))
    marks.append(m)

marks.sort()
print("Sorted marks are: ")
print(marks)