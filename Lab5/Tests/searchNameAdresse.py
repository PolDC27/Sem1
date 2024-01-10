import pickle
from Ui.ui import generate_search_list
from Modelle.Kunde import Kunde
class Repo:
    def __init__(self, datei):
        self.datei = datei

    def write_to_file(self, obj):
        f = open(self.datei, 'ab')
        pickle.dump(obj, f)
        print("Object succesfully added")
        f.close()


def test_search_by_name():
    repo = Repo("test_file.pickle")
    client = Kunde(1, "Christian", "Hoho.Str")
    repo.write_to_file(client)
    searched_client = generate_search_list("test_file.pickle", "Chr")
    assert searched_client[0].Name == client.Name
    assert searched_client[0].Adresse == client.Adresse
    searched_client = generate_search_list("test_file.pickle", "Ho")
    assert searched_client[0].Name == client.Name
    assert searched_client[0].Adresse == client.Adresse
test_search_by_name()
