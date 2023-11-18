def add(a, b):
    sum = (b[1]*a[0] + a[1]*b[0], a[1]*b[1])
    return sum

def sub(a, b):
    dif =(b[1]*a[0] - a[1]*b[0], a[1]*b[1])
    return dif

def mult(a,b):
    mul = (a[0]*b[0], a[1]*b[1])
    return mul

def div(a,b):
    imp = (a[0]*b[1], a[1]*b[0])
    return imp

def ggt(a, b):
    c, d = a, b
    while c !=d:
        if c > d:
            c-= d
        else:
            d -= c
    return d

def reduce(a):
    while ggt(a[0], a[1]) != 1:
        a = (a[0] // ggt(a[0], a[1]), a[1] // ggt(a[0], a[1]))
    return a

def add_frac(l):
    numarator = int(input('numarator='))
    numitor = int(input('numitor='))
    a = (numarator, numitor)
    l.append(reduce(a))
    print(l)

def delete(l):
    nr_fractie = int(input("nr_fractie="))
    del l[nr_fractie]
    return l

def sum_frac(l):
    sum = (0, 1)
    for i in l:
        sum = add(sum, i)
    return reduce(sum)

def maxim(l):
    max = (0, 1)
    for i in l:
        if i[0] / i[1] > max[0] / max[1]:
            max = i
    return max

def minim(l):
    min = (1, 1)
    for i in l:
        if i[0] / i[1] < min[0] / min[1]:
            min = i
    return min

