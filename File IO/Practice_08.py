# python code to copy a content of given file to make a clone or copy of the file

with open("text.txt", "r") as r:
    content=r.read()

with open("text_copy.txt", "w") as w:
    w.write(content)