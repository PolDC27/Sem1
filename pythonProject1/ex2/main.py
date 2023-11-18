from ex2.fractii import Fraction
def main():
    frac = Fraction(1000, 5)
    frac.reduce()
    print(frac.n, frac.m)

main()
