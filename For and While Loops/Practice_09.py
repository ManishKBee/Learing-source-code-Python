# python code to print a pattern

# n=3
# for i in range(3):
#     print(" " * (n-i-1), end="")  
#     # print("*" * (2*i+1), end="")
#     print(" " * (n-i-1)) # maths is damn important for logic building

# n=3
# for i in range(3):
#     print("*"*n)
#     print(" "*(n-i-2), end="")
#     # print("*"*n)
#     # print("*"*n)

# number = int(input("Enter a number: "))

# j = 1
# for i in range(1,number+1):
#     print("  "*(number-i),"* "*j)
#     j +=2

number = int(input("Enter a number: "))

print("*"*number)
for i in range(3,number+1):
    space = (" "*(number-2))
    print("*" + space + "*")
print("*"*number)