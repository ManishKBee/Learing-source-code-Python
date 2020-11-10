# python code to sort spam comments from the comment section

com=input("Comment Here: ")

sp1="make a lot 0f money"
sp2="buy now"
sp3="subscribe this"
sp4="click this"
sp5="bitcoin"

if (sp1 in com or sp2 in com or sp3 in com or sp4 in com or sp5 in com):
    print("Above comment is Spam!!!ALERT!!!")
else:
    print("Thank Ypu For Commentimg :)")