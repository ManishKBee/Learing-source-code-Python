# 01. Concatenating two string

greeting="Good Morning, "
name="MKB"
c=greeting+name
print(c)

# 02. slicing of the string and index of the leeter

name="Manish"
print(name[0])
print(name[0:5])
print(name[:4]) # it's same as name[0:4] or it's first index letter to 4
print(name[1:]) # it's same as name[1:6] or it's 1 to last index letter
print(name[-5:-1]) # it's same as name[1:5]
print(name[::2]) # it's same as name[0:6] or first letter of index to last letter of the index
'''first two num in the set are the 
range of the index letter to be consider 
and the third one is the every nth num to 
leave in the range of the index like in 
"Manish" we got Mns because python leaves
every second letter as we have set it to "2" in [::2] 
(printed "M" leaves the second which is "a" 
then prints "n" and leaves "i" then prints 
"s" and leaves "h" example taken is "Manish") 
in the range of index letters'''

'''Note: 1. the indexing of string starts from 
0 in python same with array like "MKB" M is 
index as 0 and B is index as 2 like the 
original or normal count subtract (-1) or 
can say subtract every letter (starting) 
from -3 till we reach -1 at last letter (taken 
the example of a string consisting 3 letters 
like "MKB")
2. if we are slicing the string like 
print(name[0:4]) then python will exclude the
index num 4 as the slice signals python that
print the string from the range of index 
num 0 to index num 4 for which python will 
only print 0,1,2,3 not the 4th index 
"first one is including last one is 
excluding"'''