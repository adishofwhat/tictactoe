print("---------\n|       |\n|       |\n|       |\n---------")

def print_board():
    print('---------'
          f'\n| {board[0]} {board[1]} {board[2]} |'
          f'\n| {board[3]} {board[4]} {board[5]} |'
          f'\n| {board[6]} {board[7]} {board[8]} |'
          '\n---------')

n = 0

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

i = 1

while True:
    print("Enter the coordinates:")
    indices = input().split()
    n = n + 1
        
    if not ''.join(indices).isnumeric():
        print('You should enter numbers!')
        continue

    x, y = [int(i) for i in indices]
    if any([x > 3, y > 3, x < 1, y < 1]):
        print('Coordinates should be from 1 to 3!')
        continue

    index = (x - 1) + (9 - (3 * y))
    if n == 1:
        if i == 1:
            board[index] = 'X'
            i = i - 1
        else:
            board[index] = 'O'
            i = i + 1
        print_board()
        continue
    else:
        if board[index] != ' ':
            print('This cell is occupied! Choose another one!')
        else:
            if i == 1:
                board[index] = 'X'
                i = i - 1
            else:
                board[index] = 'O'
                i = i + 1
            print_board()
       
    if (board[0] == board[1] and board[1] == board[2]):
        if board[0] != ' ' or board[1] != ' ' or board[2] != ' ':
            print(board[0] + ' wins')
            break
    elif (board[3] == board[4] and board[4] == board[5]):
        if board[3] != ' ' or board[4] != ' ' or board[5] != ' ':
            print(board[3] + " wins")
            break
    elif (board[6] == board[7] and board[7] == board[8]):
        if board[6] != ' ' or board[7] != ' ' or board[8] != ' ':
            print(board[6] + " wins")
            break
    elif (board[0] == board[3] and board[3] == board[6]):
        if board[0] != ' ' or board[3] != ' ' or board[6] != ' ':
            print(board[0] + " wins")
            break
    elif (board[1] == board[4] and board[4] == board[7]):
        if board[1] != ' ' or board[4] != ' ' or board[7] != ' ':
            print(board[1] + " wins")
            break  
    elif (board[2] == board[5] and board[5] == board[8]):
        if board[2] != ' ' or board[5] != ' ' or board[8] != ' ':
            print(board[2] + " wins")
            break
    elif (board[0] == board[4] and board[4] == board[8]):
        if board[0] != ' ' or board[4] != ' ' or board[8] != ' ':
            print(board[0] + " wins") 
            break
    elif (board[2] == board[4] and board[4] == board[6]):
        if board[2] != ' ' or board[4] != ' ' or board[6] != ' ':
            print(board[2] + " wins")
            break
    elif n == 10:
        print("Draw")
        break

               

                          
