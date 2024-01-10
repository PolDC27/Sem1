import pickle
from Repository.CustomerRepo import CustomerRepo
from Repository.CookedDishRepo import CookedDishRepo
from Repository.DrinkRepo import DrinkRepo
from Repository.OrderRepo import OrderRepo


def generate_search_list(datei, cautare):
    with open(datei, 'rb') as f:
        Objects = []
        while True:
            try:
                obj = pickle.load(f)
                Objects.append(obj)
            except EOFError:
                    break
    lista_cautari = [obj for obj in Objects if cautare in obj.Name or cautare in obj.Adresse]
    return lista_cautari

def print_list(File):
    with open(File, "rb") as f:
        while True:
            try:
                obj = pickle.load(f)
                print(str(obj))
            except EOFError:
                break


def menu_repo():
        print("""
            Ce repository doresti sa folosesti?
            1. CookedDishRepo
            2. CustomerRepo
            3. DrinkRepo
            4. OrderRepo
            """)
        alegere = int(input())
        if alegere == 1:
            my_repo = CookedDishRepo
        elif alegere == 2:
            my_repo = CustomerRepo
        elif alegere == 3:
            my_repo = DrinkRepo
        else:
            my_repo = OrderRepo

        return my_repo


class ui:
    def __init__(self, controller):
        self.controller = controller

    def menu(self):
        while True:
            print("""Bine ai venit!!! 
                    Ce doresti sa faci?
                    1.Sa adaugi ceva
                    2.Sa stergi un element specific
                    3.Sa modifici un element specific
                    4.Sa vezi lista completa
                    5.Exit        
                    """)
            Alegere = int(input("Introduce numarul corespunzator functionalitatii pe care vrei sa o folosesti:"))

            if Alegere == 1:
                print("""Ce doresti sa adaugi?
                1.Un Client
                2.O Bautura
                3.Un fel de mancare
                4.O comanda
                """)

                Alegere2 = int(input("Introduce numarul corespunzator functionalitatii pe care vrei sa o folosesti:"))
                id = int(input("id:"))

                if Alegere2 == 1:
                    Name = input("Name:")
                    Adresse = input("Adresse:")
                    self.controller.add_Kunde_to_repo(id, Name, Adresse)

                elif Alegere2 == 2:
                    preis = int(input("preis:"))
                    Portionsgrosse = input("Portionsgrosse:")
                    Alkoholgehalt = input("Alkoholgehalt:")
                    self.controller.add_Getrank_to_repo(id, preis, Portionsgrosse, Alkoholgehalt)

                elif Alegere2 == 3:
                    Name = input("Name:")
                    Preis = int(input("preis:"))
                    Portionsgrosse = input("Portionsgrosse:")
                    Zubereitungszeit = input("Zubereitungszeit:")
                    self.controller.add_GekochterGericht_to_repo(id, Name, Zubereitungszeit, Portionsgrosse, Preis)

                else:

                    cautare = input("Cauta Client:")
                    search_List = generate_search_list("Kunden.dat", cautare)

                    for itm in search_List:
                        print(str(itm))
                    kunde_nr = int(input("Al catelea client cautat il doresti"))
                    Kunden_Id = search_List[kunde_nr - 1].Id

                    print_list("Gerichte.dat")
                    Gericht_id = input("Gericht id=")
                    Liste_Gerichte = []

                    while Gericht_id != 0:
                        Liste_Gerichte.append(Gericht_id)
                        Gericht_id = int(input("Gericht id="))

                    print_list("Drink.dat")
                    Liste_Getranke = []
                    Getrank_id = int(input("Getrank id="))

                    while Getrank_id != 0:
                        Liste_Getranke.append(Getrank_id)
                        Getrank_id = int(input("Getrank id="))

                    Datum = input("Datum")
                    Uhrzeit =input("Uhrzeit=")

                    self.controller.add_Bestellung_to_repo(id, Kunden_Id, Liste_Gerichte, Liste_Getranke, Datum, Uhrzeit)

            elif Alegere == 2:
                self.controller.read()
                id = int(input("Al catelea doresti sa-l stergi:"))
                self.controller.delete(id)


            elif Alegere == 3:
                print("""Ce doresti sa modifici?
                    1.Un Client
                    2.O Bautura
                    3.Un fel de mancare
                    """)
                Alegere2 = int(input("Introduce numarul corespunzator functionalitatii pe care vrei sa o folosesti:"))

                if Alegere2 == 1:
                    print_list("Kunden.dat")
                    id = int(input("Al catelea:"))
                    Name = input("Name:")
                    Adresse = input("Adresse:")
                    self.controller.update_Kunde(id, Name, Adresse)

                elif Alegere2 == 2:
                    print_list("Drink.dat")
                    id = int(input("Al catelea:"))
                    preis = int(input("preis:"))
                    Portionsgrosse = input("Portionsgrosse:")
                    Alkoholgehalt = input("Alkoholgehalt:")
                    self.controller.update_Getrank(id, preis, Portionsgrosse, Alkoholgehalt)

                else:
                    print_list("Gerichte.dat")
                    id = int(input("Al catelea:"))
                    Name = input("Name:")
                    Preis = int(input("preis:"))
                    Portionsgrosse = input("Portionsgrosse:")
                    Zubereitungszeit = input("Zubereitungszeit:")
                    self.controller.update_GekochterGericht(id, Name, Preis, Portionsgrosse, Zubereitungszeit)



            elif Alegere == 4:
               self.controller.read()


            else:
                return False

