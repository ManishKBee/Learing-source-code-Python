# python code to find if two file are identical in nature

file1="text.txt"
file2="text_copy.txt"

with open(file1, "r") as r:
    f1=r.read()

with open(file2, "r") as r:
    f2=r.read()

if f1==f2:
    print("Files are Identical")
else:
    print("Files are Non-Identical")