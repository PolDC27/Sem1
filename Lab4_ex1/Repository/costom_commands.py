import turtle
def w():
    with open("keys.txt", "a") as f:
        turtle.forward(10)
        f.write("w ")


def s():
    with open("keys.txt", "a") as f:
        turtle.backward(10)
        f.write("s ")


def d():
    with open("keys.txt", "a") as f:
        turtle.right(45)
        f.write("d ")


def a():
    with open("keys.txt", "a") as f:
        turtle.left(45)
        f.write("a ")


def f():
    with open("keys.txt", "a") as f:
        turtle.up()
        f.write("f ")


def g():
    with open("keys.txt", "a") as f:
        turtle.down()
        f.write("g ")

