# else in for and while loop is a option step which will be executed when the loop statement becomes False and the loop breakes then the else statement will be printed in the output section

for i in range (10):
    print(i)
else:
    print("Loop is Done")

hpspells=["Riddikulus", "Accio", "Alohomora", "Crucio", "Sectumsempra"]

list=0
while list<len(hpspells):
    print(hpspells[list])
    list=list+1
else:
    print("Loop is Done")