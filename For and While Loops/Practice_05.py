# python code to find sum of first n natural number using while and for loop

n=int(input("Enter The Number: "))

# for loop

sum=0
if n > 0:
    for i in range(1, n+1):
        sum=sum+i
print(sum)

# while loop

sum=0
i=0
if n>0:
    while i<n:
        i=i+1
        sum=sum+i
print(sum) # to print just the final output like in this one (the final sum not the step toward final) always print the output outside the while or for or any conditional statement