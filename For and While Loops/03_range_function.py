# range function it help us print a range of item which is given in the For loop the items will be print till the number or indexed item (n-1) 'where "n" is last number or indexed item of the range'

for i in range(8): 
    print(i) # by default it will start printing from number 0 till (n-1) of the range

for i in range (1, 11):
    print(i) # if we want to the printing from number 1 or any other staeting number we have to just put that number in the range function syntax like this "range(1, 11)" in this '1' is the starting point and '11' is the end of the range therefore the range function will print from 1 to 10 as 10 is equal to 'n-1' or "11-1" as 11 is the 'n' here

for i in range (1, 11, 2):
    print(i) # third element in the range function is step size which means according to the step size the range will be printed like if we have a range function of "range(1, 11, 2)" then 2 is the step size and it will print every second number after the starting number in the range like the output of this function is '1, 3, 5, 7, 9' like we can see the function has skipped every 1st number after 1 