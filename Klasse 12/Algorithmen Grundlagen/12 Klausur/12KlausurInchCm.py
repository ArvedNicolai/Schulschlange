def inchToCm(x):
    return x*2.54

def cmToInch(x):
    return x*0.3937

wahl = int(input("Willst du cm in inch, wähle 2, willst du inch in cm, wähle 1 "))
if (wahl == 2):
    x=float(input("Gib' einen Wert in inch an: "))
    print(inchToCm(x))
elif (wahl == 1):
    x=float(input("Gib' einen Wert in cm an: "))
    print(cmToInch(x))
else: 
    print("Falsche Eingabe")


