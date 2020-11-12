# recursion is kind of function which revoke itself because we use direct mathamatics formula in it's difining process

'''n!=1*2*3*4*5...*n: the product of first n natural 
numbers is the factorial of nth number. 
1! = 1 and 0! = 1 defined by mathamatician
if we see 4!=4*3*2*1 and 3!=3*2*1 we found that 4! 
have 3! built or comprised into it from that we can
state 4!=4*3! which is equal to "n*(n-1)!"'''

# factorial using for loop

n=4
product=1
for i in range(n):
    product=product*(i+1)

print(product) # always print the output outside the loop statement for obtaining only the final output and not stacking with the step or range output for the final output but if you want the final output with range or step for reaching the final uotput then set or place the print() function inside loop statement!!!

# factorial using loop inside user define function

def factorial_iter(n): # iter is iterative factorial method
    product=1
    for i in range(n):
        product=product*(i+1)
    return product

print(factorial_iter(5))

# factorial using recursion or direct formula for factoral

def factorial_recursive(n): 
    if n==0 or n==0: # this is known as base condition as it will stop revoking of recursion when the base condition becomes 'True' for the value of "n" or any other variable which we have assumed
        return 1
    else: # using else statement is optional for this case but remember that it works fine with and without else statement
        return n*factorial_recursive(n-1) # this is the main recursion condition which will revoke itselt till the recuesive condition become 'False' for the value of "n" or any other variable which we have assumed
    # return n*factorial_recursive(n-1) this also works fine in this problem case!!!

print(factorial_recursive(4)) # basical when we define value of 'n' in the function then it follows the formula of factorial "n*(n-1)!" till 'n' become 1 than it pass 'n' through if statement and it returns 1 as we have hard coded it into the program and eventually 'n' becomes 0 for which the fuction repeat the process of 1! again but this time it's for 0! which is equal to 1 obvio!!!

'''> recursion is only used when we can see a direct 
mathamatic formula represent the problem statement 
given. 
> it's not recommended to always use recursion to solve 
a given problem as recursion needs a niches mathamatic 
formula to sucessfully execute the solution for the 
given problem stamentment.
> we need to be extremely careful while working with 
recursion to ensure that the function doesn't 
infinitely keep calling itself. 
> it doesn't usaully happen with iterative functions but 
it's better to know what we are coding in a recursive 
or in any function to avoid stackover flow or error 
in the program.
> recursion is sometime the most direct way to code an 
algorithm.'''