


board = [" " for i in range(0,9)]


def display_board():
    row1 = '|{}|{}|{}|'.format(board[0],board[1],board[2])
    row2 = '|{}|{}|{}|'.format(board[3],board[4],board[5])
    row3 = '|{}|{}|{}|'.format(board[6],board[7],board[8])
    print(row1)
    print(row2)
    print(row3)





def play_round(player):
    cell = int(input('Your turn, Player {}'.format(player)))
    if board[cell-1] == ' ':
        board[cell-1]=player
    else:
        print('That space is taken! You lost your chance!')    
    
def check_result(player):
    if board[0] == player and board[1] == player and board[2] == player or \
    board[3] == player and board[4] == player and board[5] == player or \
    board[6] == player and board[7] == player and board[8] == player or \
    board[0] == player and board[3] == player and board[6] == player or \
    board[1] == player and board[4] == player and board[7] == player or \
    board[2] == player and board[5] == player and board[8] == player or \
    board[2] == player and board[4] == player and board[6] == player or \
    board[0] == player and board[4] == player and board[8] == player:
        return 'success'
    
    
def draw_result():
    if ' ' not in board:
      return True
           
    
    
player = 'X'
while True:    
    play_round(player)
    display_board()
    if check_result(player) == 'success':
       print('Player {} wins!'.format(player))
       break
    elif draw_result() == True:
        print('It\'s a draw!')
        break
    if player == 'X':
       player = 'O' 
    else:
       player = 'X'
