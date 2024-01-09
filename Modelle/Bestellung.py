import functools
from Modelle.Identifizierbar import Identifizierbar
class Bestellung(Identifizierbar):
    def __init__(self, Id, Kunden_Id, Liste_Gerichte, Liste_Getranke):
        self.Kunden_Id, self.Liste_Gerichte = Kunden_Id, Liste_Gerichte
        self.Liste_Getranke, self.Gesamtkosten = Liste_Getranke, 0
        super().__init__(Id)

    def __str__(self):
        return f"{self.Id}:{self.Kunden_Id}:{self.Liste_Gerichte}:{self.Liste_Getranke}"

    def berechne_Gesamtkosten(self):
            self.Gesamtkosten += functools.reduce(lambda a, b: a+b, self.Liste_Gerichte)
            self.Gesamtkosten += functools.reduce(lambda a, b: a+b, self.Liste_Getranke)
            return self.Gesamtkosten

