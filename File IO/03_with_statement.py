# python code writing, reading, updating and appending files using "with statement"

with open("text.txt", "r") as r: # we use with statement because if we use it then we don't need to write <variable>.close as the with statement closes the file automatically by it's own
     
     a=r.read() # store the output in a variable for printing the output

     # can be opened in write or any other given mode for file like read(r), write(w), append(a) and update(+) and also works with sub modes like readline() function

print(a)