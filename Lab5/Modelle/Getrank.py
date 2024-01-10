from Modelle.Gericht import Gericht
class Getrank(Gericht):
    def __init__(self, Id, Preis,Portionsgrosse, Alkoholgehalt ):
        self.Alkoholgehalt = Alkoholgehalt
        super().__init__(Id, Portionsgrosse, Preis)

    def __str__(self):
        return f"Id: {self.Id} Preis: {self.Preis} Portionsgrosse: {self.Portionsgrosse} Alkoholgehalt: {self.Alkoholgehalt}"
