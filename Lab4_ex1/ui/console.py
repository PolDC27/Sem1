from Repository.Buchstaben import dict
from Repository.costom_commands import *


def deseneaza_cuvant(cuvant):
        turtle.up()
        turtle.goto(-200, 0)
        turtle.down()
        for ch in cuvant:
                dict[ch]()



def deseneaza_manual():
        turtle.listen()
        turtle.onkey(w, 'w')
        turtle.onkey(a, 'a')
        turtle.onkey(s, 's')
        turtle.onkey(d, 'd')
        turtle.onkey(f, 'f')
        turtle.onkey(g, 'g')
        turtle.onkey(close_window, 'Return')
        turtle.done()




