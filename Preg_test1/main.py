from math import sqrt

def adjacent(matrix, nodes):
    if matrix[nodes[0]][nodes[1]] == 1:
        return True
    else:
        return False


def v_dac(x):
    dac = round(x * 5 / 1023, 2)
    return dac


def str_to_int(x):
    x = ord(x) - ord('0')
    return x


def int_to_str(x):
    nr = x + ord('0')
    x = chr(nr)
    return x


def right_shift(x, times):
    t = 1
    for i in range(times - 1):
        t *= 2
    return round(x / t)


def line_length(point1, point2):
    return round(sqrt((point2[0]-point1[0]) ** 2 + (point2[1] - point1[1]) ** 2), 2)


def top_note(elev):
    dict = {}
    dict[list(elev.values())[0]] = max(list(elev.values())[1])
    return dict


def profit(vanzari):
    return round(list(vanzari.values())[2]* (list(vanzari.values())[1] - list(vanzari.values())[0]))


def interview(list,total):
    if total > 120 or len(list) != 8:
        print('disqualified')
        return False

    lim = 5
    for i in range(len(list)):
        if i % 2 == 0 and i !=0:
            lim += 5
        if list[i] > lim:
            print('disqualified')
            return False

    print('qualified')


def snake(x):
    max = x * x
    i = 1
    nr = 0
    while i*2 <= max:
        nr += 1
        i *= 2
    return nr


def arithmetic(string):
    if '+' in string:
        numere = string.split(' + ')
        return int(numere[0])+int(numere[1])
    elif '*' in string:
        numere = string.split(' * ')
        return int(numere[0])*int(numere[1])
    elif '-' in string:
        numere = string.split(' - ')
        return int(numere[0])-int(numere[1])
    elif '//' in string:
        numere = string.split(' // ')
        if int(numere[1]) == 0:
            return -1
        return int(numere[0])//int(numere[1])


def morse(string):
    char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}
    word = ''
    for ch in string:
        if ch in char_to_dots:
            word += char_to_dots[ch]
    return word


def is_disarium(x):
    lungime = len(str(x))
    aux = x
    s = 0
    while aux > 0:
        s += (aux % 10) ** lungime
        aux //= 10
        lungime -= 1
    return s == x


def encrypt(string):
    dictionar = {"a": '0', 'e':'1', 'i':'2', 'o': '2', 'u': '4'}
    encryption = ''
    l = []
    for ch in range(len(string)-1, -1, -1):
        l.append(string[ch])
    for ch in range(len(l)):
        if l[ch] in 'aeiou':
            l[ch] = dictionar[l[ch]]
        encryption += l[ch]
    encryption += 'aca'
    return encryption


def consecutive_combo(list1,list2):
    list3 = list1+list2
    list3.sort()
    for i in range(len(list3)-1):
        if list3[i] + 1 != list3[i+1]:
            return False
    return True


def tallest_skyscraper(matrix):
    max = 0
    for i in range(len(matrix)):
        nr = 0
        for j in range(len(matrix[0])):
            if matrix[j][i] == 1:
                nr += 1
        if nr > max:
            max = nr
    return max


def sum_mat(matrix):
    dict = {'#': 5, "O": 3, "X": 1, "!": -1, '!!': -3, '!!!': -5}
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            sum += dict[matrix[i][j]]
    if sum < 0:
        return 0
    else:
        return sum


def main():
    print(adjacent([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]], (0, 1)))
    print(v_dac(400))
    print(str_to_int('4'))
    print(int_to_str(4))
    print(right_shift(-512, 10))
    print(line_length([15, 7], [22, 11]))
    print(top_note({"name": "john", "notes": [5, 10, 4]}))
    print(profit({"cost_price": 32.67, "sell_price": 45.00, "inventory": 1200}))
    interview([5, 5, 10, 10, 15, 15, 20, 20], 120)
    print(snake(24))
    print(arithmetic('20 // 20'))
    print(morse('CASA'))
    print(is_disarium(518))
    print(encrypt('apple'))
    print(consecutive_combo([7, 4, 5, 1], [2, 3, 6]))
    print(tallest_skyscraper([
                [0, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 1, 0],
                [1, 1, 1, 1]]))
    print(sum_mat([
  ["#", "O", "#", "!!", "X", "!!", "#", "O", "O", "!!", "#", "X", "#", "O"],
  ["!!!", "!!!", "!!", "!!", "!", "!", "X", "!", "!!!", "O", "!", "!!!", "X", "#"],
  ["#", "X", "#", "!!!", "!", "!!", "#", "#", "!!", "X", "!!", "!!!", "X", "O"],
  ["!!", "X", "!!", "!!", "!!!", "#", "O", "O", "!!!", "#", "O", "O", "#", "!!"],
  ["O", "X", "#", "!", "!", "X", "!!!", "O", "!!!", "!!", "O", "!", "O", "X"],
  ["!!", "!!!", "X", "!!!", "!!", "!!", "!!!", "X", "O", "!", "#", "!!", "!!", "!!!"],
  ["!!", "!!", "#", "O", "!", "!!", "!", "!!!", "#", "O", "#", "!", "#", "!!"],
  ["X", "X", "O", "X", "!!!", "#", "!!!", "!!!", "X", "X", "X", "!", "#", "!!"],
  ["O", "!!!", "!", "O", "#", "!", "!", "#", "X", "X", "#", "O", "!!", "!"],
  ["X", "!", "!!", "#", "#", "X", "!!", "O", "!!", "X", "X", "!!", "#", "X"],
  ["!", "!!", "!!", "O", "!!", "!!", "#", "#", "!", "!!!", "O", "!", "#", "#"],
  ["!", "!!!", "!!", "X", "!!", "!!", "#", "!!!", "O", "!!", "!!!", "!", "!", "!"],
  ["!!!", "!!!", "!!", "O", "!", "!", "!!!", "!!!", "!!", "!!", "X", "!", "#", "#"],
  ["O", "O", "#", "O", "#", "!", "!!!", "X", "X", "O", "!", "!!!", "X", "O"]
]))


main()
