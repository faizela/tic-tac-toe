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

def rows_dict():
    rows_dic = {}
    count = 0
    board_arr = board.split('\n')
    for row in board_arr:
        rows_dic[f'R{1 + count}'] = row
        count += 1

    return rows_dic


# 

# def row_1():
#     r1_str = rows_list()[0]
#     r1_dic = {'r1' : r1_str}
#     return r1_dic

# def row_1_cells():
#     r1_dic = row_1()
#     r1_str = r1_dic['r1']
#     return r1_str.split('|')

  

