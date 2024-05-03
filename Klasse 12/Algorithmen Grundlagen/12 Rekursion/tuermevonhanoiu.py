def Scheibe(X,Z):
    print(X, "-->", Z)

def Turm(n,X,Z,Y):
    if (n > 1):
        Turm(n-1,X,Y,Z)
        Scheibe(X,Z)
        Turm(n-1,Y,Z,X)
    else:
        Scheibe(X,Z)

Turm(4,"A","C","B")