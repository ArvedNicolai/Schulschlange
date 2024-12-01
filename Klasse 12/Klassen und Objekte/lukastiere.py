class Tier:
    def __init__(self, name):
        self.name = name
    
    def macheGeraeusch(self):
        print(f"{self.name} macht ein Geräusch.")
    
    def bewegeDich(self):
        print(f"{self.name} bewegt sich.")


class Hund(Tier):
    def __init__(self, name, rasse):
        super().__init__(name) 
        self.rasse = rasse
    
    def macheGeraeusch(self):
        print(f"{self.name} sagt: Wau Wau")
    
    def bewegeDich(self):
    
        print(f"{self.name} rennt!")


class Katze(Tier):
    def __init__(self, name, anzahlLeben=9):
        super().__init__(name)  
        self.anzahlLeben = anzahlLeben
    
    def macheGeraeusch(self):
        print(f"{self.name} sagt: Miau Miau")
    
    def bewegeDich(self):
        
        print(f"{self.name} schleicht.")


class Kuh(Tier):
    def __init__(self, name, milchleistung):
        super().__init__(name)
        self.milchleistung = milchleistung
    
    def macheGeraeusch(self):
        print(f"{self.name} sagt: Muh!")
    
    def bewegeDich(self):
        
        print(f"{self.name} steht.")


tiere = [
    Hund("hund", "Labrador"),
    Katze("katze", 8),
    Katze("katze2"),
    Kuh("kuh", 30),
]



for tier in tiere:
    tier.macheGeraeusch() 
    tier.bewegeDich()  

    print("---")

#gibt das komplette Objekt aus
print(tiere[1].__dict__)
print(tiere[2].anzahlLeben)