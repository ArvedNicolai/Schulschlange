lauf = 0

def sumNaturalNumbers(n):
    if (n == 1):
        return 1
    return n + sumNaturalNumbers(n - 1)


def factorial(n):
    if (n == 1):
        return 1
    return n * factorial(n - 1)


def palindrom(wort, lauf, start, end):
    if (start != end):
        return 0
#Gerade Zahl, und die zwei mittleren Elemente werden verglichen
#oder Ungerade Zahl, in der es nur ein mittleres Element gibt
    if (lauf==len(wort)-lauf or lauf+1 == len(wort)-lauf):
        return 1
    lauf += 1 
    return palindrom(wort,lauf,wort[lauf],wort[len(wort)-lauf-1])



#print(sumNaturalNumbers(10))
#print(factorial(4))

wort = str(input("Gib ein Wort ein."))
#print(start, end)
print(palindrom(wort,lauf, wort[lauf],wort[len(wort)-1-lauf]))
