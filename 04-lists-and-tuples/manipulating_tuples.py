# lists are immutable data types in python
t = (1,3)
print(t)
# t[0]=10 # raises error
print()

l = list(t)
print(l)
l[0] = 10
print(l)
print()

t = tuple(l)
print(t)