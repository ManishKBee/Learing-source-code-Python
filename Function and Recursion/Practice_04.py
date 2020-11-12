# python code to find sum of first "n" natural given

def sum_recursive(n): # always specify the variable in recursion function at the time of naming the function inside the '(parentheses)'!!!
    if n==0:
        return 0
    return n+sum_recursive(n-1)

n=int(input("Enter The Number: "))
print("Sum of given 'n' Numbers:", sum_recursive(n))