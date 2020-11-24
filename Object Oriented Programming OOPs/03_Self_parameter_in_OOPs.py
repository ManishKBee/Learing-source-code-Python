# self parameter in OOPs: what how and why of self

class EmployeeInfo:
    company="Google"
    '''def getSalary() this will show an error because 
    we haven't mentioned or given any instruction for 
    accepting agruments for our function getsalary() 
    but when we try pass an argument in our function 
    it show an error called <getsalary() takes 0 
    positional arguments but 1 was given>''' 
    def getSalary(self): 
        print(f"Salary of {self.name} who works in {self.company} is {self.salary}") # always use <self> for using the class or object attributes

'''<self> is a parameter which auto fill itself with 
the given argument in the object like we have define 
a method or function inside our class call 
getsalary(self) now when we make a new object (manish) 
of our class EmployeeInfo and use the function 
getsalary(self) then self parameter will auto replace 
itself with manish and give the output back'''

manish=EmployeeInfo()
manish.salary=f"Rs. {1.5} lakhs."
manish.name="Manish"
manish.getSalary()
# EmployeeInfo.getSalary(manish) this is back or internal processing of the above code
