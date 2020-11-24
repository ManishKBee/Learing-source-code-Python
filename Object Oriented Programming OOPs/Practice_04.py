# python code to make a calculator with static method greet to wish

import math
import datetime

'''without defining the variable attribute
class Calculator:
    def square(self):
        return self.number*self.number
    def cube(self):
        return self.number*self.number*self.number
    def square_root(self):
        return math.sqrt(self.number)
    @staticmethod
    def greet():
        print("Good Morning")

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
        print(number*number)
    def cube(self, number):
        self.number=number # variable attribute # always define the variable attribute inside the function or method which we've created inside the class
        print(number*number*number)
    def square_root(self, number):
        self.number=number
        print(math.sqrt(number))
    @staticmethod
    def greet(greeting):
        print(f"Hello, Prof\n{greeting}")

def greeting():
    hour=int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        return("Good Morning")
    elif hour >=12 and hour<17:
        return("Good Afternoon")
    else:
        return("Good Evening")

num=Calculator()
num.greet(greeting())
num.square(4)
num.cube(4)
num.square_root(4)
