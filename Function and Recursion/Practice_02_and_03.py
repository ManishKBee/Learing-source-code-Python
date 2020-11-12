# python function to convert celsius to fahrenheit

'''formula: (100°C × 9/5) + 32 = 212°F'''

def celsius_to_fahrenheit():
    return ((c*9)/5)+32

c=int(input("Enter Temperature in Celsius:\n ")) # [Pratice_03]: \n is used to print a new line at the end!!!
print("Fahrenheit for given Celsius:\n", celsius_to_fahrenheit())

# Q3. print function to stop adding a new line while printing something

print("Hello", end=",") # by default print() function 'ends' with \n for adding a new line at the end given line
print(" How are", end=" ")
print("you!", end="") # 'end' function is used to print anything at the end of given line 