import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag, das überwacht, ob eine Vertauschung vorgenommen wurde
        swapped = False
        
        # Durchlaufe das Array von 0 bis n-i-1
        # Die letzten i Elemente sind bereits sortiert
        for j in range(0, n-i-1):
            # Vertausche, wenn das gefundene Element größer als das nächste ist
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # Wenn keine zwei Elemente vertauscht wurden, brich die Schleife ab
        if not swapped:
            break

def print_list(arr):
    for i in arr:
        print(i, end=" ")
    print()

# Beispiel zum Testen des Bubble-Sort-Algorithmus
liste = []
for i in range(10):
    liste.append(random.randint(1,20))
    
print("Gegebene Liste ist:")
print_list(liste)

bubble_sort(liste)

print("Sortierte Liste ist:")
print_list(liste)