from Repository.DataRepo import DataRepo

class DrinkRepo(DataRepo):
    def __init__(self):
        self.Drinks = []
        super().__init__(datei="Drink.dat")



    def update(self, id, new_price=None, new_Portionsgrosse=None, new_Alkoholgehalt = None):
        for Drink in self.Drinks:
            if Drink.Id == id:
                if new_price is not None:
                    Drink.price = new_price
                if new_Portionsgrosse is not None:
                    Drink.Portionsgrosse = new_Portionsgrosse
                if new_Alkoholgehalt is not None:
                    Drink.Alkoholgehalt = new_Alkoholgehalt
        self.write_to_file(self.Drinks)

    def read(self):
        self.Drinks = self.convert_to_string(self.load())
        for Drink in self.Drinks:
            print(str(Drink))


    def convert_to_string(self, obj_Liste):
        return map(lambda x: str(x), obj_Liste)

    def convert_from_string(self, string):
        objectList = []
        return map(lambda x: objectList.append(x), string)
