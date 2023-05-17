print("This is a Tic Tac Toe Game")
print('-----------------------------')
print()
board = '''----|----|----|\n----|----|----|\n----|----|----|'''
print(board)
choices = ['X', 'O']
print()
p1 = input("Player 1 - What letter would you like to choose 'X' or 'O' ")
p2 = ''

### This will need to be refactored later ### 
# to not allow any other input but 'X' and 'O'
# and it also needs to be in a while loop
# till a suitable input is provided
if p1.upper() == 'X':
    p2 = p2 + choices[1]
    print(f'Player two your choice will be {p2}')
else:
    p2 = p2 + choices[0]
    print(f'Player two your choice will be {p2}')

def rows_list():
    board_arr = board.split('\n')
    return board_arr

def row_1():
    r1_str = rows_list()[0]
    r1_dic = {'r1' : r1_str}
    return r1_dic



