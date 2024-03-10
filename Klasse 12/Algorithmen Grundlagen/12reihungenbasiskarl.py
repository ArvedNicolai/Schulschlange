#import
liege2 = [3, 100, 31, 12, 28, 12, 14, 8, 12, 43, 38]
def Funktion1(liege2):
    #print(liege[2])
    #print(max(liege))
    #liege.append(555)
    #liege.sort()
    #print(liege)
    #liege.pop(6)
    #print(liege)
    #print(liege.count(12))
    #liege.reverse()
    #print(liege)
    i = len(liege2)-1
    while(i+1>0):
        k = liege2[10]
        k = k+2
        liege2.pop(len(liege2)-1)
        #oder liege2.pop()
        liege2.insert(0,k)
        i=i-1
        print(liege2)
    print(liege2)
Funktion1(liege2)