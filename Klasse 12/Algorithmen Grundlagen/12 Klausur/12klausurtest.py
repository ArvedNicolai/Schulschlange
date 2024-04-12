z = input("Diese Zahl soll getestet werden")

def TeilerFeststellen(z):
    teiler = []
    vgl = z/2
    i=0
    while i < vgl:
            if z%i == 0:
                teiler.append(i)
            i = i+1
    return teiler
def SummeErstellen(teiler):
    Sum = 0;
    for k in teiler:
        Sum = Sum + teiler[k]
    return Sum
def SummeVergleichen(Sum,z):
    if Sum == z:
        return "es handelt sich um eine perfekte Zahl"
    else:
        return "es handelt sich nicht um ein perfekte Zahl"

teiler = TeilerFeststellen(z)
Sum = SummeErstellen(teiler)
erg =  SummeVergleichen(Sum,z)




