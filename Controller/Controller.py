from Modelle.Getrank import Getrank
from Modelle.Kunde import Kunde
from Modelle.Bestellung import Bestellung
from Modelle.GekochterGericht import GekochterGericht



class Controller:
    def __init__(self, repo):
        self.repo = repo


    def add_Getrank_to_repo(self, Id, Preis, Portionsgrosse, Alkoholgehalt):
        new_Getrank = Getrank(Id, Preis, Portionsgrosse, Alkoholgehalt)
        self.repo.write_to_file(new_Getrank)


    def update_Getrank(self, Id, new_Preis, new_Portionsgrosse, new_Alkoholgehalt):
        updated_Getrank = Getrank(Id, new_Preis, new_Portionsgrosse, new_Alkoholgehalt)
        self.repo.update(updated_Getrank)


    def delete(self, Id):
        self.repo.delete(Id)


    def read(self):
        self.repo.read()


    def add_Kunde_to_repo(self, Id, Name, Adresse):
        new_Kunde = Kunde(Id, Name, Adresse)
        self.repo.write_to_file(new_Kunde)


    def update_Kunde(self, Id, new_Name, new_Adresse):
        updated_Kunde = Kunde(Id, new_Name, new_Adresse)
        self.repo.update(updated_Kunde)


    def add_Bestellung_to_repo(self, Id, Kunden_Id, Liste_Gerichte, Liste_Getranke):
        new_Bestellung = Bestellung(Id, Kunden_Id, Liste_Gerichte, Liste_Getranke)
        self.repo.write_to_file(new_Bestellung)


    def update_Bestellung(self, Id, new_Kunden_Id, new_Liste_Gerichte, new_Liste_Getranke):
        updated_Bestellung = Bestellung(Id, new_Kunden_Id, new_Liste_Gerichte, new_Liste_Getranke)
        self.repo.update(updated_Bestellung)


    def add_GekochterGericht_to_repo(self, Id, Zubereitungszeit, Portionsgrosse, Preis):
        new_GekochterGericht = GekochterGericht(Id, Zubereitungszeit, Portionsgrosse, Preis)
        self.repo.write_to_file(new_GekochterGericht)


    def update_GekochterGericht(self, Id, new_Zubereitungszeit, new_Portionsgrosse, new_Preis):
        updated_GekochterGericht = GekochterGericht(Id, new_Zubereitungszeit, new_Portionsgrosse, new_Preis)
        self.repo.update(updated_GekochterGericht)

