import matplotlib.pyplot as plt
import numpy as np

def zeichenzaehlen (text,zeichen):
    i = 0
    x.append(zeichen)
    for buchstabe in text:
        if (buchstabe == zeichen): 
            i += 1
    y.append(i)

alphabet = "abcdefghijklmnopqrstuvwxyz"
text = input("Geheimtext: ")
x = []
y = []
for buchstabe in alphabet:
    zeichenzaehlen(text,buchstabe)

plt.bar(x,y)
plt.show()
