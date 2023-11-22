
from ui.console import deseneaza_cuvant,adauga_char
from ui.console import deseneaza_manual

def draw_word():
    word = input('word=')
    deseneaza_cuvant(word)


def menu():
    return  """
            Alege ce sa faci:
            Opt = 1 : Deseneaza un cuvant automat
            Opt = 2 : Adauga si deseneaza manual un caracter
            """

def menu_manual():
    return """
            Miscari posibile:
            W - Move Forward
            A - Move Left 45 degrees
            S - Move Backward
            D - Move Right 45 degrees
            F - Pen up
            G- Pen Down
            """

def alegere():
        print(menu())
        opt = int(input('opt='))
        if opt == 1:
            alegere = str(input('Doresti sa desenezi un caracter costom?'))
            if alegere == "nu":
                draw_word()
            elif alegere == "da":
                alegere1 = int(input("Al catelea il doresti desenat"))
                draw_word()
                with open("keys.txt", 'r') as F:
                    adauga_char(F, alegere1)

        elif opt == 2:
            print(menu_manual())
            deseneaza_manual()
            with open("keys.txt", "a") as F:
                F.write("\n")




