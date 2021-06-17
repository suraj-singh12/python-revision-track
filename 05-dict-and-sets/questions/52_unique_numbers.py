print("Enter any 8 numbers:")
s = set()
for i in range(0,8):
    s.add(input())

print("The unique elements are: ", s)

s.add(18)
s.add("18")
print(s)

