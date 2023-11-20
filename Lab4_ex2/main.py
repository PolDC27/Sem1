
def numara_schimbari(wort1):
    nr = 0
    f = open('../pythonProject/Aufgabe_2/meine_datei.txt', 'r')
    for line in f:
        for word in line.split():
            if word == wort1:
                nr += 1
    f.close()
    return nr
def modifica_datei(wort1,wort2):
    f = open('../pythonProject/Aufgabe_2/meine_datei.txt', 'r')
    data = f.read()
    f.close()
    data = data.replace(wort1, wort2)
    f = open('../pythonProject/Aufgabe_2/meine_datei.txt', 'w')
    f.write(data)
    f.close()

def main():
    wort1 = input("Wort zu ersetzen=")
    wort2 = input("Wort das ersetzt=")
    if numara_schimbari(wort1) == 0:
        print('Nici un cuvant nu a fost modificat')
    else:
        print('Au fost gasite si modificate', numara_schimbari(wort1), 'cuvinte')
        modifica_datei(wort1, wort2)

main()

