# Q4. python code to find the len of the set "s"

s=set()
s.add(20)
s.add(20.0)
s.add("20")

print(s)

print(len(s))

'''Note: set consider "0.0 float as int 0" and 
if we "int 0" in the set then it will not show 
the "0.0 float as it's a repeatative item" for 
the set and set dosen't allow repeat value'''
