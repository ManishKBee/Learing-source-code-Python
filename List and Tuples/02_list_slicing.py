# list slicing it's same as string slicing

Dost=["suraj", "mcbc", "javed", "raj"]
# print the list using print(a)
print(Dost)

# access a single item from the list using print(a[index num])
print(Dost[2])

# print a range of item from the list using print(a[range like "0:2", "1:3", "0:3", etc...])
print(Dost[0:2])

# print a range of item from the list using (negative range) print(a[negative range like "-3:0", "-2:0", "-3:-1", etc...])
print(Dost[-3:-1])

# use auto fill option for the range of the items in list same as string a[0:] will be auto filled till end of the list like [0:4], [0:7], etc...
print(Dost[0:])

# use auto fill option for the range of the items in list same as string a[:4] will be auto filled till start of the list like [0:5], [0:8], etc...
print(Dost[:2])

# use auto fill option for the range of the items in list same as string a[::] will be auto fill the start and end of the list like [0:5], [0:8], etc... and the third argument or option is nth num to print after first num like if there's a list of bee[1,3,4,5,3] then if we use [::2] then the output will be [1,4,3] it will print every second num after 0th index or first item in the list
print(Dost[::2])
