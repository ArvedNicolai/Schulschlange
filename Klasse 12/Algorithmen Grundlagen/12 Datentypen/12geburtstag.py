t = int(input("Tag: "))
m = int(input("Monat: "))
jahr = int(input("Jahr: "))

if (m == 1 or m == 2):
    m += 12
    jahr -= 1

j = int(jahr/100)
k = jahr%100

w = int((t + (13*(m+1))/5+k+k/4+j/4-2*j)%7)
w -= 1

tage = ["Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Samstag","Sonntag"]

#print (w)
print (tage[w-1])


