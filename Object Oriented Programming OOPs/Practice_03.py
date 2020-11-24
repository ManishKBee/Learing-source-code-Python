# python code to chech class and instance or object attributes

class A:
    Aattribute="a" # class attribute 
    '''Aattribute="ae"''' # class attribute 
    '''if this is present then it 
    will be consider as class attribute as it's 
    the latest one of the same attribute'''
    
    def getAattribute(self):
        print(self.Aattribute)

obj=A()
obj.Aattribute="e" # object or instance attribute
print(f"Class Attribute: {A.Aattribute}")
print(f"Object Attribute: {obj.Aattribute}")

'''here we can see that intance or object atrribute 
will always have preferance over class attribute and 
when we create a same object attribute to the existing
class attribute then the program make a new object 
attribute without replacing or removing the existing 
class attribute'''