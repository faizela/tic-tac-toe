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
        p2 = p2_letter + choices[1]
        print(f'Player two your choice will be {p2}')
        break
    elif p1_letter.upper() == 'O':
        p2 = p2_letter + choices[0]
        print(f'Player two your choice will be {p2}')
        break
    else:
        print('Enter a letter X or O')
            
        

def game_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('---------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('---------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

 

game_board()
print() # for space
while True:
    print('The cell blocks are 1 to nine')
    player_1 = input(f'Player_1 - Where would You like to place your {p1_letter.upper()} in which cell block [1 - 9]?')


    



    


def vertical_win_x(board):
    return board[0] == 'X' and board[3] == 'X' and board[6] == 'X'








  

