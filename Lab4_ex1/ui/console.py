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

def adauga_char(file, input):
        d = {}
        i = 0
        for line in file:
                d[i] = line.strip()
                i += 1
        for ch in d[input]:
                if ch == 'w':
                        w2()
                elif ch == 's':
                        s2()
                elif ch == 'a':
                        a2()
                elif ch == 'd':
                        d2()
                elif ch == 'f':
                        f2()
                elif ch == 'g':
                        g2()







