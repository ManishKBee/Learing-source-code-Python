# python code to find pass and fail status of the students

name=input("Name of The Student: ")

print("Enter Marks of", name.capitalize())

s1=int(input("Marks of 1st Subject: "))
s2=int(input("Marks of 2nd Subject: "))
s3=int(input("Marks of 3rd Subject: "))

outof=100
s1per=(s1/outof)*100
s2per=(s2/outof)*100
s3per=(s3/outof)*100
pc=33
pcper=(pc/outof)*100

gtoutof=300
gt=s1+s2+s3
gtper=(gt/gtoutof)*100
gtpc=120
gtpcper=(gtpc/gtoutof)*100

if (gtper>=gtpcper):
    if (s1per>=pcper):
        if (s2per>=pcper):
            if (s3per>=pcper):
                print(name.capitalize(), "Has Passed The Assessment!!!")
else:
    print("Failed...")