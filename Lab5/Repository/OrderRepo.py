from Repository.DataRepo import DataRepo

class OrderRepo(DataRepo):
    def __init__(self):
        self.Orders = []
        super().__init__(datei="Orders.dat")


    def read(self):
        self.Orders = self.load()
        for Order in self.Orders:
           print(str(Order))


    def convert_to_string(self, obj_Liste):
        return map(lambda x: str(x), obj_Liste)

    def convert_from_string(self, string):
        objectList = []
        return map(lambda x: objectList.append(x), string)
