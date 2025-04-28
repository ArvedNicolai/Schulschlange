#Klausuraufgaben Olaf, 11. Klasse Teil 1

farben = [(255,255,255),
          (255,255,255),
          (255,255,255),
          (255,255,255),
          (255,255,255),
          (255,255,255),
          (255,255,255),
          (255,255,255),
          (255,255,255),]

farben2 = [(101,102,100),
          (100,100,100),
          (100,100,100),
          (100,100,100),
          (100,100,100),
          (100,100,100),
          (100,100,100),
          (100,100,100),
          (100,100,100)]

#Schwarz-Weiss-Tester
zaehler = 0
for element in farben:
    
    if element == (255,255,255):
        zaehler += 1
    elif element == (0,0,0):
        zaehler += 1
    else:
        pass

if zaehler == len(farben):
    print ("Bild ist schwarz-weiss")
else: 
    print ("Bild ist nicht schwarz-weiss")


#Farbsättigung erhöhen
#Tupel kann man nicht verändern, also muss man eine neue Liste erstellen

farben3 = []

for (x, y, z) in farben2:
    farben3.append((x + 1, y + 8, z + 1))

print(farben3)