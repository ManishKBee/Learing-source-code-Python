# python code to find if the given post is about a specific person or place or thing

post=input("Enter The Post Here: ")

kywrd=input("Enter The Keyword Here for Search: ")

if (kywrd in post.lower()):
    print("The Post is About:", kywrd.capitalize())
else:
    print("The Post isn't About:", kywrd.capitalize())