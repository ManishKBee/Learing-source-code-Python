# python code to find if the student is present in the list or not

s1=input("Enter Name Of The Student: ")
s2=input("Enter Name Of The Student: ")
s3=input("Enter Name Of The Student: ")
s4=input("Enter Name Of The Student: ")
s5=input("Enter Name Of The Student: ")

list=[s1, s2, s3, s4, s5]

if (input("Enter The Name for The Search: ") in list):
    print("Present!!!")
else:
    print("Absent...")