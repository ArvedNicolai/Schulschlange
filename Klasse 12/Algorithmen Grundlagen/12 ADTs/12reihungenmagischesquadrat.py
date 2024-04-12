zahl = int(input("Gib eine ungerade Zahl ein: "))
quadrat = [ [int(0)]*zahl for i in range(zahl)]

#erstes Element platzieren:
spalte = int(zahl/2) 
zeile = int(zahl/2+1)
max = zahl - 1
quadrat[zeile][spalte]=1
i = 2
for i in range(2,zahl*zahl+1):
    zeile = zeile + 1
    spalte = spalte + 1
    if (zeile > max): zeile = 0
    if (spalte > max): spalte = 0
    if (quadrat[zeile][spalte]==0): quadrat[zeile][spalte]+=i
    else:
        while(1):
            zeile = zeile + 1
            spalte = spalte - 1
            if (zeile > max): zeile = 0
            if (spalte < 0): spalte = max
            if (quadrat[zeile][spalte]==0): quadrat[zeile][spalte]+=i
            break

for i in range(len(quadrat)):
    for j in range(len(quadrat[i])):
        print(quadrat[i][j], " ", end=' ')
    print()




