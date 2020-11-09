# Q1. python code to print value from the Dictionary for "Key" inputed by the user

E2HnH2E={"authority":"अधिकार", 
"अधिकार":"authority", "power":"शक्ति",
"शक्ति":"power", "discipline":"अनुशासन",
"अनुशासन":"discipline"
}

print("List of Words Available:", E2HnH2E.keys())

word=input("Enter Text/Word: ")

print(E2HnH2E.get(word))

'''use input() function for user input and 
use print() function with Dictionary name 
and input as the Key for the print() 
function syntax which is: 
print(dict[key])
*always use .get function to pull the values 
from the dictionary as it reduces the changes 
of errors to occur*'''
