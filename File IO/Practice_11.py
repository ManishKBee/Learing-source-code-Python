import os 

old_file="sam_text.txt"
new_file="rename_by_python.txt"

with open(old_file, "r") as r:
    content=r.read()

with open(new_file, "w") as w:
    w.write(content)

os.remove(old_file) # this is a os module's function which deletes the ginven file in the function like os.remove(<file name>)