import pickle

class DataRepo:
    def __init__(self, datei):
        self.datei = datei


    def save(self, Liste):
        f = open(self.datei, 'wb')
        pickle.dump(Liste, f)
        f.close()


    def load(self):
        with open(self.datei, 'rb') as f:
            object_list = []
            while True:
                try:
                    obj = pickle.load(f)
                    object_list.append(str(obj))
                except EOFError:
                    break
        return object_list



    def read_file(self):
        f = open(self.datei, 'rb')
        for line in f:
            print(str(line))
        f.close()


    def write_to_file(self, obj_List):
        f = open(self.datei, 'ab')
        pickle.dump(obj_List, f)
        print("Object succesfully added")
        f.close()


    def delete(self, Id):
        objs = self.load()
        if Id < len(objs):
            objs.pop(Id)
        self.save(objs)


    def convert_to_string(self, obj_Liste):
        pass


    def convert_from_string(self, string):
        pass






