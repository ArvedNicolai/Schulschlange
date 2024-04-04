liege = [3, 100, 31, 12, 28, 12, 14, 8, 12, 43, 38]
liege.append(12)
print (liege)
print (max(liege))
print (liege.count(12))
liege.remove(liege[10])
print("Remove: ", liege)
for element in range(len(liege)):
    liege[element] += 2
print (liege)
liege.sort()
print (liege)
liege.reverse()
print(liege)

