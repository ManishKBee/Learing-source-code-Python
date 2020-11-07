# Q2. fill the letter template with name and date

letter='''Dear <|NAME|>,
    You are selected!!!
    Date:<|DATE|>'''

name=input("enter the name:")
Name=name.capitalize() # Keep track on parentheses'()'
date=input("enter the date:")

letter=letter.replace("<|NAME|>", Name)
letter=letter.replace("<|DATE|>", date)

print(letter)