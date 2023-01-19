# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом

def input_validation():
    while True:
        try:
            x = input(f'Your turn, player {player} \n')
            if 0 < int(x) < 10 and not x in buf:
                break
            else:
                print('Enter a number between 0 and 10 of unused numbers')
        except:
            print('Enter a number between 0 and 10 of unused numbers')
    buf.append(x)
    return x

def victory_check(playing_field):
    winner = 0
    for i in range(len(playing_field) - 2):
        if playing_field[i] == playing_field[i+1] == playing_field[i+2]:
            winner = 1
            print(f'Player {player} is a winner')
    for i in range(len(playing_field) - 8):
        if playing_field[i] == playing_field[i+4] == playing_field[i+8]:
            winner = 1
            print(f'Player {player} is a winner')
    if my_playing_field[0] == my_playing_field[5] == my_playing_field[-1]:
        winner = 1
        print(f'Player {player} is a winner')
    if my_playing_field[2] == my_playing_field[5] == my_playing_field[-3]:
        winner = 1
        print(f'Player {player} is a winner')
    if count == 9:
        print(f'Dead heat')
        winner = 1
    
    return winner

my_playing_field = [' 1 ', ' 2 ', ' 3 ', '\n', ' 4 ', ' 5 ', ' 6 ', '\n', ' 7 ', ' 8 ', ' 9 ']
winner = 0
player = ' X '
playing_field = ''
count = 0
buf = []

for i in my_playing_field:
    playing_field += i
print(playing_field)

while winner == 0:

    x = input_validation()

    for i in range(len(my_playing_field)):
        if x in my_playing_field[i] and my_playing_field[i] !=' X ' != ' O ':
            print(my_playing_field[i])
            my_playing_field[i] = my_playing_field[i].replace(my_playing_field[i], f'{player}')


        # print('This cell is occupied')

    playing_field = ''

    for i in my_playing_field:
        playing_field += i
    print(playing_field)

    count += 1
    winner = victory_check(my_playing_field)
    if player == ' X ':
        player = ' O '
    else:
        player = ' X '
    

