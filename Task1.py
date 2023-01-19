# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит заданное количество конфет. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.

# a) Добавьте игру против бота

# b) Подумайте как наделить бота 'интеллектом'
import random

opt = ''
while opt != 'human' or opt != 'bot':
        opt = input('Do you want to play with a human or with a bot? \n')
        if opt == 'human':
            break
        elif opt == 'bot':
            break
        else:
            print('Write "human" or "bot" \n')


while True:
    try:
        amount_of_candies = int(input('Enter the amount of candies: \n'))
        break
    except:
        print('Enter a number')

def play_human(player):
    while True:
        try:
            candies = int(input(f'Player {player}, how many candies would you like to take? \n'))
            if not 0 < int(candies) < 29:
                print('Enter a number between 0 and 28')
                ValueError
            else:
                break
        except ValueError:
            print('Enter a number between 0 and 28')
    return candies

    
def human(amount_of_candies):

    player = random.randint(1,2)

    if player == 1:
        print(f'Player 1 goes first')
    else:
        print(f'Player 2 goes first')

    while amount_of_candies > 0:

        print(f'Player {player} turn')
        candies = play_human(player)
        amount_of_candies -= candies
        if amount_of_candies > 0:
            print(f'{amount_of_candies} candies left')
        else:
            print(f'Player {player} is winner')

        if player == 1:
            player = 2
        else:
            player = 1


def bot(amount_of_candies):

    player = random.randint(1,2)

    if player == 1:
        player = '1'
        print(f'Player {player} goes first')
    else:
        player = 'Bot'
        print(f'{player} goes first')

    while amount_of_candies > 0:
        print(f'Player {player} turn')
        if player == '1':
            candies = play_human(player)
            amount_of_candies -= candies
            if amount_of_candies > 0:
                print(f'{amount_of_candies} candies left')
            else:
                print(f'Player{player} is winner')
            player = 'Bot'
        else:
            candies = amount_of_candies%29
            if candies == 0:
                candies += random.randint(0, 28)
            print(f'The bot took {candies} candies')
            amount_of_candies -= candies

            if amount_of_candies > 0:
                print(f'{amount_of_candies} candies left')
            else:
                print(f'{player} is winner')           
            player = '1'
        
if opt == human:
    human(amount_of_candies)
else:
    bot(amount_of_candies)