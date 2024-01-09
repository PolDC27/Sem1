from Modelle.Gericht import Gericht
class Getrank(Gericht):
    def __init__(self, Id, Alkoholgehalt, Portionsgrosse, Preis):
        self.Alkoholgehalt = Alkoholgehalt
        super().__init__(Id, Portionsgrosse, Preis)

    def __str__(self):
        return f"{self.Id}:{self.Preis}:{self.Portionsgrosse}:{self.Alkoholgehalt}"
