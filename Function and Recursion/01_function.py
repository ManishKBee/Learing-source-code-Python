# funtions in python: there are two kinds of function in python 1st is in-built function and user define function

# 01. in built function are those functions which come along the python language and are pre-define in the language example: print(), range(), len() and etc functions.

# 02. user define function are those function which are not pre-define in the python language and it's define by the for specific tasks which are convert into function by the coder for the coder!!!
'''a function is a group of statements performing a 
specefic task.
when a program gets bigger in size and it's complexity
grows, it gets difficult for a programmer to keep 
track on which piece of code is doing what!!!
a function can be reused by the programmer in a given 
program any number of time.'''

'''argument (input name) given below would be change 
according to the problem statement's argument like 
for Ex. if we define a function name avg() which 
calculates the avrage of given numbers and run it 
for a list of calles 'a' then the argument would be 
avg(a).'''

'''Syntax: def name of the function(input name):
                here difine the task 
    'the above is also known as function defination'

now when you need the function just call the function 
by typing the name of the function() for revoking the 
function for executing the task assinged to it and we
call this process as call function!!!'''

# python code for user define function for find avrage by using def(this is to define any function) avg() function  

def avg():
    a=sum(marks)/len(marks)
    return a

marks=[78,89,91,87,95]
print(avg())

# Quick Quiz

def greet():
    return "Hello\nGreetings, "

name=input("Enter The Name: ")
print(greet(), name.capitalize()) # if you are printing the function the put your defination in <return> section as shown in this case

'''a function can have argument in it so that it can 
work with it to return values. the values are kept 
inside the parentheses() and the arguments in the 
funtion can vary according to the need of the function 
it can be 1 or more than 1 or as much you want'''

# default parameter value(dpv) is the value which we can set as default input name's value which will help us to avoid error if we don't input any value in the function

def greets(name="Mate"): # for (dpv) mention the parameter in the defination of the function like mentioned below print("string" + parameter)
    print("Hello\nGreetings, " + name)

greets() # if you're just revoking the function and have done all additional definings in the function defination than define the output using print() function as shown in this case 
