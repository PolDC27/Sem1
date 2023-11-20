import random
from joc.win_loss import win, loss
def run():
    l =['schere', 'papier', 'stein']
    user_score = 0
    computer_score = 0
    while True:
        user_input = input('\033[35m Choose your weapon (Schere, Stein, oder Papier):')
        computer_choice = random.choice(l)
        print(' Oponentul a ales:', computer_choice)

        if computer_choice == user_input:
            print("\033[33m Scorul ramane neschimbat ")

        if user_input == 'papier':
            if computer_choice == 'schere':
                computer_score += 1
                print('\033[31m Ai pierdut runda!, score:', user_score, '-', computer_score)
            if computer_choice == 'stein':
                user_score += 1
                print('\033[32m Ai castigat runda!, score:', user_score, '-', computer_score)

        if user_input == 'stein':
            if computer_choice == 'schere':
                user_score += 1
                print('\033[32m Ai castigat runda!, score:', user_score, '-', computer_score)
            if computer_choice == 'papier':
                computer_score += 1
                print('\033[31m Ai pierdut runda!, score:', user_score, '-', computer_score)

        if user_input == 'schere':
            if computer_choice =='stein':
                computer_score += 1
                print('\033[31m Ai pierdut runda!, score:', user_score, '-', computer_score)
            if computer_choice =='papier':
                user_score += 1
                print('\033[32m Ai castigat runda!, score:', user_score, '-', computer_score)

        if win(user_score):
            print('Felicitari pentru victorie!!!')
            return True

        if loss(computer_score):
            print('Computerul a castigat')
            return False

