#Variante inf-schule.de

def bewegeScheibe(X, Z):
    #Bewege eine einzelne Scheibe von X nach Z.
    print(X, "->", Z)

def bewegeMehrereScheiben(n, X, Z, Y):
    if n > 1:
    #Bewege n Scheiben von X nach Z (über Y).""
        bewegeMehrereScheiben(n-1,X,Y,Z)
        bewegeScheibe(X,Z)
        bewegeMehrereScheiben(n-1,Y,Z,X)
    else:
        bewegeScheibe(X,Z)
        
bewegeMehrereScheiben(3, "A", "C", "B")
