# python code find the grade of a student from the given grade scheme

name=input("Student's Name: ")

print("Entering Marks Of", name.capitalize())

marks=int(input("Enter The Marks: "))

if (marks>=91):
    print("Grade Secured: 'O'")
elif (marks>=81):
    print("Grade Secured: 'A'")
elif (marks>=71):
    print("Grade Secured: 'B'")
elif (marks>=61):
    print("Grade Secured: 'C'")
elif (marks>=51):
    print("Grade Secured: 'D'")
elif (marks<50):
    print("Grade Secured: 'F'")