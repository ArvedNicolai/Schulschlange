class Fahrzeug:

    def __init__(self, marke, modell, baujahr, kilometerstand, mietpreisProTag = 0):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr
        self.kilometerstand = kilometerstand
        self.mietpreisProTag = mietpreisProTag

    def setKilometerstand(self, km):
        self.kilometerstand = km

    def berechneMietpreis(self, tage):
        return self.mietpreisProTag * tage

class PKW(Fahrzeug):

    def __init__(self, marke, modell, baujahr, kilometerstand, anzahlTueren, mietpreisProTag = None):
        super().__init__(marke, modell, baujahr, kilometerstand)
        self.anzahlTueren = anzahlTueren
        if mietpreisProTag is None:
            self.mietpreisProTag = 80
        else:
            self.mietpreisProTag = mietpreisProTag

    def berechneMietpreis(self, tage):
        preis = super().berechneMietpreis(tage)
        if tage > 6:
            preis *= 0.9
        return preis

        
class LKW(Fahrzeug):

    def __init__(self, marke, modell, baujahr, kilometerstand, maxLadung, mietpreisProTag = None):
        super().__init__(marke, modell, baujahr, kilometerstand)
        self.maxLadung = maxLadung
        if mietpreisProTag is None:
            self.mietpreisProTag = 80
        else:
            self.mietpreisProTag = mietpreisProTag

    def berechneMietpreis(self, tage):
        preis = super().berechneMietpreis(tage)
        # Zuschlag von 20% bei mehr als 5 Tagen Mietdauer
        if tage > 4:
            preis *= 1.2  # 20% Zuschlag
        return preis
    

volvo = PKW("Volvo", "3", 1990, 100000,5)
bmw = PKW("BMW", "Coupé", 2003, 502329,3)
bmw2 = PKW("BMW", "Coupé", 2003, 502329,3,30)
audi = PKW("Audi", "Quattro", 2005, 280232,3)
brumm = LKW("Brumm", "Brumm", 2001, 989822,2)
mans = LKW("Wiuuu", "Brumm", 2020, 13029,2)

fahrzeugliste = [volvo, bmw, audi, brumm, mans]

#print("Fahrzeug: ", volvo.marke, volvo.modell)
#print("Mietpreis für 4 Tage: ", volvo.berechneMietpreis(4))
#print("Mietpreis für 10 Tage: ", volvo.berechneMietpreis(10))
print (mans.mietpreisProTag)

print("Fahrzeug: ", brumm.marke, brumm.modell)
print("Mietpreis für 4 Tage: ", brumm.berechneMietpreis(4))
print("Mietpreis für 10 Tage: ", brumm.berechneMietpreis(10))




