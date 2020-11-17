# python code to find out whether a log file contain python or not in it

with open("log.txt", "r") as r:
    py=r.read() # change the given into lower case while storing the file at the time of reading it
    
    if "python" in py.lower(): # or change the given file into lower case while checking the stored value
        print("Python Found")
    else:
        print("Python not Found")