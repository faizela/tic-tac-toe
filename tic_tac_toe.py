print("This is a Tic Tac Toe Game")
print('-----------------------------')
board = ['-','-','-',
        '-','-','-',
        '-','-','-']

CurrentPlayer = 'X'
Winner = None
gameRunning = True


   
#  printing the game board
def print_board(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('---------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('---------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


# take player input

def player_input(board):
        try:
            inp = int(input("Enter a number 1-9: "))
            if inp >= 1 and inp <= 9 and board[inp-1] == '-':
                board[inp-1] = CurrentPlayer
            else:
                print("That position is already taken by other player")
        except ValueError:
             print("Enter a valid number from 1 to 9")
     



# Check for win or tie
def check_row(board):
    global Winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        Winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        Winner = board[1]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        Winner = board[6]
        return True

def check_column(board):
    global Winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        Winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        Winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        Winner = board[2]
        return True
    
def check_diagnols(board):
    global Winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        Winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        Winner = board[2]
        return True
    
def check_tie(board):
    if '-' not in board:
        print_board(board)
        print("It is a tie!")
        global gameRunning
        gameRunning = False

def check_win():
    if check_row(board) or check_column(board) or check_diagnols(board):
        print(f'The winner is {Winner}')
        global gameRunning
        gameRunning = False

# switch the player
def switch_player():
    global CurrentPlayer
    if CurrentPlayer == 'X':
        CurrentPlayer = 'O'
    else:
        CurrentPlayer = 'X'


# check for win or tie again
        
while gameRunning:
    print_board(board)
    player_input(board)
    check_win()
    check_tie(board)
    switch_player()
    


                

 










  






















