import pickle
from Repository.CustomerRepo import CustomerRepo
from Repository.CookedDishRepo import CookedDishRepo
from Repository.DrinkRepo import DrinkRepo
from Repository.OrderRepo import OrderRepo



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
                    preis = input("preis:")
                    Portionsgrosse = input("Portionsgrosse:")
                    Alkoholgehalt = input("Alkoholgehalt:")
                    self.controller.add_Getrank_to_repo(id, preis, Portionsgrosse, Alkoholgehalt)

                elif Alegere2 == 3:
                    Preis = input("preis:")
                    Portionsgrosse = input("Portionsgrosse:")
                    Zubereitungszeit = input("Zubereitungszeit:")
                    self.controller.add_GekochterGericht_to_repo(id, Zubereitungszeit, Portionsgrosse, Preis)

                else:


                    Kunden_Id = int(input("Kunden_id:"))
                    preis_Gericht = int(input("Preis Gericht="))
                    Liste_Gerichte = []

                    while preis_Gericht != 0:
                        Liste_Gerichte.append(preis_Gericht)
                        preis_Gericht = int(input("Preis Gericht="))

                    Liste_Getranke = []
                    preis_Getrank = int(input("Preis Getrank="))
                    while preis_Getrank != 0:
                        Liste_Getranke.append(preis_Getrank)
                        preis_Getrank = int(input("Preis Getrank="))

                    self.controller.add_Bestellung_to_repo(id, Kunden_Id, Liste_Gerichte, Liste_Getranke)

            elif Alegere == 2:
                self.controller.read()
                id = int(input("id:"))
                self.controller.delete(id)


            elif Alegere == 3:
                print("""Ce doresti sa modifici?
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
                    self.controller.update_Kunde(id, Name, Adresse)

                elif Alegere2 == 2:
                    preis = input("preis:")
                    Portionsgrosse = input("Portionsgrosse:")
                    Alkoholgehalt = input("Alkoholgehalt:")
                    self.controller.update_Getrank(id, preis, Portionsgrosse, Alkoholgehalt)

                elif Alegere2 == 3:
                    Preis = input("preis:")
                    Portionsgrosse = input("Portionsgrosse:")
                    Zubereitungszeit = input("Zubereitungszeit:")
                    self.controller.update_GekochterGericht(id, Preis, Portionsgrosse, Zubereitungszeit)

                else:
                    with open("Kunden.dat", 'rb') as f:
                        while True:
                            try:
                                obj = pickle.load(f)
                                print(obj)
                            except EOFError:
                                break
                    Kunden_Id = int(input("Kunden_id:"))
                    with open("Gerichte.dat", 'rb') as f:
                        while True:
                            try:
                                obj = pickle.load(f)
                                print(str(obj))
                            except EOFError:
                                break

                    preis_Gericht = int(input("Gericht id="))
                    Liste_Gerichte = []

                    while preis_Gericht != 0:
                        Liste_Gerichte.append(preis_Gericht)
                        with open("Gerichte.dat", 'rb') as f:
                            while True:
                                try:
                                    obj = pickle.load(f)
                                    print(str(obj))
                                except EOFError:
                                    break

                        preis_Gericht = int(input("Gericht id="))

                    Liste_Getranke = []
                    with open("Drink.dat", 'rb') as f:
                            while True:
                                try:
                                    obj = pickle.load(f)
                                    print(str(obj))
                                except EOFError:
                                    break
                    preis_Getrank = int(input("Gericht id="))
                    while preis_Getrank != 0:
                        Liste_Getranke.append(preis_Getrank)
                        with open("Drink.dat", 'rb') as f:
                            while True:
                                try:
                                    obj = pickle.load(f)
                                    print(str(obj))
                                except EOFError:
                                    break
                        preis_Getrank = int(input("Gericht id="))
                    self.controller.update_Bestellung(id, Kunden_Id, Liste_Gerichte, Liste_Getranke)

            elif Alegere == 4:
               self.controller.read()


            else:
                return False

