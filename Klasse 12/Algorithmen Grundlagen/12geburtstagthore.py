def Tag(start):
    out=""
    if (start== 0):
        out ="Sonntag"
    elif(start== 1):
        out = "Montag"
    elif(start== 2):
        out = "Dienstag"
    elif(start == 3):
        out = "Mittwoch"
    elif(start== 4):
        out = "Donnerstag"
    elif(start== 5):
        out = "Freitag"
    else:
        out = "Sonntag"
    return out


def out(day,month,year,precise):
    print("Tag: " + str(day))
    print("Monat: " + str(month))
    print("Jahr: " + str(year) )
    print("Wochentag: " + str(precise))

def zeller(t,m,j,k):
    
    w= (t +((13*(m+1))/5) + k + k/4  + j/4 - 2*j)%7 -1
    
    return w 

def einmonthen(start):
    w = 0
    if (int(start)== 1 ):
        w = 13
    elif (int(start)== 2  ):
        w = 14
    else:
        w = int(start)

    return w

def aufteilen(start):
    
    a = [str(i) for i in str(start)]
    
    b = a[0]+a[1]
    c = a[2]+a[3]

    j = int(b)
    k = int(c)
    return j,k

def work(a):
    
    bot = str(a).split(".")
    day = int(bot[0])
    month = einmonthen(bot[1])
    year = int(bot[2])
    split = aufteilen(year)
    precise = int(zeller(day,month,split[0],split[1]))
    out(day,month,year,Tag(precise))
    
def main():   
    print("An welchem Tag wurden sie geboren?")
    print("Format: DD.MM.YYYY")
    base = input()
    work(base)

main()
