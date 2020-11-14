# python code to write or append any text or string to a file using write function for files

w=open("sample.txt", "w")
w.write('''Data science is a "concept to unify 
statistics, data analysis and their related methods" 
in order to "understand and analyze actual phenomena" 
with data \n''') # this function will append multiple times if we run this code multiple times before closing the opened file 
w.close()

'''Note: if we use the write() function for a non 
existing file like "Iam_here.txt" then the write will 
make a file named "Iam_here.txt" then write the given 
text or string'''

# append function will give us the functionality to add anything at the end without overwriting the given as we have seen in the write() function but we use the same write() function in this but we open our file in append (a) mode so that we can add the given text or string

a=open("sample.txt", "a")
a.write("Hello, Iam Manish") # this function will append multiple times if we run this code multiple times
a.close()