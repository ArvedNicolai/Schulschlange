wort = ['a','b','c','c','b','a']
i=0

def Anagramm(wort,i):
    if wort[i]==wort[len(wort)-(i+1)]:
        
        if i+1==len(wort)-(i+1):
            return 'Das Wort ist ein Anagramm'
        if i+1==len(wort)-(i+2):
            return 'Das Wort ist ein Anagramm'
        i=i+1
        #Anagramm(wort,i)
    return 'das Wort ist kein Anagramm'

print(Anagramm(wort,i))  