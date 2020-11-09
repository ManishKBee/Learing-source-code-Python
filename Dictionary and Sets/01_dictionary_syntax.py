# dictionary is a collection of key and value pairs

# create dictionary using {} curly brackets
HiDict={
    "Money": "Anything that have a exchange value",
    "Coding": "Tool for passionate problem solver",
    "Manish": "Started with coding and programming",
    "Cash": [350,550,750], # Dictionary can contain int and list in it!!!
    "HeyDict": {"TYBcom":"Third Year in Bachelor of Commerce"}, # like this we create nested Dictionary which means Dictionary within Dictionary like we have main Dictionary named "HiDict" and the nested Dictionary named as "HeyDict"
    25:100
}

# print using print(Dictionary name[key like first words (Money,Coding,Manish and Cash) in the "HiDict"]) function
print(HiDict["Money"])
print(HiDict["Manish"])
print(HiDict["Cash"])
print(HiDict[25])
print(HiDict["HeyDict"])

# print nested Dictionary using print(main Dictionaty[Key of main Dictionary][Key of nested Dictionary])
print(HiDict["HeyDict"]["TYBcom"])

HiDict["Cash"]=[1000,700,950]
print(HiDict["Cash"])

'''Note: 01. Dictionary not arranged in an 
order i.e, it doesn't have specific num to 
any Key or Value
02. Dictionary are editable like lists
03. Dictionary have indexed data in it like 
we can evoke any value by just using the Key
04. Dictionary can't contain duplicate Keys 
means we can't have two different values for 
same Key if we use an existing Key for storing 
new "value" then python will just replace the 
old value with new value inputed
05. "Different keys" can have same value'''