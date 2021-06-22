class Complex:
    def __init__(self, real=0, imag=0):
        self.real=real
        self.imag=imag
    
    def __add__(self, c2):      # overloaded + operator
        c = Complex()
        c.real = self.real + c2.real
        c.imag = self.imag + c2.imag
        return c
    
    def __mul__(self, c2):      # overloaded * operator
        c = Complex()
        c.real = self.real * c2.real - self.imag * c2.imag
        c.imag = self.real * c2.imag + self.imag * c2.real
        return c
    
    def __str__(self):
        if self.imag>=0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {-self.imag}i"

c1 = Complex(-5,6)
print(c1)
c2 = Complex(-6,7)
print(c2)

c3 = c1+c2
print(c3)

c4 = c1*c2
print(c4)
