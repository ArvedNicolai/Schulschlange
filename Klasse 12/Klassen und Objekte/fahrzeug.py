# Basisklasse Fahrzeug
class Fahrzeug:
    def __init__(self, geschwindigkeit=0, farbe="Weiß"):
        self.geschwindigkeit = geschwindigkeit
        self.farbe = farbe

    def beschleunigen(self, wert):
        self.geschwindigkeit += wert
        print(f"Das Fahrzeug beschleunigt auf {self.geschwindigkeit} km/h.")

    def bremsen(self, wert):
        self.geschwindigkeit -= wert
        if self.geschwindigkeit < 0:
            self.geschwindigkeit = 0
        print(f"Das Fahrzeug bremst auf {self.geschwindigkeit} km/h ab.")

# Abgeleitete Klasse Auto
class Auto(Fahrzeug):
    def __init__(self, geschwindigkeit=0, farbe="Weiß", anzahlTueren=4):
        super().__init__(geschwindigkeit, farbe)
        self.anzahlTueren = anzahlTueren

    def hupen(self):
        print("Hup Hup!")

# Abgeleitete Klasse Fahrrad
class Fahrrad(Fahrzeug):
    def __init__(self, geschwindigkeit=0, farbe="Schwarz", hatKlingel=True):
        super().__init__(geschwindigkeit, farbe)
        self.hatKlingel = hatKlingel

    def klingeln(self):
        if self.hatKlingel:
            print("Klingeling!")
        else:
            print("Keine Klingel vorhanden.")

# Hauptprogramm
def main():
    # Objekt Auto erstellen
    mein_auto = Auto(geschwindigkeit=50, farbe="Rot", anzahlTueren=2)
    mein_auto.beschleunigen(20)
    mein_auto.hupen()
    print(f"Das Auto hat {mein_auto.anzahlTueren} Türen und die Farbe {mein_auto.farbe}.")

    # Objekt Fahrrad erstellen
    mein_fahrrad = Fahrrad(geschwindigkeit=15, farbe="Blau", hatKlingel=True)
    mein_fahrrad.bremsen(5)
    mein_fahrrad.klingeln()
    print(f"Das Fahrrad hat die Farbe {mein_fahrrad.farbe}.")

    ein_fahrrad = Fahrrad(geschwindigkeit = 10, farbe="Grün", hatKlingel=False)
    ein_fahrrad.bremsen(4)
    ein_fahrrad.beschleunigen(8)

if __name__ == "__main__":
    main()
