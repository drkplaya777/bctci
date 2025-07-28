def is_valid(chess_board, r, c):
    return 0 <= r < len(chess_board) and 0 <= c < len(chess_board) and chess_board[r][c] != 1


def move_queen(chess_board):
    queens_directions = [
        [-1, 0], [1, 0], [0, -1], [0, 1],
        [-1, -1], [-1, 1], [1, 1], [1, -1]  # diagonals
    ]
    queens = []
    result_board = []

    # Create new board
    num_of_rows = len(chess_board)
    num_of_cols = len(chess_board[0])
    for row_index in range(num_of_rows):
        result_board.append([])
        for _ in range(num_of_cols):
            result_board[row_index].append(0)

    # Find all the queens
    for row_index, row in enumerate(chess_board):
        for col_index, column in enumerate(row):
            if row[col_index] == 1:
                queens.append([row_index, col_index])


    # place queens on new board
    for queen_r, queen_column in queens:
        result_board[queen_r][queen_column] = 1

    # Move queens in all directions
    for queen_r, queen_column in queens:
        for dir_r, dir_c in queens_directions:
            new_r = queen_r + dir_r
            new_c = queen_column + dir_c

            while is_valid(result_board, new_r, new_c):
                result_board[new_r][new_c] = 1
                new_r += dir_r
                new_c += dir_c

    return result_board


if __name__ == '__main__':
    board = [
        [0, 0, 0, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 0, 0, 0],
    ]
    print(move_queen(board))
    board = [[1]]
    print(move_queen(board))
    board = [[0]]
    print(move_queen(board))
    board = [[0, 0], [0, 0]]
    print(move_queen(board))