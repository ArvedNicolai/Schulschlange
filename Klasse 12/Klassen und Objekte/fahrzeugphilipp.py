class Fahrzeug:
    def __init__(self, geschwindigkeit, farbe):
        self.geschwindigkeit = geschwindigkeit
        self.farbe = farbe
    
    def beschleunigen (self,wert):
        self.geschwindigkeit = wert
    
    def bremsen (self,wert):
        self.geschwindigkeit = wert

class auto(Fahrzeug):
    def __init__(self, geschwindigkeit, farbe, anzahltueren):
        super().__init__(geschwindigkeit, farbe)
        self.anzahltueren = anzahltueren
    def hupen(self):
        print ("hup hup")

class fahrrad(Fahrzeug):
    def __init__(self, geschwindigkeit, farbe, hatklingel):
        super().__init__(geschwindigkeit, farbe)
        self.hatklingel = hatklingel
    def klingeln(self):
        print("Klingeling!")



vw = auto(10, "yellow", 5)
print(vw.geschwindigkeit)
vw.bremsen(3)
print(vw.geschwindigkeit)

nc = fahrrad(30, "green", False)
nc.klingeln()