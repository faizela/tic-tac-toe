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
        gameRunning = False

# switch the player
def switch_player():
    global CurrentPlayer
    if CurrentPlayer == 'X':
        CurrentPlayer = 'O'
    else:
        CurrentPlayer = 'X'
    
    





# def cols_win_x(board):
#     return board[0] == 'X' and board[3] == 'X' and board[6] == 'X' or \
#     board[1] == 'X' and board[4] == 'X' and board[7] == 'X' or \
#     board[2] == 'X' and board[5] == 'X' and board[8] == 'X'

# def rows_win_x(board):
#     return board[0] == 'X' and board[1] == 'X' and board[2] == 'X' or \
#     board[3] == 'X' and board[4] == 'X' and board[5] == 'X' or \
#     board[6] == 'X' and board[7] == 'X' and board[8] == 'X'

# def diagnols_win_x(board):
#     return board[0] == 'X' and board[4] == 'X' and board[8] == 'X' or \
#     board[2] == 'X' and board[4] == 'X' and board[6] == 'X'

# def cols_win_o(board):
#     return board[0] == '' and board[3] == 'O' and board[6] == 'O' or \
#     board[1] == '0' and board[4] == '0' and board[7] == '0' or \
#     board[2] == '0' and board[5] == '0' and board[8] == '0'

# def rows_win_o(board):
#     return board[0] == 'O' and board[1] == 'O' and board[2] == '0' or \
#     board[3] == 'O' and board[4] == 'O' and board[5] == '0' or \
#     board[6] == '0' and board[7] == '0' and board[8] == '0'

# def diagnols_win_o(board):
#     return board[0] == 'O' and board[4] == 'O' and board[8] == 'O' or \
#     board[2] == 'O' and board[4] == 'O' and board[6] == 'O'



        

while gameRunning:#
    print_board(board)
    player_input(board)
    # allowed_nums = [1,2,3,4,5,6,7,8,9]
    # P1_WIN_MSG = 'Player 1 Wins!'
    # P2_WIN_MSG = 'Player 2 Wins!'
    # count =  0 # count variablle to check for '-' used for checking for draw

    # Player one
   

   

    # # Player two 
        # if running:
        #     try:
        #         player_2_int = int(input(f'Player 2 - Where would You like to place your {p2_letter.upper()} in which cell block [1 - 9]? '))
        #         if player_2_int not in allowed_nums:
        #                     print('Enter a valid number from 1 to 9')
        #     except ValueError:
        #         print('Enter a valid number between 1 to 9')
        #     else:
        #         try:
        #             if player_2_int not in allowed_nums:
        #                     print('Enter a valid number from 1 to 9')
        #         except:
        #             print('Enter a valid number between 1 to 9')
        #         else:
        #             for num in allowed_nums:
        #                 if num == player_2_int:
        #                     board[num - 1] = p2_letter.upper()
                                
        #     game_board()
                
        


    # game_board()
    #             if rows_win_x(board) and p1_letter.upper() == 'X':
    #                 running = False
    #                 print(P1_WIN_MSG)

    #             if cols_win_x(board) and p1_letter.upper() == 'X':
    #                 running = False
    #                 print(P1_WIN_MSG)

    #             if diagnols_win_x(board) and p1_letter.upper() == 'X':
    #                 running = False
    #                 print(P1_WIN_MSG)

    #             if rows_win_o(board) and p1_letter.upper() == 'O':
    #                 running = False
    #                 print(P1_WIN_MSG)

    #             if cols_win_o(board) and p1_letter.upper() == 'O':
    #                 running = False
    #                 print(P1_WIN_MSG)

    #             if diagnols_win_o(board) and p1_letter.upper() == 'O':
    #                 running = False
    #                 print(P1_WIN_MSG)
        
    #     for i in range(len(board)):
    #         if running and board[i] != '-':
    #             count += 1
    #         if count == 9:
    #             running = False
    #             print("it's a draw")

                

    
    #     #### player two ####
    #     if running:
    #         try:
    #             player_2_int = int(input(f'Player_2 - Where would You like to place your {p2_letter.upper()} in which cell block [1 - 9]? '))
    #             if player_2_int not in allowed_nums:
    #                 print('Enter a valid number from 1 to 9')
    #         except ValueError:
    #             print('Enter a valid number between 1 to 9')
    #         for num in allowed_nums:
    #             if num == player_2_int:
    #                 board[num - 1] = p2_letter.upper()
    #                 game_board()
    #                 if rows_win_x(board) and p2_letter.upper() == 'X':
    #                     running = False
    #                     print(P2_WIN_MSG)

    #                 if cols_win_x(board) and p2_letter.upper() == 'X':
    #                     running = False
    #                     print(P2_WIN_MSG)

    #                 if diagnols_win_x(board) and p2_letter.upper() == 'X':
    #                     running = False
    #                     print(P2_WIN_MSG)

    #                 if rows_win_o(board) and p2_letter.upper() == '0':
    #                     running = False
    #                     print(P2_WIN_MSG)

    #                 if cols_win_o(board) and p2_letter.upper() == '0':
    #                     running = False
    #                     print(P2_WIN_MSG)
                        
    #                 if diagnols_win_o(board) and p2_letter.upper() == '0':
    #                     running = False            
    #                     print(P2_WIN_MSG)



                

 










  






















