# break statement help us come out of the loop on demand or the break statement instucts the program to EXIT the Loop now!!!

for i in range (10):
    print(i)
    if i==5:
        break
else:
    print("Loop is Done") # this else statement will not execute if the program is set to a manual break to the loop before loop gets break naturally when the True condition gets False 