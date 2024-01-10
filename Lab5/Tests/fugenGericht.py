
from Modelle.GekochterGericht import GekochterGericht
import pickle

class Repo:
    def __init__(self, datei):
        self.datei = datei


    def write_to_file(self, obj):
        f = open(self.datei, 'ab')
        pickle.dump(obj, f)
        print("Object succesfully added")
        f.close()

def test_write_to_file():
    repo = Repo('test_file.pickle')
    obj = GekochterGericht(1, 25, 25, 25)
    repo.write_to_file(obj)

    with open('test_file.pickle', 'rb') as f:
        loaded_obj = pickle.load(f)

    assert loaded_obj.Id == obj.Id
    assert loaded_obj.Zubereitungszeit == obj.Zubereitungszeit
    assert loaded_obj.Portionsgrosse == obj.Portionsgrosse
    assert loaded_obj.Preis == obj.Preis

test_write_to_file()
