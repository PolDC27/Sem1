from Modelle.Identifizierbar import Identifizierbar

class Gericht(Identifizierbar):
    def __init__(self, Id, Portionsgrosse, Preis):
        self.Portionsgrosse = Portionsgrosse
        self.Preis = Preis
        super().__init__(Id)




