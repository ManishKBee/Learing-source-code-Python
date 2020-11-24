# python code to make a calculator 

import math

'''without defining the variable attribute
class Calculator:
    def square(self):
        return self.number*self.number
    def cube(self):
        return self.number*self.number*self.number
    def square_root(self):
        return math.sqrt(self.number)

num=Calculator()
num.number=4
square=num.square()
print(square)
cube=num.cube()
print(cube)
square_root=num.square_root()
print(square_root)'''

'''with defined variable attributes'''
class Calculator:
    def square(self, number):
        self.number=number # variable attribute # always define the variable attribute inside the function or method which we've created inside the class
        print(f"Square Of The Number: {number*number}") # can also do the same by using arithmetic operator in python for exponent which is <**> for Square it's "number**2"
    def cube(self, number):
        self.number=number # variable attribute # always define the variable attribute inside the function or method which we've created inside the class
        print(f"Cube Of The Number: {number*number*number}") # can also do the same by using arithmetic operator in python for exponent which is <**> for cube it's "number**3"
    def square_root(self, number):
        self.number=number
        print(f"Square Root Of The Number: {math.sqrt(number)}") # can also do the same by using arithmetic operator in python for exponent which is <**> for Square Root it's "number**0.5"

num=Calculator()
num.square(4)
num.cube(4)
num.square_root(4)
