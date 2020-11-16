# python code read a given file and identifing if there's a word in the text thats given in the problem statement

w=open("poem.txt", "w")
w.write('''Twinkle, twinkle, little star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle, twinkle little star
How I wonder what you are''')
w.close()

p=open("poem.txt", "r")
poem=p.read()
if "twinkle" in poem:
    print("Twinkle")
else:
    print("Twinkle is not present")
p.close()