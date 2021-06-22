from typing import final


class Vector:
    # constructor
    def __init__(self, vec):
        self.vec = vec

    # this function tells print() fn how to print a Vector() class's instance 
    def __str__(self):
        v = ''
        index=0
        for i in self.vec:
            v += f" {i}a{index} +"
            index += 1
        return v[:-1]

    # simple vector addition
    def __add__(self, vec2):
        if len(self.vec) != len(vec2.vec):
            print("Addition Failed!!, Unequal dimensions.")
            return None        
        newList=[]
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)

    # this does dot product of the vectors
    def __mul__(self, vec2):
        if len(self.vec) != len(vec2.vec):
            print("Dot Product Failed!!, Unequal dimensions.")
            return None
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i]*vec2.vec[i]
        return f" {sum}"

v1 = Vector([1,5,6])
v2 = Vector([6,7])
print(v1)
print(v2)

print(v1+v2)
print(v1*v2)