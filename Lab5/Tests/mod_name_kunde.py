from Modelle.Kunde import Kunde
import pickle


class Repo:
    def __init__(self, datei):
        self.datei = datei
        self.Customers = []

    def write_to_file(self, obj):
        f = open(self.datei, 'wb')
        pickle.dump(obj, f)
        print("Object succesfully added")
        f.close()

    def load(self):
        with open(self.datei, 'rb') as f:
            object_list = []
            while True:
                try:
                    obj = pickle.load(f)
                    object_list.append(obj)
                except EOFError:
                    break
        return object_list

    def update(self, id, new_Name = None,  new_Adresse = None):
            self.Customers = self.load()
            self.Customers.pop(id - 1)
            new_Kunde = Kunde(id, new_Name, new_Adresse)
            self.Customers.append(new_Kunde)
            self.write_to_file(self.Customers)

def test_update_Kunden_Name():
    repo = Repo("test_file.pickle")
    client = Kunde(1, "Christian", "Hoho.Str")
    repo.write_to_file(client)
    repo.update(1, "Ion", "Hoho.Str")
    updated_client = repo.load()[0][0]
    assert updated_client.Name == "Ion"


test_update_Kunden_Name()
