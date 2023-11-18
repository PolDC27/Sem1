def create_dict(s):
    d ={ }
    for ch in s:
        if ch in d.keys():
            d[ch] += 1
        else:
            d[ch] = 1
    return d

def add_tags(tags, s):
    new1 = '<'
    new2 = '>'
    new3 = '</'
    s = new1 + tags + new2 + s + new3 + tags + new2
    print(s)


def check_pal(s):
    for ch in range(len(s) // 2):
        if s[ch] != s[-(ch+1)]:
            print('nu este palindrom')
            return False
    print('este palindrom')


def fakultat(x):
    p = 1
    for nr in range(1, x+1):
        p *= nr
    print(x,'! =',p)


def eind_buch(s):
    anz = 0
    d = {}
    for ch in s:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1
    for ch in d:
        if d[ch] == 1:
            anz += 1
    print(anz)


def ver_anagrame(s,p):
    if s == p:
        print('cuvintele sunt identice')
        return False
    if create_dict(s) == create_dict(p):
        print('cuvintele sunt anagrame')
    else:
        print('cuvintele nu sunt anagrame')


def ceaser_encrypt(s,nr):
    d = ''
    for ch in s:
        d += chr(ord(ch)+nr)
    return d


def str_find(target, source):
    str =""
    t = 0
    pos = 0
    if source in target:
        for i in range(len(target)-1):
            if target[i] == source[t]:
                if t == 0:
                    pos = i
                str += target[i]
                t += 1
            else:
                t = 0
                str = ''
        print(pos)
    else:
        print(-1)




def main():
    print(create_dict('ana'))
    add_tags('i', 'mama')
    check_pal('an')
    fakultat(4)
    eind_buch("iona")
    ver_anagrame('ama', 'mama')
    print(ceaser_encrypt('ana', 3))
    str_find("testing", "ing")

main()
