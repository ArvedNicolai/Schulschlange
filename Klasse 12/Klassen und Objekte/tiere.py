# Basisklasse Tier
# Die Aufgabenstellung verlangt keine Attribute.

class Tier:
    def macheGeraeusch(self):
        print("Unbekanntes Geräusch")

# Abgeleitete Klasse Hund
class Hund(Tier):
    def macheGeraeusch(self):
        print("Wau Wau!")

# Abgeleitete Klasse Katze
class Katze(Tier):
    def macheGeraeusch(self):
        print("Miau!")

# Abgeleitete Klasse Kuh
class Kuh(Tier):
    def macheGeraeusch(self):
        print("Muh!")

# Hauptprogramm
def main():
    tiere = [Hund(), Katze(), Kuh()]
    for tier in tiere:
        tier.macheGeraeusch()

if __name__ == "__main__":
    main()
