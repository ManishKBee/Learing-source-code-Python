# python function to identify the greatest number from the given numbers

def great_num():
    n1=0
    if a>b:
        n1=a # '==' always symbolises equality which we use when need to assign a specific value to the variable for which the variable can be boolean and we use '=' to store a specific value in the variable for which the variable is equal to the value assigned
    else:
        n1=b # '==' always symbolises equality which we use when need to assign a specific value to the variable for which the variable can be boolean and we use '=' to store a specific value in the variable for which the variable is equal to the value assigned
    if n1>c:
        print("The Greatest NUmber is", n1)
    else:
        print("The Greatest NUmber is", c)

a=int(input("Enter The Number: "))
b=int(input("Enter The Number: "))
c=int(input("Enter The Number: "))

great_num()