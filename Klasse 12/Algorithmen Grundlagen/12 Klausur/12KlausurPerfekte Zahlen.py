def isPerfect(i):
    liste = []
    summe = 0
    for j in range(1,i):
        if (i%j== 0):
            liste.append(int(j))
            
    #Lennart hatte hier noch vorgeschlagen, direkt die Teil aufzusummieren. Das wäre einfacher.
    #Aber dann hätte man die Liste nicht.
    #würde aber so aussehen: 
    #for j in range(1,i):
    #    if (i%j==0):
    #       summe += j

    for k in liste:
        summe += k
    if (i == summe):
        return 1
    else: 
        return 0

for i in range(1,500):
    #das hier war überflüssig 
    #isPerfect(i)
    if (isPerfect(i) == 1):
        print(i)
