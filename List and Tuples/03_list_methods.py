# most used and imp. data type and it's functions/methods to use the data type

fang=[1,3,5,6,7,5,7,9,0,34,4,6,8,89,35,67,92]

# 01. this will sort the list in ascending order
fang.sort()
print(fang)

# 02. this will sort the list in descending order
fang.reverse()
print(fang)

# 03. this will add a new item to the list in the end or it will be new last num before sorted 
fang.append(69)
print(fang)

# 04. this will insert a new item to the list but in replacement of an existint item and the new item will take index num of the previous item it been changed to like if change "45" in the "index position of 5" then the item in "index 5" will changed by new item named or known as "45"
fang.insert(3,10)
print(fang)

# 05. this will remove an item from the list using the "index num provided" like if we use pop(3) then it will remove the item "indexed in 3" of the list
fang.pop(11)
print(fang)

# 06. this will remove an item from the list using the "item name like 34,21,56,12,45,79" like if we use remove(21) then it will remove the item "named 21" in the list and the new list will be [34,56,12,45,79]
fang.remove(69)
print(fang)

'''Note: there will be two kind of output 
or effects on data type while using any 
kind function on the data type which are:
01. the function will return a new output 
by shifting to new vesel of same data type 
with changed set of data stored due to the 
use of the function.
02. the function will change the existing
vesel of the data type with new data set 
formed due the fuction.
03. if we want to know about new list methods 
or anything about list the just search list
methods python docs'''
