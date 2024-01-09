from Modelle.Identifizierbar import Identifizierbar
class Kunde(Identifizierbar):
    def __init__(self, Id, Name, Adresse):
        self.Name = Name
        self.Adresse = Adresse
        super().__init__(Id)

    def __str__(self):
        return f"{self.Id}:{self.Name}:{self.Adresse}"
