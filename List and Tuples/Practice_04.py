# Q4. python code to sumup a list of 4 numbers

marks=[56,49,51,45]

# alternate method print(m[0]+m[1]+m[2]+m[3])

Marks=sum(marks)

print(Marks)

# Marks=sum(marks,5) this is second type which have start mentioned which will just addup to the total sum of the list like if we take list as l1=[1,2,3,4,5] then s1=sum(l1,5) will be equal to "15 total of list" + "5 the start of the 'sum' given"

'''Notes: 
01. "sum(a)"
a is the list , it adds up all the numbers in the 
list a and takes start to be 0, so returning 
only the sum of the numbers in the list.
02. "sum(a, start)"
this returns the sum of the list + start''' 