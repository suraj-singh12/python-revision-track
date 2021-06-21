import math

class Calculator:
    def square(self):
        return self.number*self.number
    def cube(self):
        return self.number*self.number*self.number
    def sqr_root(slfgf):                # see it is not necessary that we always write self, we can use any word here
        return math.sqrt(slfgf.number)      # see 

obj = Calculator()
obj.number=49
print("Square root of {} is {}".format(obj.number, obj.sqr_root()))
print("Square of {} is {}".format(obj.number, obj.square()))
print("Cube of {} is {}".format(obj.number, obj.cube()))
