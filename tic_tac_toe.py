print("This is a Tic Tac Toe Game")
print('-----------------------------')
print()

board = '''----|----|----|\n----|----|----|\n----|----|----|'''
choices = ['X', 'O']
p1 = input("Player 1 - What letter would you like to choose 'X' or 'O' ")
p2 = ''

if p1.upper() == 'X':
    p2 = p2 + choices[1]
    print(f'Player two your choice will be {p2}')
else:
    p2 = p2 + choices[0]
    print(f'Player two your choice will be {p2}')



