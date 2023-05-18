print("This is a Tic Tac Toe Game")
print('-----------------------------')
print()

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


  

