# python code to read(r), write(w), append(a) or add(a) and update(+) a file stored in the internal storage

'''if we are working with binary file we have to 
write "rb" (read in binary mode) for read() function 
and "rt" (read in text mode) for text files but the 
't' is auto adds to the different modes for text 
files'''

f=open("sample.txt", "r") # open() function have two arguments 1st is the file name and 2nd is mode like read, write, append or add and update.
# f=open("sample.txt") if we don't specify any mode in open() function then it take read mode as the default mode for the function  
data=f.read()
# data=f.read(no. of character) this read() function will only read first n character as the number of characters(n) mentioned inside the parentheses 
print(data)
f.close()

# readline() function for reading the given file

e=open("sample.txt", "r")
# reads 1st line
text=e.readline() # this function will only reads the first line of the given file
print(text, end="") # emd= to anything will replace \n fromt the end of print function
# reads 2nd line
text=e.readline() # we can have multiple readline() functions in our code which will give the next line of the given file like if the 1st readline() gives 1st line of the file then 2nd readline() will give 2nd line of the file and this goes till the content of file ends or we stop the readline() after 5th attempt then the last line printed will be the fifth line of the given file
print(text, end="") # emd= to anything will replace \n fromt the end of print function
# reads 3rd line
text=e.readline() # we can have multiple readline() functions in our code which will give the next line of the given file like if the 1st readline() gives 1st line of the file then 2nd readline() will give 2nd line of the file and this goes till the content of file ends or we stop the readline() after 5th attempt then the last line printed will be the fifth line of the given file
print(text, end="") # emd= to anything will replace \n fromt the end of print function

e.close()