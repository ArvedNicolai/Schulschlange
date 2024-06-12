import random
from time import *



def insertion_sort(arr):
    # Durchlaufe das Array beginnend mit dem zweiten Element
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Verschiebe Elemente von arr[0..i-1], die größer als key sind, eine Position nach rechts
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Setze das key-Element an die richtige Position
        arr[j + 1] = key

def print_list(arr):
    for i in arr:
        print(i, end=" ")
    print()

# Beispiel zum Testen des Insertion-Sort-Algorithmus
liste = []
for i in range(10):
    liste.append(random.randint(1,20))
    
print("Gegebene Liste ist:")
print_list(liste)
t1 = process_time()

insertion_sort(liste)
t2 = process_time()
t = t2 - t1
print("Rechenzeit: ", t)

print("Sortierte Liste ist:")
print_list(liste)
