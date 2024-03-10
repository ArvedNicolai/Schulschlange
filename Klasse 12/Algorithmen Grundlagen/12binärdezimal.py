import math

#bitte nochmal mit Bitshift-Operator probieren

binaer = []
dec = 0

def binaryToDecimal(n,dec):
    i = 0
    while n >= 1:
        zahl = int(n%10) #ergebnis ist 1
        potenz = zahl * pow(2,i) #ergebnis ist 1
        dec = dec + potenz #ergebnis ist 0 + 1 = 1
        n = n/10 #ergebnis ist 101
        i += 1 
    #1101%10 = 1
    return dec

def decimalToBinary(n):
    while (n >= 1):
       rest = int(n % 2)
       binaer.insert(0,rest) 
       n = n / 2 
    return binaer

i = int(input("Gib 1 für die Umwandlung bin-->dec und 2 für die Umwandlung dec-->bin an: "))
n = int(input("Welche Zahl soll umgewandelt werden?"))


if (i == 1):
    dec = binaryToDecimal(n,dec)
    print(dec)
    #print ("Dec: ", dec)
else:
    binaer = decimalToBinary(n)
    print (binaer)
    #print (binaer)