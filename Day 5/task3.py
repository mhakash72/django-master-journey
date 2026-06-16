class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b= b
    def add(self,a,b):
        return a + b 
    def subtract(self,a,b):
        return a - b
    def multiply(self,a,b):
        return a*b

a1 = Calculator(10,20)
print(a1.add(10,20))
print(a1.subtract(10,10))
print(a1.multiply(2,3))