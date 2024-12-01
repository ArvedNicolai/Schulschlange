class Auto:
    def __init__(self, farbe):
        self.farbe = farbe

# Erstellen eines Auto-Objekts
auto1 = Auto("rot")

# Zuweisen von auto1 zu auto2
auto2 = auto1

# Ändern der Farbe über auto2
auto2.farbe = "blau"

# Überprüfen der Farbe über auto1
print(auto1.farbe)  
