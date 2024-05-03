text = input("Text: ")
i = 1
for buchstabe in "abcdefghijklmnopqrstuvwxyz":
    zaehler = 0
    for zeichen in text:
        if zeichen == buchstabe:
            zaehler+=1
    print(str(buchstabe),  ':' , zaehler)
    i+=1

