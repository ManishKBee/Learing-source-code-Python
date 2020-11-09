# useful methods for sets

'''creating an empty set'''

HiSet=set()

print(type(HiSet))

# 01. .add: it will help us add new items or elements in our "empty set"
HiSet.add(1)
HiSet.add(2)
HiSet.add(2)
HiSet.add(3)

# HiSet.add([4,5,6]) this will show TypeError: unhashable type: 'list' hence we can't add list to a set

'''Note: You can't add a list and dictionary to a set because 
lists are mutable, meaning that you can 
change the contents of the list and dictionary after 
adding it to the set. IMP: some explanation: 
The documentation defines a set as an 
unordered collection of distinct hashable 
objects.
* Property of set are they're unordered and 
unindexed items, set are non editable data 
type, and set can't contain duplicate value 
as have seen that set are madeup of non 
repeatable items or values'''

# HiSet.add({4:7,5:8,6:9}) this will show TypeError: unhashable type: 'dict' hence we can't add Dictionary to a set, same reason like 'list' 

HiSet.add((4,5,6)) # but we can add tuples to a set

print(HiSet)

# 02. len() fuction: it will print all the item present inside the set
print(len(HiSet)) # prints the length of the set

# 03. .remove: it will help us remove a specific item from the set
HiSet.remove(1)

# HiSet.remove(10) it can't remove an item which is not present in the 'set'
# HiSet.remove(2,3) it can't remove two items at same time as the function only accept one argument at one time

print(HiSet)

# 04. .pop(): it will remove and return a random item from the 'set'

print(HiSet.pop()) # removes a random item from the set

print(HiSet) # printing the exsiting set after .pop() function

# 05. .clear(): it will clear all the items from the "set"

HiSet.clear()

print(HiSet)

'''adding new item to the set''' 

HiSet.add(10)
HiSet.add(100)
HiSet.add(1000)
HiSet.add((1,11,111))

print(HiSet)

# 06. .union(): for this we need two or more set with items stored in it, then we use this function of .union and it will return a new set which will comprise or include all include all items from both the sets

set1={7,12,43,24,38,59}
set2={66,81,7,75,59,98}

print(set1.union(set2)) # union of set1 and set2, for printing the just use print() function before the .union() with the sets

# 07. .intersection: same concept as union need two or more sets for this function and it will return a new set with only those item or items which are present in both sets on which the function is applied

set1={7,12,43,24,38,59}
set2={66,81,7,75,59,98}

print(set1.intersection(set2))