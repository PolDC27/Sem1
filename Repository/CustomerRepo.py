from Repository.DataRepo import DataRepo

class CustomerRepo(DataRepo):
    def __init__(self):
        self.Customers = []
        super().__init__(datei="Kunden.dat")


    def update(self, id, new_Name = None,  new_Adresse = None):
        self.Customers = self.load()
        for Customer in self.Customers:
            if Customer.Id == id:
                if new_Name is not None:
                    Customer.price = new_Name
                if new_Adresse is not None:
                    Customer.Portionsgrosse = new_Adresse
        self.write_to_file(self.Customers)


    def read(self):
        self.Customers = self.load()
        for Customer in self.Customers:
            print(str(Customer))

    def convert_to_string(self, obj_Liste):
        return map(lambda x: str(x), obj_Liste)

    def convert_from_string(self, string):
        objectList = []
        return map(lambda x: objectList.append(x), string)
