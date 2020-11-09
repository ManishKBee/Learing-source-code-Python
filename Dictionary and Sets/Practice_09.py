# Q9. can we change the values of list stored inside a set

'''s={8, 7, 12, "Manish", [1,2]} this will 
show an error that we can't store list in a 
set as "set" are non-editable data type and 
list are editable data type which doesn't 
follws the criteries of the !set!'''

s={8, 7, 12, "Manish", (1,2)} # tuples can be stored inside the set as they are also non-editable data type

print(s)