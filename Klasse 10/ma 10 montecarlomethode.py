import matplotlib.pyplot as plt
import random
import math
import numpy as np

i = 0
innen = 0
anzahl = int(input("Wie oft soll ein Punkt erzeugt werden?"))
while i <= anzahl:
    x = random.random()
    y = random.random()
    if math.sqrt(x*x+y*y) < 1:
        plt.scatter(x,y, s=10, color='blue') # Einen Punkt zeichnen
        innen += 1
    else: 
        plt.scatter(x,y, s=10, color='red') # Einen Punkt zeichnen
    i += 1

pi = innen/anzahl * 4    

# Viertelkreis
x = np.linspace(0,1,100)
y = np.sqrt(1-x*x)
plt.plot(x,y)

plt.title(pi)
plt.suptitle("Annäherung an π mit Montecarlo-Methode")

plt.xlabel('x-Achse'); plt.ylabel('y-Achse') # Label für die Koordinatenachsen
plt.axis([0, 1, 0, 1]) # Achsen-Bereiche festlegen; Syntax: plt.axis([xmin, xmax, ymin, ymax])
plt.grid(True)         # Diagramm-Gitter einblenden
plt.plot(x,y)
plt.show()             # Diagramm anzeigen

