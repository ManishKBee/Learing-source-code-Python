# imp methods used in Dictionary

HiDict={
    "money": "Anything that have a exchange value",
    "coding": "Tool for passionate problem solver",
    "manish": "Started with coding and programming",
    "cash": [350,550,750], # Dictionary can contain int and list in it!!!
    "HeyDict": {"TYBcom":"Third Year in Bachelor of Commerce"}, # like this we create nested Dictionary which means Dictionary within Dictionary like we have main Dictionary named "HiDict" and the nested Dictionary named as "HeyDict"
    25:100
}

# 01. .keys: it's used to find/print all Keys in the Dictionary and the default data type of it is 'dict_keys'
print(HiDict.keys())
print(type(HiDict.keys()))

# the data type to list using the below syntax
print(list(HiDict.keys()))

# 02. .values: it's used to print all the values in the dictionary
print(HiDict.values())

# 03. .items: it's used to print the "keys" and "values" in tuple(kind of list) format but we can iterate it in 'for loops'(future topic) and the default data type is 'dict_items'
print(HiDict.items())

# 04. .update: it's to update the main dictionary with new keys and values for the dictionary
print(HiDict) # printing unupdated dictionary for reference

HelloDict={
    "microsoft": "windows operating system"
} # the update we want to push for our existing Dictionary with new set of keys and values

HiDict.update(HelloDict) # update pushed and the dictionary is successfully updated with new set of keys and values

print(HiDict) # printing updated dictionary for checking updated content

# 05. .get: it's used to pull value for specific key in the dictionary 

print(HiDict.get("manish")) # this will give value of the key mentioned in the function and available in the dictionary

print(HiDict.get("manish behera")) # this will give "None" if the 'Key' is not present in the dictionary which will not break the code with an error msg

print(HiDict["manish"]) # it will print same value like .get if the is available in the dictionary

# below given the key difference between .get and main dictionary["key"]

'''print(HiDict["manish behera"]) if we are
using [square brackets] to find the value 
of a key then it's your job to know that if
the key is present or not in the dictionary
if the key is present then it's fine and we 
are good but if not present in the dictionary 
then python will throw an error like::
KeyError:: 'manish behera' and break the code 
with an error msg'''

# for more dictionary methods visit python docs