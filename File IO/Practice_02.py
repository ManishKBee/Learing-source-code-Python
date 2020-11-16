def game():
    HiScore=int(input("Enter Your Score: "))
    return HiScore
    # return 45 can direct return a int value

score=game()
with open("Hi-Score.txt", "r") as r:
    Hi_Score=r.read()

if Hi_Score=="":
    with open("Hi-Score.txt", "w") as HiSc:
        HiSc.write(str(score))

elif int(Hi_Score)<score:
    with open("Hi-Score.txt", "w") as HiSc:
        HiSc.write(str(score))
# HiSc.write("Hi Score:", str(score)) this doesn't work coz write() function takes only one argument
