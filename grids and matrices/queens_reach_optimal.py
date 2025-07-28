def safe_cells(board):
    n = len(board)
    res = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if board[r][c] == 1:
                res[r][c] = 1
                mark_reachable_cells(board, r, c, res)
    return res

def mark_reachable_cells(board, r, c, result):
    directions = [
        [-1, 0], [1, 0], [0, -1], [0, 1], # up/down; left/right
        [-1, -1], [-1, 1], [1, -1], [1, 1] # diagonals
    ]
    for dir_r, dir_c in directions:
        new_r, new_c = r + dir_r, c + dir_c
        while is_valid(board, new_r, new_c):
            result[new_r][new_c] = 1
            new_r += dir_r
            new_c += dir_c

def is_valid(board, r, c):
    return 0 <= r < len(board) and 0 <= c < len(board) and board[r][c] != 1

if __name__ == '__main__':
    chess_board = [
        [0, 0, 0, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 0, 0, 0],
    ]
    print(safe_cells(chess_board))
    chess_board = [[1]]
    print(safe_cells(chess_board))
    chess_board = [[0]]
    print(safe_cells(chess_board))
    chess_board = [[0, 0], [0, 0]]
    print(safe_cells(chess_board))