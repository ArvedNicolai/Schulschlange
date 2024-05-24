import random

def selection_sort(arr):
    # Durchlaufe alle Arrayelemente
    for i in range(len(arr)):
        # Finde das kleinste Element im unsortierten Teil des Arrays
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Tausche das gefundene kleinste Element mit dem ersten Element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def print_list(arr):
    for i in arr:
        print(i, end=" ")
    print()

# Beispiel zum Testen des Selection-Sort-Algorithmus
liste = []
for i in range(10):
    liste.append(random.randint(1,20))

    
print("Gegebene Liste ist:")
print_list(liste)

selection_sort(liste)

print("Sortierte Liste ist:")
print_list(liste)