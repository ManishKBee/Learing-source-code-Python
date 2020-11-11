# continue statement is a close relative of break statement as it doesn;t exit the full loop but it just skip the values which are mentioned in the program

for i in range (10):
    if i==5:
        continue
    print(i) # it will skip the value of equality which is given in the if statement like 'if i==10' then it skip the value 10 from the loop and print all other item same as before