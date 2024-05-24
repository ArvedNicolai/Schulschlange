text = "I"
text1 = "."
text2 = "I"
text31="("
text32=")"

i = 0
while (i<30):
    if (text[0]=="I"):
        text = text1 + text + text1
    elif (text[0]=="."):
        text = text31 + text + text32
    else:
        text = text2 + text + text2
    i += 1
    print(text)