# string functions used in python

phrase="The quick brown fox jumps over the lazy dog, where's the fox now"

''' 01. len of the string: gives the total 
num of letters in the string'''

print(len(phrase))

''' 02. endswith of the string: this is 
boolean where the function returns true or 
false on the basis of ginen end letters like 
endswith "sh" will return ture but "ma" will
return false as we have taken the example of
"manish" as are string'''

print(phrase.endswith("dog"))

''' 03. count of the string: will the total 
num of the specific letter or word in the 
string like if we take "manish kumar" as 
an example and then if we count the num of 
"m's" in the string then we will get '2' 
as the count'''

print(phrase.count("t"))
print(phrase.count("the"))

''' 04. capitalize of the string: this function 
will capitalize or convert the first small 
letter of the string to capital letter like 
if we take the example of "manish" where "m" 
is written in small letter and if we run the 
same string with capitalize function then the 
function will make/convert the first letter 
to capital letter which will be "Manish" we 
can see small 'm' converted to capital 'M' 
after we used the function'''

print(phrase.capitalize())

''' 05. find the word in the string: this 
function will be used to find a specific 
word in the string but only for first 
occurrence of the word for example we 
take "MKB is a noob in coding but started 
coding" and then find the word "coding" 
then the function will show the position 
of indexed word "coding" but it will be only 
for first occurence of the word in the 
string therefore the output will be "17th" 
place in the string'''

print(phrase.find("fox"))

''' 06. replace of a word from the string: 
this function will be used to replace a 
specific word with a different or new word 
from the string and the replacement of the 
word will effect the whole string and the 
word from entire string will be replaced 
with the new word not like the find function 
where the function only effects the first 
occurence of the word for example we take 
"MKB is a noob in coding but started coding" 
and if we replace the word "coding" with the
new word "sailing" then the output will be
"MKB is a noob in sailing but started 
sailing" as we seen that the function has
replaced all the occurence of "coding" with
"sailing" from the string'''

print(phrase.replace("fox", "wolf"))

