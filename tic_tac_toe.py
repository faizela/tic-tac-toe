print("This is a Tic Tac Toe Game")
print('-----------------------------')
board = ['-','-','-',
        '-','-','-',
        '-','-','-']

choices = ['X', 'O']

while True:
    p1_letter = input("Player 1 - What letter would you like to choose 'X' or 'O' ")
    p2_letter = ''

    if p1_letter.upper() == 'X':
        p2_letter = p2_letter + choices[1]
        print(f'Player two your choice will be {p2_letter}')
        break
    elif p1_letter.upper() == 'O':
        p2_letter = p2_letter + choices[0]
        print(f'Player two your choice will be {p2_letter}')
        break
    else:
        print('Enter a letter X or O')
            
        

def game_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('---------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('---------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

def cols_win_x(board):
    return board[0] == 'X' and board[3] == 'X' and board[6] == 'X' or \
    board[1] == 'X' and board[4] == 'X' and board[7] == 'X' or \
    board[2] == 'X' and board[5] == 'X' and board[8] == 'X'

def rows_win_x(board):
    return board[0] == 'X' and board[1] == 'X' and board[2] == 'X' or \
    board[3] == 'X' and board[4] == 'X' and board[5] == 'X' or \
    board[6] == 'X' and board[7] == 'X' and board[8] == 'X'

def diagnols_win_x(board):
    return board[0] == 'X' and board[4] == 'X' and board[8] == 'X' or \
    board[2] == 'X' and board[4] == 'X' and board[6] == 'X'

def cols_win_o(board):
    return board[0] == '' and board[3] == 'O' and board[6] == 'O' or \
    board[1] == '0' and board[4] == '0' and board[7] == '0' or \
    board[2] == '0' and board[5] == '0' and board[8] == '0'

def rows_win_o(board):
    return board[0] == 'O' and board[1] == 'O' and board[2] == '0' or \
    board[3] == 'O' and board[4] == 'O' and board[5] == '0' or \
    board[6] == '0' and board[7] == '0' and board[8] == '0'

def diagnols_win_o(board):
    return board[0] == 'X' and board[4] == 'X' and board[8] == 'X' or \
    board[2] == 'X' and board[4] == 'X' and board[6] == 'X'


game_board()
print() # for space
running = True
while running:
    allowed_nums = [1,2,3,4,5,6,7,8,9]
    P1_WIN_MSG = 'Player 1 Wins!'
    P2_WIN_MSG = 'Player 2 Wins!'
    # if running:
    #     player_2_str = input(f'Player_2 - Where would You like to place your {p1_letter.upper()} in which cell block [1 - 9]? ')
    try:
        player_1_int = int(input(f'Player_1 - Where would You like to place your {p1_letter.upper()} in which cell block [1 - 9]? '))
        # player_2_int = int(player_2_str)
        if player_1_int not in allowed_nums:
            print('Enter a valid number from 1 to 9')
        for num in allowed_nums:
            if num == player_1_int:
                board[num - 1] = p1_letter.upper()
                game_board()
                if rows_win_x(board) and p1_letter.upper() == 'X':
                    # print()
                    # print(P1_WIN_MSG)#
                    # print()
                    running = False
                    game_board()
                    print(P1_WIN_MSG)

                # if cols_win_x(board) and p1_letter.upper() == 'X':
                #     print(P1_WIN_MSG)
                #     running = False
                # if diagnols_win_x(board) and p1_letter.upper() == 'X':
                #     print(P1_WIN_MSG)
                #     running = False
                # if rows_win_o(board) and p1_letter.upper() == 'O':
                #     print(P1_WIN_MSG)
                #     running = False
                # if cols_win_o(board) and p1_letter.upper() == 'O':
                #     print(P1_WIN_MSG)
                #     running = False
                # if diagnols_win_o(board) and p1_letter.upper() == 'O':
                #     print(P1_WIN_MSG)
                #     running = False

            # elif num == player_2_int:
            #     board[num - 1] = p2_letter.upper()
            #     if running:
            #         game_board()
                # print()
            #     if rows_win_x(board) and p2_letter.upper() == 'X':
            #         print(P2_WIN_MSG)
            #         running = False
            #     if cols_win_x(board) and p2_letter.upper() == 'X':
            #         print(P2_WIN_MSG)
            #         running = False
            #     if diagnols_win_x(board) and p2_letter.upper() == 'X':
            #         print(P2_WIN_MSG)
            #         running = False
            #     if rows_win_o(board) and p2_letter.upper() == 'O':
            #         print(P2_WIN_MSG)
            #         running = False
            #     if cols_win_o(board) and p2_letter.upper() == 'O':
            #         print(P2_WIN_MSG)
            #         running = False
            #     if diagnols_win_o(board) and p2_letter.upper() == 'O':
            #         print(P2_WIN_MSG)
            #         running = False
            
            # else:
            #     print("It's a draw")
            

                

    except ValueError:
            print('Enter a valid number between 1 to 9')










  






















