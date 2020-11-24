# python code to implement @staticmethod which allows us run a function

import datetime

class EmployeeInfo:
    company="Google"
    def getSalary(self, sign): # we can have multiple parameters in or method or function
        print(f"Salary of {self.name} who works in {self.company} is {self.salary}\n{sign}") # always use <self> for using the class or object attributes

    '''<@staticmethod>
    this set an instrution or rule that had to be 
    followed in order to run this code file the 
    insturtion or the rule is don't pass <self> as a 
    auto parameter in this code but we can set other 
    parameters in this insturtion other than <self> 
    parameter'''

    @staticmethod # Decorator to mark <greet> as a ststic method
    def greet(greeting, time): # (greeting) inside this is a parameter which is accepted by this method as an argument
        print(f"Hello, Prof\n{greeting}\n{time}")

def greeting(): # greeting() here is a defined function which will auto wise according to the time of the day 
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        return("Good Morning") # use return in place of print() function inside the defined function for returning the required value or string in place of printing the the values or strings. 
    elif hour>=12 and hour<17:
        return("Good Afternoon") # use return in place of print() function inside the defined function for returning the required value or string in place of printing the the values or strings.
    else:
        return("Good Evening") # use return in place of print() function inside the defined function for returning the required value or string in place of printing the the values or strings.

def time():
    # time=datetime.datetime.now().time() this will store the current time of the system into the given vesel in this case in time. the time will be stored in full format like hour:minute:second:microsecond
    hour=datetime.datetime.now().hour
    minute=datetime.datetime.now().minute
    return f"Current Time: {hour}:{minute}"
    # return f"Current Time: {time}" this will return the values stored in time

manish=EmployeeInfo()
manish.salary=f"Rs. {1.5} lakhs."
manish.name="Manish"
manish.greet(greeting(), time())
manish.getSalary("Thank You") # EmployeeInfo.getsalary(manish) is the internal processing of this given code
