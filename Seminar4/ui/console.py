from Repository.functii import add_frac, sum_frac, minim, maxim, delete
l = []
def menu():
    print("1. Einfugen")
    print("2. Summe aller Zahlen")
    print("3. Minimum")
    print("4. Maximum")
    print("5. Loschen")
    print("0. Exit")

def run_menu():
    while True:
        menu()
        choice = input('Was willst du machen? opt=')
        if choice == '1':
            add_frac(l)
        elif choice == '2':
            print(sum_frac(l))
        elif choice == '3':
            print(minim(l))
        elif choice =='4':
            print(maxim(l))
        elif choice == '5':
            print(delete(l))
        elif choice == '0':
            break



