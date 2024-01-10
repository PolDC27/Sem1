from Repository.DataRepo import DataRepo
from Modelle.GekochterGericht import GekochterGericht

class CookedDishRepo(DataRepo):
    def __init__(self):
        self.CookedDishes = []
        super().__init__(datei="Gerichte.dat")



    def update(self, id, new_Name, new_price, new_Portionsgrosse, new_Zubereitungszeit):
            self.CookedDishes = self.load()
            self.CookedDishes.pop(id - 1)
            new_dish = GekochterGericht(id, new_Name, new_Zubereitungszeit, new_Portionsgrosse, new_price)
            self.CookedDishes.append(new_dish)
            self.save(self.CookedDishes)

    def read(self):
        self.CookedDishes = self.load()
        for Dish in self.CookedDishes:
            print(str(Dish))

    def convert_to_string(self, obj_Liste):
        return map(lambda x: str(x), obj_Liste)

    def convert_from_string(self, string):
        objectList = []
        return map(lambda x: objectList.append(x), string)
