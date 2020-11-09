# Q6. python code to record the fav. language of 4 different friends

# problem scenario: if two friends have same name 

f1=input("Enter Your Name: ")
print("Hello", f1)
l1=input("Enter Fav. Language: ")
f2=input("Enter Your Name: ")
print("Hello", f2)
l2=input("Enter Fav. Language: ")
f3=input("Enter Your Name: ")
print("Hello", f3)
l3=input("Enter Fav. Language: ")
f4=input("Enter Your Name: ")
print("Hello", f4)
l4=input("Enter Fav. Language: ")

FrinLan={f1:l1, f2:l2, f3:l3, f4:l4}

print(FrinLan)

'''Ans. python will create a Dictionary using 
the inputed keys and values but their will 
be only 3 pairs of keys and values as two 
keys are same and dictionay doesn't record the 
duplicate key, Hence 3 pairs of keys and values
*the latest value update for key the will be 
stored inside key by replacing the old 
value*'''
