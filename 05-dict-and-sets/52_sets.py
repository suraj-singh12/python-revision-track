# a set is a collection of non repeatitive elements.
'''
Properties of Sets:
1. unordered
2. unindexed
3. there is no way to change items in sets
4. sets do not contain duplicate values
'''  
s = {1,2,3,5,1,3}
print(s)
print(type(s))


s2 = set()
print(type(s2))
s2.add(9)
s2.add(9)
s2.add(5)
# s2.add([4,5,6])     # a list can't be added to a set because it can be modified later
# s2.add({1:2})       # similarily dictionary can't be added
s2.add((4,5,6))     # but a tuple can be added, as it can't be modified

print(s2)
print(len(s2))

s2.remove(5)
print(s2)

print(s2.pop()) # removes any random element from the set and prints it
print(s2)
s2.add(1)

print(s2.union(s))    # prints the union of sets as a new set
print(s2.intersection(s))   # prints the intersection of sets as a new set