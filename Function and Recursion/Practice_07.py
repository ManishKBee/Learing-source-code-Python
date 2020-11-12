# python code to remove a word from a given list[]

'''def word_remove():
    return l1.remove(n)

l1=["mac", "fluffy", "123", "den", "bunny"]
n=input("Enter The Word To Remove: ")
word_remove()

print(l1)''' # this will return a list

# python function to remove a word and blank spaces between the given string

def word_remove(string, word):
    new_string=string.replace(n, "")
    return new_string.strip()

l="  mac, fluffy, 123den, bunny  "
n=input("Enter The Word To Remove: ")
a=word_remove(l, n)

print(a) # this will return string