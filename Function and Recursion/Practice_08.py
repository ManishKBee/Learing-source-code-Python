# python function which prints multiplication of given number 

n=0
def multiplication():
    for i in range(1, 11):
        print(f"{n}x{i}={i*n}")

n=int(input("Enter The Number: "))
multiplication()
