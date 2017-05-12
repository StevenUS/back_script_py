board1 = [
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,1,0,0,0,0],
            [0,1,0,0,0,0],
            [0,1,0,0,0,0],
            [0,1,0,0,0,0]
          ]
board2 = [
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,1,1,1,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0]
          ]

def check_dwn(board, piece, idx1, idx2, direction="a"):
    if idx1+1 < len(board) and idx1+1 > -1 and board[idx1+1][idx2] == piece:
        return 1 + check_dwn(board, piece, idx1+1, idx2)
    return 0
def check_up(board, piece, idx1, idx2):
    if idx1-1 < len(board) and idx1-1 > -1 and board[idx1-1][idx2] == piece:
        return 1 + check_up(board, piece, idx1-1, idx2)
    return 0

up_dwn_total = 1 + check_dwn(board1, 1, 2, 1) + check_up(board1, 1, 2, 1)

print("up dwn: ", up_dwn_total)

def check_right(board, piece, idx1, idx2):
    if idx2+1 < len(board[0]) and board[idx1][idx2+1] == piece:
        return 1 + check_dwn(board, piece, idx1+1, idx2)
    return 0
def check_left(board, piece, idx1, idx2):
    if idx2-1 > -1 and board[idx1][idx2-1] == piece:
        return 1 + check_up(board, piece, idx1-1, idx2)
    return 0

l_r_total = 1 + check_left(board1, 1, 2, 1) + check_right(board1, 1, 2, 1)
print("L R: ", l_r_total)
