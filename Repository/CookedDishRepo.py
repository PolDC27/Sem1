from Repository.DataRepo import DataRepo

class CookedDishRepo(DataRepo):
    def __init__(self):
        self.CookedDishes = []
        super().__init__(datei="Gerichte.dat")



    def update(self, id, new_price = None, new_Portionsgrosse = None, new_Zubereitungszeit = None):
        Dishes = []
        Dishes.append(self.load())
        for Dish in Dishes:
            if Dish.Id == id:
                if new_price is not None:
                    Dish.price = new_price
                if new_Portionsgrosse is not None:
                    Dish.Portionsgrosse = new_Portionsgrosse
                if new_Zubereitungszeit is not None:
                    Dish.Zubereitungszeit = new_Zubereitungszeit
        self.write_to_file(Dishes)

    def read(self):
        self.Dishes = self.load()
        for Dish in self.Dishes:
            print(str(Dish))

    def convert_to_string(self, obj_Liste):
        return map(lambda x: str(x), obj_Liste)

    def convert_from_string(self, string):
        objectList = []
        return map(lambda x: objectList.append(x), string)
