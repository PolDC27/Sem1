from Repository.DataRepo import DataRepo
from Modelle.Kunde import Kunde
class CustomerRepo(DataRepo):
    def __init__(self):
        self.Customers = []
        super().__init__(datei="Kunden.dat")


    def update(self, id, new_Name ,  new_Adresse):
            self.Customers = self.load()
            self.Customers.pop(id - 1)
            new_Kunde = Kunde(id, new_Name, new_Adresse)
            self.Customers.append(new_Kunde)
            self.save(self.Customers)


    def read(self):
        self.Customers = self.load()
        for Customer in self.Customers:
            print(str(Customer))

    def convert_to_string(self, obj_Liste):
        return map(lambda x: str(x), obj_Liste)

    def convert_from_string(self, string):
        objectList = []
        return map(lambda x: objectList.append(x), string)
