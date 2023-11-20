import turtle
from Repository.Buchstaben import dict
from Repository.costom_commands import *


def deseneaza_cuvant(cuvant):
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
        with open("keys.txt", "a") as F:
                F.write("\n")
        turtle.exitonclick()



