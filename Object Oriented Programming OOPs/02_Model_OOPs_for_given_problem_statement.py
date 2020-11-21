# python code to model objects for solving the given problem statement

# where to start: modelling the OOPs for the problem.
'''we find the following info. from our problem 
statement (for the given case of employee):
[Noun]------>[Class]------>[Employee]
[Adjective]->[Attributes]->[name, age, salary]
                |->[class attributes]
 =>Characteristic which are specific to the class!
                |->[instance or object attributes]
  =>Characteristic which are specific to the instance!
[Verb]------>[Methods]---->[crsalary(), ctc()]'''

class EmployeeInfo():
    company="Google" # these all are class attributes for this given class EmployeeInfo
    salary=500 # these all are class attributes for this given class EmployeeInfo
    departmentId=f"GE{450}" # these all are class attributes for this given class EmployeeInfo
    hodName="Humpty" # these all are class attributes for this given class EmployeeInfo
    departmentFloor=f"Floor No. {3}" # these all are class attributes for this given class EmployeeInfo

abhay=EmployeeInfo()
manish=EmployeeInfo()
javed=EmployeeInfo()

print(javed.company)
print(manish.company)
print(abhay.company)

EmployeeInfo.company="YouTube" # here we have updated the company name in class atributes

print(javed.company) # this will print the updated company name for the class attributes 
print(manish.company) # this will print the updated company name for the class attributes 
print(abhay.company) # this will print the updated company name for the class attributes

javed.salary=550 # these are the instance attribute for this given object
abhay.salary=450 # these are the instance attribute for this given object

print(abhay.salary)
print(manish.salary)
print(javed.salary)

'''*Note: instance attributes haves preference over class 
attributes during assignment and retrival.
for Example if call salary attribute(adjective) in our 
class then our class will ask two questions:
    1. is attribute present in instance or object?
    -> if No, then the 2nd question will be asked
    -> if Yes, then it will directly return the object 
    attribute without asking the the 2nd question
    2. is attribute present in class?
    -> if Yes, then it will return the class attribute
    -> if No, then it will show an "error" called 
    <class name> object has No attribute <attribute title>'''
