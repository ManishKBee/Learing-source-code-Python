# python code to print a multiplication table of given number

num=int(input("Enter The Number: ")) # always remember to type cast the input value

for i in range(1, 11):
     print(f"{num}x{i}={i * num}") # f strings are used to write strings with variable numbers like previously we have to Concatenate different strings with int values 'str(i)+"num"' but now we have to just write a 'f' before the string starts and write all the variable inside the "{}"