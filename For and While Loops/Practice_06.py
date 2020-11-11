# python code to find the factorial of given number 
 
n=int(input("Enter The Number: "))

factorial = 1

for i in range(1, n+1):
    factorial = factorial * i
print(f"The Factorial of {n} is {factorial}")
