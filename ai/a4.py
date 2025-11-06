import matplotlib.pyplot as plt
import numpy as np

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    for i, j in zip(range(row-1,-1,-1), range(col-1,-1,-1)):
        if board[i][j] == 1:
            return False
        
    for i, j in zip(range(row+1, n), range(col-1,-1,-1)):
        if board[i][j] == 1:
            return False
        
    return True 

def solve (board, col, n):
    if col == n:
        return True
    
    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve(board , col+1, n):
                return True
            board[row][col] = 0

    return False

def draw_board(board):
    n = len(board)
    board_pattern = np.zeros((n,n))
    board_pattern[1::2, ::2] = 1
    board_pattern[::2, 1::2] = 1 

    fig ,ax = plt.subplots()
    ax.imshow(board_pattern, cmap ='grey')
    for r in range(n):
        for c in range(n):
            if board[r][c] == 1:
                ax.text(r,c,"Q", color= 'red')
    plt.show()

n=8
board = [[0]*n for _ in range(n)]
solve(board, 0,n)
draw_board(board)