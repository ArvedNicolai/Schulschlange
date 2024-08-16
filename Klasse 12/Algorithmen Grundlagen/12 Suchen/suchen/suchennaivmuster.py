from time import *
Schuelerlist = []
with open("data.txt","r") as read:
    for line in read:
        Schuelerlist.append(line)
    for i in range(len(Schuelerlist)):
        Schuelerlist[i]=Schuelerlist[i].replace("\n","")
        Schuelerlist[i]=int(Schuelerlist[i])
    # Kontrollausgabe
    #for i in range(len(Schuelerlist)):
        #print(Schuelerlist[i])

t1 = process_time()

for i in range(20):
    for element in Schuelerlist:
        if (element == 8889 or element ==  5755 or element == 9956 or element == 1077):
            print("Zahl gefunden")

t2 = process_time()
t = t2 - t1
print(t)