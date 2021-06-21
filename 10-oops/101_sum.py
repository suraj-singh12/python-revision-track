
class Arithmetic:
    def sum(self):
        return self.a + self.b

myNum = Arithmetic()
myNum.a = 56
myNum.b = 23
print(f"Sum of {myNum.a} and {myNum.b} is: ",myNum.sum())
