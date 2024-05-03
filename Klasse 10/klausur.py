text=input("Wie lautet dein Text")
alphabet="abcdefghijklmnopqrstuvwxyz"
ausgabe=[]
buchstabe=""
buchstabe=str(buchstabe)
for buchstabe in text:
    ausgabe = ausgabe.append(ord(buchstabe))
    ausgabe[ord(buchstabe)]+=1
i=0
while i<27:
    print(chr(97+i),":",ausgabe[97+i])
    i+=1
