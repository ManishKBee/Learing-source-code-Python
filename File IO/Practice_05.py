# python code to replace a list of foul language with censored text

words=["donkey", "kalle", "mote", "bekar"]

with open("sample.txt", "r") as r:
    text=r.read()

for word in words:
    text=text.replace(word, "#$!&")

    with open("sample.txt", "w") as w:
        w.write(text)