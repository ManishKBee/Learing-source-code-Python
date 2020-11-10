# conditional exp. are criteria that we assign to our code which decides the execution of code or not in specific condition or case

con=int(input("Enter Your Number: "))

# if-elif-if ladder: it will always consider first true value to be only true in the whole lsdder without running the other parts of ladder which can be also true and satify the condition to become true for the statement or input 

# else is optional in if-elif-else ladder! 

if(con>20):
    print("The value of Entered number is greater than 20")
elif(con>40):
    print("The value of Entered number is greater than 40")
elif(con>60):
    print("The value of Entered number is greater than 60")
elif(con>80):
    print("The value of Entered number is greater than 80")
elif(con>100):
    print("The value of Entered number is greater than 100")
else:
    print("The value of Entered number is less than 100")

print("Done")

# multi if statements or conditions: it will always consider all the if condition as individual condition set and run all the sets before declearing true, Hence this will run all given conditions individually before printing true for all given conditions, and not by only considering one or few condition statement 

Con=int(input("Enter Your Number: "))

if(Con>20):
    print("The value of Entered number is greater than 20")

if(Con>40):
    print("The value of Entered number is greater than 40")

if(Con>60):
    print("The value of Entered number is greater than 60")

if(Con>80):
    print("The value of Entered number is greater than 80")

if(Con>100):
    print("The value of Entered number is greater than 100")
else:
    print("The value of Entered number is less than 100")

print("Done")

# Quick Check

a=22

if(a>9):
    print("Greater")
else:
    print("Lesser")

print("Done")

# Quick Quiz

print("The Legal age Test: Balik or NaBalik")

name=input("Enter Your Name: ")
print("Hello", name.capitalize())
gder=input("Enter Your Gender: ")
age=int(input("Enter Your Age: "))

if(gder=="male"):
    if(age>=18):
        print("Balik")
    else:
        print("NaBalik")

if(gder=="female"):
    if(age>=21):
        print("Balik")
    else:
        print("NaBalik")

print("Done!!!")