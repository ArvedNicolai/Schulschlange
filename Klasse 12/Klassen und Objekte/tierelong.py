# Basisklasse Tier
class Tier:
    def __init__(self, name):
        self.name = name

    def macheGeraeusch(self):
        print(f"{self.name} macht ein unbekanntes Geräusch.")

# Abgeleitete Klasse Hund
class Hund(Tier):
    def __init__(self, name, rasse):
        super().__init__(name)
        self.rasse = rasse

    def macheGeraeusch(self):
        print(f"{self.name}, der {self.rasse}, bellt: Wau Wau!")

# Abgeleitete Klasse Katze
class Katze(Tier):
    def __init__(self, name, anzahlLeben=9):
        super().__init__(name)
        self.anzahlLeben = anzahlLeben

    def macheGeraeusch(self):
        print(f"{self.name}, die Katze, miaut: Miau!")

# Abgeleitete Klasse Kuh
class Kuh(Tier):
    def __init__(self, name, milchleistung):
        super().__init__(name)
        self.milchleistung = milchleistung

    def macheGeraeusch(self):
        print(f"{self.name}, die Kuh, muht: Muh!")

# Hauptprogramm
def main():
    # Objekte erstellen
    hund = Hund("Bello", "Labrador")
    katze = Katze("Minka")
    kuh = Kuh("Elsa", 20)
    katze2 = Katze("Gitte")

    # Liste von Tieren
    tiere = [hund, katze, kuh, katze2]

    # Polymorpher Methodenaufruf
    for tier in tiere:
        tier.macheGeraeusch()

    # Zugriff auf spezifische Attribute
    print(f"{hund.name} ist ein {hund.rasse}.")
    print(f"{katze.name} hat {katze.anzahlLeben} Leben.")
    print(f"{kuh.name} gibt {kuh.milchleistung} Liter Milch pro Tag.")

if __name__ == "__main__":
    main()
