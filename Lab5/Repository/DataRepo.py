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
                    object_list.append(obj)
                except EOFError:
                    break
        return object_list


    def clear_file(self):
        with open(self.datei, 'wb') as f:
            pickle.dump(None, f)

    def read_file(self):
        f = open(self.datei, 'rb')
        for line in f:
            print(str(line))
        f.close()


    def write_to_file(self, obj):
        f = open(self.datei, 'ab')
        pickle.dump(obj, f)
        print("Object succesfully added")
        f.close()


    def delete(self, Id):
        objs = self.load()
        if len(objs) == 1:
            self.clear_file()
        else:
            objs.pop(Id - 1)
            for obj in objs:
                self.save(obj)


    def convert_to_string(self, obj_Liste):
        pass


    def convert_from_string(self, string):
        pass






