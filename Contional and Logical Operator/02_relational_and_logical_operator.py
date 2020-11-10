# Logical and Relational Operators

'''A1. Relational operators: these operator defines
the programming relation between data type 
and valiable in the code.
Example: 01. "==" this defines the equqlity 
of the variable to the data type like we say 
a=12 and in the next line we code if a==12 
then print YES or print NO then we can run the 
code and see that it will print YES as a is 
assigned 12 and it's equality is equal to 
12 therefore it print YES if the equality 
assinged to a is not equql to 12 then it would 
print NO.
02. ">=" more than equal to it's used when we 
want to show a relation of more than equql
between the variable and data type
03. "<=" less than equal to it's used when we 
want to show a relation of less than equql
between the variable and data type
04. "!=" not equal to it's used when we want 
to show a relation bwtween varialbe and data 
type such that variable is not equal to the 
data type input. and there are many more 
relation operators can find them on 
python .org or docs.
A2. Logical operator: 01. "and" this is used 
when we want the condition to be only true 
when both variables in the program are true 
for the given data type.
02. "or" this is used when we want the 
condition to be true when either of the 
variables in the program are true for the 
given data type.
03. "not" this is used when we want the 
condition to be true when the given variable 
in the program is false for the given data 
type. and there are many logical operators 
can find them on python .org or docs.'''

print("Find Your Name Prefix!!!")

name=input("Enter Your Name: ")

print("Hello", name.capitalize())

age=int(input("Enter Your Age: "))
gder=input("Enter Your Gender: ")
mryorsgle=input("Enter Your Marrital status: ")

if (gder=="male"):
    if (age>=18):
        if (mryorsgle=="single"):
            print("Your Name Prefix is: Mr.")
        elif (mryorsgle=="married"):
            print("Your Name Prefix is: Mr.")
    elif (age<18):
        if (mryorsgle=="single"):
            print("Your Name Prefix Is: Master")
        elif (mryorsgle=="married"):
            print("Byah Ho Gya Tumhara: Mr.")

elif (gder=="female"):
    if (mryorsgle=="married"):
        print("Your Name Prefix is: Mrs.")
    else:
        print("Your Name Prefix Is: Miss")

print("Done!!!")

# "is" and "in" in python program

# 01. "is" it's similar to equality "==" operator in relation operators

HiIs=None

if(HiIs is None):
    print("NONE")
else:
    print("FULL")

# 02. "in" it's used we we want to find a item in list and if the item is present in this list then it prints True and it will print False if the item is not present in the list

HiIn=[12,45,67,89]

print(12 in HiIn)
print(72 in HiIn)