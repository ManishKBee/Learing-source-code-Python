# python to find odd and even number with range range function

# n=int(input("Enter The Number: "))

# if n%2==0:
#     if n in range(2, 6):
#         print("Not Weird")
#     elif n in range(6, 21):
#         print("Weird")
#     elif n>20:
#         print("Not Weird")
# else:
#     print("Weird")

'''A number which is divisible by 2 and generates a 
remainder of 0 is called an even number. An odd 
number is a number which is not divisible by 2. The 
remainder in the case of an odd number is always 
“1”.'''

# python code to print square of given number if the number is non negative integer

# n=int(input())

# i=0
# if n>0:
#     for i in range(n):
#         print(i*i)
# else:
#     print("None")

# python code with leap year logic 

# def is_leap(y):

#     if y%4==0:
#         if y%100==0:
#             if y%400==0:
#                 print(True)
#             else:
#                 print(False)
#         else:
#             print(True)
# y=int(input())
# is_leap(y)

# alternative way of doing the same without return

# def is_leap(year):
    
#     if year%4==0:
#         if year%100==0:
#             if year%400==0:
#                 print(True)
#             else:
#                 print(False)
#         else:
#             print(True)
#     else:
#         print(False)

# year = int(input())
# print(is_leap(year))

# # alternative way of doing the same with return

# def is_leap(year):
#     leap = False
    
#     if year%4==0:
#         if year%100==0:
#             if year%400==0:
#                 leap=True
#             else:
#                 leap=False
#         else:
#             leap=True
#     else:
#         leap=False
    
#     return leap
# year = int(input())
# print(is_leap(year)

# python code to print 1 to n without spaces between the items of numbers

# n=int(input())
# for i in range(1, n+1):
#     print(str(i), end="") # ends the output with and without <" ":space, "":no space> space as menthioned in the code and we can also end with any <"str"> string

# python code for below problem statement

'''ou are given two sets,  and .
Your job is to find whether set  is a subset of set .

If set  is subset of set , print True.
If set  is not a subset of set , print False.

Input Format

The first line will contain the number of test cases, .
The first line of each test case contains the number of elements in set .
The second line of each test case contains the space separated elements of set .
The third line of each test case contains the number of elements in set .
The fourth line of each test case contains the space separated elements of set .

Constraints

Output Format

Output True or False for each test case on separate lines.

Sample Input

3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2
Sample Output

True 
False
False
Explanation

Test Case 01 Explanation

Set  = {1 2 3 5 6}
Set  = {9 8 5 6 3 2 1 4 7}
All the elements of set  are elements of set .
Hence, set  is a subset of set .'''

# for i in range(int(input())): 
#     # a = int(input()) # this doesn't do anything just here to satify the condition or the problem case given!!!
#     A = set(input().split()) # The split() method splits a string into a list. You can specify the separator, default separator is any whitespace.
#     # b = int(input()) # this doesn't do anything just here to satify the condition or the problem case given!!!
#     B = set(input().split()) # The split() method splits a string into a list. You can specify the separator, default separator is any whitespace.
#     if A.issubset(B):
#         print(True)
#     else:
#         print(False)

# More than 4 lines will result in 0 score. Blank lines won't be counted.  
# https://www.programiz.com/python-programming/methods/set/issubset (python subset resource)
