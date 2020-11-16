# python code to save a multiplication table from 2 to 20 in a given file

for i in range(2, 21): # always check if the loop statement is correctly written or not as in this i have written if statement in place of for loop statement and trying to break the but there's no loop it show the error that break outside the loop as the break statement not inside the second loop statement
    with open(f"Multi_Table/Multiplication_Table_of_{i}.txt", "w") as f: # never forgot put value inside the {} if you are using f"string_{variable_is_must}"
        for j in range(1, 11):
            f.write(f"{i}x{j}={i*j}")
            if j!=10:
                f.write("\n")
    # break statement to see if we are going on the rigth track for coding the problem statement