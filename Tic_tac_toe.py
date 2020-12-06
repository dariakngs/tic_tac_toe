current_player = 1
player_1 = 1
player_2 = 2
board = [
    [0, 0, 0], 
    [0, 0, 0],
    [0, 0, 0],
]

def print_board():
    print('   0  1  2') 
    for idx, row in enumerate(board):
        print(idx , row)

def make_turn():
    turn = input("Pick row and column e.g. 23: ")
    return int(turn[0]), int(turn[1])

def save_turn(turn, player):
    if board[turn[0]][turn[1]] == 0:
        board[turn[0]][turn[1]] = player
        return True
    else:
        print('Field is already taken!')
        return False

def check_win(player):
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        return True
    elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
        return True
    elif board[2][0] == player and board[2][1] == player and board[2][2] == player:
        return True

    elif board[0][0] == player and board[1][0] == player and board[2][0] == player:
        return True
    elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
        return True
    elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
        return True

    elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    elif board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return True

def is_full():
    for row in board:
        for field in row:
            if field == 0:
                return False
    return True

while not is_full():
    print_board()
    print('Now is turn of player: ', current_player)
    if not save_turn(make_turn(), current_player):
        continue
    if check_win(current_player):
        print('Player ', current_player, 'WON!')
        break
    current_player = player_1 if current_player == player_2 else player_2
		