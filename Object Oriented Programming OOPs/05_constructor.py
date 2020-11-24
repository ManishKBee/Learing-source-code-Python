# constructor in python code help us initiate our defined function in a created class by showing or returing the ginven vlue for the function

class EmployeeInfo: # constructor gives our class the ability to accept mentoned argument in the defined constructor function
    company="Google"
    def getSalary(self, sign): # we can have multiple parameters in or method or function
        print(f"Salary of {self.name} who works in {self.company} is {self.salary}\n{sign}") # always use <self> for using the class or object attributes

    def __init__(self, name, salary, subunit): # this will be printed first whenever we run this code without even calling it as it initiates the methods or functions set inside the class created 
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("Hello. \nNew Object: Employee being Created or Hired!")

    def EmployeeDetail(self):
        print(f"Name of the Employee: {self.name}")
        print(f"Salary of the Employee: {self.salary}")
        print(f"Subunit of the Employee: {self.subunit}")

    @staticmethod
    def greet():
        print("Greetings, Prof")

manish=EmployeeInfo("Manish", f"{1.5} Lakhs", "Youtube")
manish.greet()
manish.getSalary("Thank You") # EmployeeInfo.getsalary(manish) is the internal processing of this given code
manish.EmployeeDetail()