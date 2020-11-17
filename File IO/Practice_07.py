# python code to find out whether a log file contain python or not in it and also find in which line python is present

py=True
i=1
with open("log.txt", "r") as r:
    while py:
        py=r.readline() # change the given into lower case while storing the file at the time of reading it
        if "python" in py.lower(): # or change the given file into lower case while checking the stored value
            print(py)
            print(f"Python Found in Line {i}")
        i=i+1