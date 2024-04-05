def isPerfect(x):
    liste = []
    summe = 0
    for j in range(1,i):
        if (i%j== 0):
            liste.append(int(j))
    for k in liste:
        summe += k
    if (i == summe):
        return 1
    else: 
        return 0

for i in range(1,500):
    isPerfect(i)
    if (isPerfect(i) == 1):
        print(i)
