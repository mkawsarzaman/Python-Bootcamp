from IPython.display import clear_output

def display_board(board_list): #for displaying the game board, corresponding positions are numpad positions of keypad
    print(board_list[7]+'  |  '+ board_list[8]+'  |  '+ board_list[9])
    print('---|-----|---')
    print(board_list[4]+'  |  '+ board_list[5]+'  |  '+ board_list[6])
    print('---|-----|---')
    print(board_list[1]+'  |  '+ board_list[2]+'  |  '+ board_list[3])

def player_select():
    from random import randint
    if randint(0,1) == 0:
        return 'player1'
    else:
        return 'player2'

def player_input(): #for assigning 2 players with markers 'X' or 'O'
    marker = ' '
    while marker not in ['X','O']:
        marker = input('Player 1: please choose between X or O: ').upper()
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    print(f'player 1 has selected {player1} and player 2 has selected {player2}')
    return (player1,player2)

def select_position():
    position = 'dadadaffafa'
    while position not in range(1,10):
        position = input ('choose among positions 1,2,3,4,5,6,7,8,9: ')
        if position.isdigit() and int(position) in range(1,10):
            return int(position)
        else:
            print('Wrong selection! please select number among 1,2,3,4,5,6,7,8,9')
            continue


def place_marker_on_board(board_list, marker, position): #update board with player input
    board_list[position] = marker
    return board_list

def win_check(board_list,marker): #check horizontal, vertical and diagnal positions of the board for win
    if((board_list[1] == marker and board_list[2] == marker and board_list[3] == marker) or
    (board_list[4] == marker and board_list[5] == marker and board_list[6] == marker) or
    (board_list[7] == marker and board_list[8] == marker and board_list[9] == marker) or
    (board_list[1] == marker and board_list[4] == marker and board_list[7] == marker) or
    (board_list[2] == marker and board_list[5] == marker and board_list[8] == marker) or
    (board_list[3] == marker and board_list[6] == marker and board_list[9] == marker) or
    (board_list[1] == marker and board_list[5] == marker and board_list[9] == marker) or
    (board_list[3] == marker and board_list[5] == marker and board_list[7] == marker)):
            return True
    else:
            return False

#def fullboard_check(board_list):
#    for index,value in enumerate(board_list):
#        if board_list[index] != ' ':
#            return True
#       else:
#           return False

def position_check(board_list,position):
    if board_list[position] == ' ':
        return True
    else:
        return False

def fullboard_check(board_list):
    for position in range(1,10):
        if position_check(board_list, position)== True:
            return False
    return True


def replay():
    game_on = 'adaaefefcf'
    while game_on not in ['Y','y','N','n']:
        game_on = input('do you want to play again? Y or N: ')
        if game_on in ['Y','y']:
            return True
        elif game_on in ['N','n']:
            return False
        else:
            print('select Y or N')
            continue

while True:
    board_list = ['*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    display_board(board_list)
    player1_marker,player2_marker = player_input()
    turn = player_select()
    print(f'{turn} has the first go')
    play_game = input('Ready to play? Y or N')
    if play_game.lower() == 'y':
        game_on = True
    elif play_game.lower() == 'n':
        game_on = False
        print('Run later')
        break

    while game_on == True:
        if turn == 'player1':
            display_board(board_list)
            position = select_position()
            place_marker_on_board(board_list,player1_marker,position)
            if win_check(board_list,player1_marker) == True:
                display_board(board_list)
                print('Player 1 has won')
                game_on = False
            else:
                if fullboard_check(board_list) == True:
                    display_board(board_list)
                    print('There is a draw!')
                    break
                else:
                    turn = 'player2'
        else:
            display_board(board_list)
            position = select_position()
            place_marker_on_board(board_list, player2_marker, position)
            if win_check(board_list, player2_marker) == True:
                display_board(board_list)
                print('Player 2 has won')
                game_on = False
            else:
                if fullboard_check(board_list) == True:
                    display_board(board_list)
                    print('There is a draw!')
                    break
                else:
                    turn = 'player1'

    if replay() == True:
        game_on = True
    else:
        break