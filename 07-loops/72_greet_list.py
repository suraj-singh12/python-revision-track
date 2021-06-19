# doing using for loop
l1 = ["Suraj","Tarun","Sachin","Pratap"]
for name in l1:
    if name[0].lower()=='s':
        print("Hi!,",name)

print()
# doing using while loop
i = 0
while i < len(l1):
    if l1[i][0].lower() == 's':
        print("Hi!,",l1[i])
    i = i+1


print()
# BETTER WAYS
for name in l1:
    if name.lower().startswith('s'):
        print("Hi!, {}".format(name))

print()

i = 0
while i < len(l1):
    if l1[i].lower().startswith('s'):
        print("Hi!, {}".format(l1[i]))
    i = i+1