from Repository.DataRepo import DataRepo
from Modelle.Getrank import Getrank

class DrinkRepo(DataRepo):
    def __init__(self):
        self.Drinks = []
        super().__init__(datei="Drink.dat")



    def update(self, id, new_price, new_Portionsgrosse, new_Alkoholgehalt):
        self.Drinks = self.load()
        self.Drinks.pop(id - 1)
        new_drink = Getrank(id, new_price, new_Portionsgrosse, new_Alkoholgehalt)
        self.Drinks.append(new_drink)
        self.save(self.Drinks)

    def read(self):
        self.Drinks = self.load()
        for Drink in self.Drinks:
            print(str(Drink))


    def convert_to_string(self, obj_Liste):
        return map(lambda x: str(x), obj_Liste)

    def convert_from_string(self, string):
        objectList = []
        return map(lambda x: objectList.append(x), string)
