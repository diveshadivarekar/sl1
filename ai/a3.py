import math

AI = 'O'
HUMAN  = 'X'

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ': return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ': return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ': return board[0][0]
    if board[2][0] == board[1][1] == board[0][2] != ' ':return board[2][0]

def check_move(board):
    return any(' ' in row for row in board)

def minimax(board,depth,is_max):
    winner = check_winner(board)
    if winner == AI: return 10 -depth
    if winner == HUMAN: return depth -10
    if not check_move(board):return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = AI
                    best = max(best, minimax(board, depth+1, False))
                    board[i][j] = ' '
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = HUMAN
                    best = min(best, minimax(board, depth+1, True))
                    board[i][j] = ' '
        return best
    
def find_best(board):
    best_val, move = -math.inf, (-1,-1)
    for i in range(3):
        for j in range (3):
            if board[i][j] == ' ':
                board[i][j] = AI
                val = minimax(board, 0, False)
                board[i][j] =' '
                if val > best_val:
                    best_val, move = val, (i,j)
    return move

def draw_board(board):
    for row in board: print(row)

board = [[' ']*3 for _ in range(3)]

while True:
    draw_board(board)
    r = int(input("enter row = "))
    c = int(input("enter column= "))
    if board[r][c] != ' ': 
        print("invalid move ")
        continue
    board[r][c] = HUMAN

    i,j = find_best(board)
    board[i][j] = AI
    if not check_move(board): break

if check_winner(board) == AI:
    print ("ai won")
else:
    print("you won")