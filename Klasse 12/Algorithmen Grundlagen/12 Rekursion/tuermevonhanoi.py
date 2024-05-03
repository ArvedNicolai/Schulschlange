def Turm(k,a,b):
    if k!=0:
        c=6-a-b
        Turm(k-1,a,c)
        print(k,a,b)
        Turm(k-1,c,b)
    return

Turm(4,1,2)