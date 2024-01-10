from Modelle.Gericht import Gericht

class GekochterGericht(Gericht):
    def __init__(self, Id, Name, Zubereitungszeit, Portionsgrosse, Preis):
        self.Name = Name
        self.Zubereitungszeit = Zubereitungszeit
        super(). __init__(Id, Portionsgrosse, Preis)

    def __str__(self):
        return f"id:{self.Id} Zubereitungszeit:{self.Zubereitungszeit} Name:{self.Name} Portionsgrosse:{self.Portionsgrosse} Preis:{self.Preis}"
