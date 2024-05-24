import random

def quicksort(sliste):
  if len(sliste) <= 1:
      return sliste

  pivot = sliste.pop()

  low = []
  high = []
  for x in sliste:
      if x <= pivot:
          low.append(x)
      else:
          high.append(x)

  return quicksort(low) + [pivot] + quicksort(high)

liste = []
for i in range(10):
    liste.append(random.randint(1,20))

print (liste)
print(quicksort(liste))

