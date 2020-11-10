# python code to find the greatest of the four number entered by the user

n1=int(input("Enter Your 1st Number: "))
n2=int(input("Enter Your 2nd Number: "))
n3=int(input("Enter Your 3rd Number: "))
n4=int(input("Enter Your 4th Number: "))

print(max(n1, n2, n3, n4)) # without conditional statements or operators

if (n1>n4):
    g1=n1
    # print(str[n1]+"Greater than"+str[n4])
else:
    g1=n4
    # print(str[n4]+"Greater than"+str[n1])

if (n2>n3):
    g2=n2
    # print(str[n2]+"Greater than"+str[n3])
else:
    g2=n3
    # print(str[n3]+"Greater than"+str[n2])

if (g1>g2):
    print(str(g1) + " Greatest Number Entered")
else:
    print(str(g2) + " Greatest Number Entered")