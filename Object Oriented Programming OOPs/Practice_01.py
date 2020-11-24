# python code to create a class for storing information of rhe Employee or Programmer

'''1. storing inte information using __init__ constructor
class ProgrammerInfo:
    company="Microsoft"
    def __init__(self, name, salary, subunit):
        self.name=name # always assing or set the variable or variable attributes first before calling them in the function or method
        self.salary=salary # always assing or set the variable or variable attributes first before calling them in the function or method
        self.subunit=subunit # always assing or set the variable or variable attributes first before calling them in the function or method
        print("Programmer's Detail")

    def programmerDetail(self):
        print(f"Programmer's Name: {self.name}")
        print(f"Programmer's Salary: {self.salary}")
        print(f"Programmer's Subunit: {self.subunit}")

manish=ProgrammerInfo("Manish", f"{1.5} Lakhs", "Office 365")
manish.programmerDetail()'''

'''2. storing the information using OOPs without __init__ constructor'''
class ProgrammerInfo:
    company="Microsoft"
    def programmerDetail(self, name, salary, subunit):
        self.name=name # always assing or set the variable or variable attributes first before calling them in the function or method 
        self.salary=salary # always assing or set the variable or variable attributes first before calling them in the function or method
        self.subunit=subunit # always assing or set the variable or variable attributes first before calling them in the function or method
        print("Programmer's Detail")
        print(f"Programmer's Name: {self.name}")
        print(f"Programmer's Salary: {self.salary}")
        print(f"Programmer's Subunit: {self.subunit}")

manish=ProgrammerInfo()
manish.programmerDetail("Manish", f"{1.5} Lakhs", "Office 365")