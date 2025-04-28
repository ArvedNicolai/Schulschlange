def vorzeichen(n):
    if n == 0:
        return 1
    else:
        return n * vorzeichen(n - 1)

# Beispielaufruf der Funktion
for i in range(1,6):
    print(vorzeichen(i))


    