from Repository.DataRepo import DataRepo

class OrderRepo(DataRepo):
    def __init__(self):
        self.Orders = []
        super().__init__(datei="Orders.dat")


    def update(self, id, new_Kunden_Id = None, new_Liste_Gerichte = None, new_Liste_Getranke = None):
        Orders = self.load()
        for Order in Orders:
            if Order.Id == id:
                if new_Kunden_Id is not None:
                    Order.Kunder_Id = new_Kunden_Id
                if new_Liste_Gerichte is not None:
                    Order.Liste_Gerichte = new_Liste_Gerichte
                if new_Liste_Getranke is not None:
                    Order.Liste_Getranke = new_Liste_Gerichte
        self.write_to_file(Orders)

    def read(self):
        self.Orders = self.load()
        for Order in self.Orders:
           print(str(Order))


    def convert_to_string(self, obj_Liste):
        return map(lambda x: str(x), obj_Liste)

    def convert_from_string(self, string):
        objectList = []
        return map(lambda x: objectList.append(x), string)
