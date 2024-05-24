import random

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Bestimmen des Mittelpunkts des Arrays
        # : ist ein Sliceoperator, änhlich wie in Excel
        # ist : vorangestellt, wird das mid-Element nicht mit in die Liste genommen
        # ist : nachgestellt wird mid-Element mit genommen, bis zum Ende der Liste
        left_half = arr[:mid]  # Teilen der Elemente in zwei Hälften
        right_half = arr[mid:]

        merge_sort(left_half)  # Rekursives Sortieren der ersten Hälfte
        merge_sort(right_half)  # Rekursives Sortieren der zweiten Hälfte

        i = j = k = 0

        # Kopieren der Daten in temporäre Arrays left_half und right_half
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Prüfen, ob noch Elemente übrig sind
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def print_list(arr):
    for i in arr:
        print(i, end=" ")
    print()

# Beispiel zum Testen des Merge-Sort-Algorithmus
liste = []
for i in range(10):
    liste.append(random.randint(1,20))
    
print("Gegebene Liste ist:")
print_list(liste)

merge_sort(liste)

print("Sortierte Liste ist:")
print_list(liste)