def perf_zahl(x):
    sum = 0
    for t in range(1, x // 2+1):
        if x % t == 0:
            sum += t
    if sum == x:
        return True
    return False


def perf_spalten(matrix):
    for i in range(len(matrix)):
        sum = 0
        for j in range(len(matrix)):
            sum += matrix[j][i]
        if not perf_zahl(sum):
            return False
    return True


def linien(matrix):
    a = []
    for i in range(len(matrix)):
        suma = 0
        max = -5
        for j in range(len(matrix)):
            suma += matrix[i][j]
            if matrix[i][j] > max:
                max = matrix[i][j]
        if suma - max == max:
            a.append(True)
        else:
            a.append(False)
    return a


def lang_wort():
    with open("datei.txt", "r") as f:
        list = []
        data = f.readline()
        while data:
            words = data.split()
            max = len(words[1])
            for word in words:
                if len(word) > max:
                    max = len(word)
            list.append(max)
            data = f.readline()
    return list


def verif_palind(x):
    for ch in range(len(x) // 2):
        if x[ch] != x[-1-ch]:
            return False
    return True


def data_pal():
    dict = {}
    with open("datei.txt",'r') as file:
        data = file.readline()
        while data:
            words = data.split()
            for word in words:
                if verif_palind(word) and word in dict:
                    dict[word] += 1
                elif verif_palind(word):
                    dict[word] =1
            data = file.readline()
    return dict


def new_data():
    with open("datei.txt", "r") as f:
        data = f.readline()
        with open("palin.txt", "w") as file:
            while data:
                words = data.split()
                for word in words:
                    if verif_palind(word):
                        file.write('\n' + word)
                data = f.readline()

def main():
    print(perf_spalten([[4, 3, 10], [1, 2, 10], [1, 1, 8]]))
    print(linien([[4, 3, 1],
                  [1, 2, 1],
                 [0, 5, 1]]))
    print(lang_wort())
    print(data_pal())
    new_data()

main()
