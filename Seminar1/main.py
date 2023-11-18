def sum(a,b):
    return a+b


def lungime_nume(nume, prenume):
    return sum(len(nume),len(prenume))


def suma_folge():
    s = 0
    while True:
        x = int(input('x='))
        if x == 0:
            break
        else:
            s += x
    print(s)


def remove_repetitions(s):
    temp = ''
    for ch in s:
        if ch not in temp:
            temp +=ch
    s = temp
    print(s)


def is_prim(x):
    for t in range(2, x // 2 + 1):
        if x % t == 0:
            return False
    return True


def main():
    a = int(input ('a='))
    b = int(input ('b='))
    zeichenkette = (input('zeichenkette='))
    nume = input('Care este numele tau?')
    prenume = input('Care este prenumele tau?')
    n = int(input('n='))

    s = sum(a, b)
    lungime = lungime_nume(nume, prenume)

    print('Salut', nume, prenume, '\n', 'Numele si prenumele tale contin in total', lungime, 'litere')
    print(s)
    suma_folge()

    remove_repetitions(zeichenkette)
    for i in range(2, n):
        if is_prim(i):
            print(i)

main()
