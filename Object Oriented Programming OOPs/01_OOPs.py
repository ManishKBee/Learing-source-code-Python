# object oriented programming or OOPs

'''solving a problem statement by creating object is 
one of the most popular approaches in programming. 
this is called object oriented programming.

this concept focuses on code reusability
        |->implements DRY principle
                        |->don't repeat yourself'''

'''class: class is a blueprint for creating a object 
and class doesn't take space in memory or doesn't 
take instance in memory by itself.

contain info to create a vaild application <-[blank form] =>filled by a Person =>[blank form converts into an application for that Person]

contain info to create a vaild object <-[class] =>object instantiation => [class converts into an object for that instantiation]'''

'''1. PascalCase: EmployeeName, MyName, YourName
-> classes are usually written in PascalCase!
2. camelCase: employeeName, myNmae, yourName'''

class Number:
    def sum(self): # [this is encapsulation of methods and variable for this class as it will only functionale while using this class for creating an object] this is the defined method for this class and the methods are written in camelCase.
        return self.a+self.b # [this is encapsulation of methods and variable for this class as it will only functionale while using this class for creating an object] this is the defined variable for this class.

'''syntax of class: class <"ClassName">:
                        Method and variables'''

newNum=Number() # this is object instantiation after which class are able to store itself in the memory space and the variable for oblect instantiation are written in camelCase.

'''objects: an object is an instantiation of a class.
when a class is define, only the template or info is 
defined which doesn't take any space in memory. memory 
is allocated only after object instantiation.

object of a given class can make the methods available
to it without revealing the implementation details to 
the user. -> [Abstraction and Encapsulation]'''

newNum.a=12
newNum.b=34
s=newNum.sum() # Abstraction in how does this method returns this output
print("The sum of a and b is:", s)

a=12
b=34

print("The sum of a and b is:", a+b)
