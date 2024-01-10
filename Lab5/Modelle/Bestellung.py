import functools
from Modelle.Identifizierbar import Identifizierbar
class Bestellung(Identifizierbar):
    def __init__(self, Id, Kunden_Id, Liste_Gerichte, Liste_Getranke, Datum, Uhrzeit):
        super().__init__(Id)
        self.Kunden_Id, self.Liste_Gerichte = Kunden_Id, Liste_Gerichte
        self.Liste_Getranke, self.Gesamtkosten = Liste_Getranke, 0
        self.Datum = Datum
        self.Uhrzeit = Uhrzeit

    def __str__(self):
        return f" Id:{self.Id} Kunden id:{self.Kunden_Id} Liste Gerichte:{self.Liste_Gerichte} Liste Getranke:{self.Liste_Getranke} " \
               f"Datum:{self.Datum} Uhrzeit:{self.Uhrzeit}"

    def berechne_Gesamtkosten(self, List):
            self.Gesamtkosten = (functools.reduce(lambda a, b: a+b, List))
            return self.Gesamtkosten


