print("This is a Tic Tac Toe Game")
print('-----------------------------')
print()

choices = ['X', 'O']
print()
while True:
    p1 = input("Player 1 - What letter would you like to choose 'X' or 'O' ")
    p2 = ''

    if p1.upper() == 'X':
        p2 = p2 + choices[1]
        print(f'Player two your choice will be {p2}')
        break
    elif p1.upper() == 'O':
        p2 = p2 + choices[0]
        print(f'Player two your choice will be {p2}')
        break
    else:
        print('Enter a letter X or O')
        p1 = input("Player 1 - What letter would you like to choose 'X' or 'O' ")


    




  

