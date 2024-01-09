from Modelle.Gericht import Gericht

class GekochterGericht(Gericht):
    def __init__(self, Id, Zubereitungszeit, Portionsgrosse, Preis):
        self.Zubereitungszeit = Zubereitungszeit
        super(). __init__(Id, Portionsgrosse, Preis)

    def __str__(self):
        return f"{self.Id}:{self.Zubereitungszeit}:{self.Portionsgrosse}:{self.Preis}"
