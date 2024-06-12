Schuelerlist=[]
with open("data.txt","r") as read:
    for line in read:
        Schuelerlist.append(line)
    for i in range(len(Schuelerlist)):
        Schuelerlist[i]=Schuelerlist[i].replace("\n","")
        Schuelerlist[i]=int(Schuelerlist[i])
    # Kontrollausgabe
    for i in range(len(Schuelerlist)):
        print(Schuelerlist[i])
