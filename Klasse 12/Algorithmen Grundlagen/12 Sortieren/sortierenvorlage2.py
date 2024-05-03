import random

def randoms(size):
    return [random.randint(1, size+1) for i in size * [None]]

size = int(input("Wie viele Elemente sollen erzeugt werden?"))

print(randoms(size))