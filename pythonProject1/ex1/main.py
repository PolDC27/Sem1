from ex1.dice import Dice

def main():
    dice = Dice(6)
    print(dice.throw())
    while True:
        result = dice.throw()
        print(result)
        if result == 6:
            break

main()
