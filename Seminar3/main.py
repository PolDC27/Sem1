def check_sum(l, nr):
    l.sort()
    left = 0
    right = len(l)-1
    while left < right:
        if l[left] + l[right] == nr:
            return True
        elif l[left] + l[right] > nr:
            right -= 1
        else:
            left += 1
    if left >= right:
        return False


def generate_multiple(nr, length):
    l = [nr]
    for i in range(2, length+1):
        l.append(nr * i)
    return l


def big_sum(a, b):
    c = ''
    nr = 0
    i = -1
    for i in range(len(a)-1, -1, -1):
        sum = int(a[i])+int(b[i])
        c = str(nr + sum % 10) + c
        if sum > 10:
            nr = 1
        else:
            nr = 0
    return c


def reverse(word):
    cuvant = ''
    l = []
    for i in word:
        if i in 'AEIOUaeiou':
            l.append(i)
    for i in range((len(l))//2):
        l[i], l[-1-i] = l[-1-i], l[i]
    j = 0
    for i in range(len(word)):
        if word[i] in  'AEIOUaeiou':
            cuvant += l[j]
            j += 1
        else:
            cuvant += word[i]
    print(cuvant)


def big_sum2(a,b):
    d = ''
    if len(a) < len(b):
        b, a = a, b
    c = ''
    for i in range(len(a)-len(b)):
        c += a[i]
    for i in range(len(a)-len(b), len(a)):
        d += a[i]
    c += big_sum(d, b)
    return c



def main():
    print(check_sum([2, 9, 1], 3))
    print(generate_multiple(3, 4))
    print(big_sum('1212312231231', '5553412313231'))
    reverse('Terminator')
    print(big_sum2('1234556544345', '2343234'))


main()
