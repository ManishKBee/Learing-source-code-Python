# python code to replace foul language with censored text 

with open("sample.txt", "r") as r:
    text=r.read()
text=text.replace("donkey", "#$!&")

with open("sample.txt", "w") as w:
    w.write(text)