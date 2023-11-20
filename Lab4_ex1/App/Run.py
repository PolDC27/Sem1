import turtle
from ui.console import deseneaza_cuvant
from ui.console import deseneaza_manual
def draw_word():
    word = input('word=')
    deseneaza_cuvant(word)
    turtle.exitonclick()


def menu():
    return  """
            Alege ce sa faci:
            Opt = 1 : Deseneaza un cuvant automat
            Opt = 2 : Adauga si deseneaza manual un caracter
            """
def alegere():
        print(menu())
        opt = int(input('opt='))
        if opt == 1:
            draw_word()
        elif opt == 2:
            deseneaza_manual()

def run():
    alegere()

