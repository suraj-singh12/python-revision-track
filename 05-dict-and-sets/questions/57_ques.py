# Can you change the values inside a list which is contained in set s
s = {8,6,2,5,"Charlie", [1,3]}

# answer : The question is incorrect, as we cannot have a list in a set,
#          because lists are unhashable.

'''
Hashable objects are objects with a hash value that does not change over time. 
Examples of hashable objects are tuples and strings. 
Lists do not have an unchanging hash value. 
Their hash values can change over time. 
This means you cannot specify a list as a dictionary key, or an element of a set.
'''

'''
Python hash() The hash() method returns the hash value of an object if it has one. 
Hash values are just integers that are used to compare dictionary keys during a dictionary lookup quickly. Internally, hash() method calls __hash__() method of an object which is set by default for any object.
'''