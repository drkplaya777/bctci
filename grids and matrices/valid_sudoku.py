def validate_sodoku(board):
    # Check rows
    for row_index in range(9):
        seen_numbers = {}
        for col_index in range(9):
            if board[row_index][col_index] != 0:
                if board[row_index][col_index] not in seen_numbers:
                    seen_numbers[board[row_index][col_index]] = True
                else:
                    return False

    # Check cols
    for col_index in range(9):
        seen_numbers = {}
        for row_index in range(9):
            if board[row_index][col_index] != 0:
                if board[row_index][col_index] not in seen_numbers:
                    seen_numbers[board[row_index][col_index]] = True
                else:
                    return False

    # check 3x3 grids
    row, col = 0, 0
    starting_positions = [
        [0,0], [0, 3], [0, 6],
        [3,0], [3, 3], [3, 6],
        [6,0], [6, 3], [6, 6]
    ]
    for start_row, start_col in starting_positions:
        seen_numbers = {}
        for row_index in range(start_row, start_row + 3):
            for col_index in range(start_col, start_col + 3):
                if board[row_index][col_index] != 0:
                    if board[row_index][col_index] not in seen_numbers:
                        seen_numbers[board[row_index][col_index]] = True
                    else:
                        return False

    return True

if __name__ == '__main__':
    sudoku_board = [
        [5, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 9, 0, 5, 0, 3, 0, 0],
        [0, 3, 0, 0, 0, 2, 0, 0, 0],
        [8, 0, 0, 7, 0, 0, 0, 0, 9],
        [0, 0, 2, 0, 0, 0, 8, 0, 0],
        [4, 0, 0, 0, 0, 6, 0, 0, 3],
        [0, 0, 0, 3, 0, 0, 0, 4, 0],
        [0, 0, 3, 0, 8, 0, 2, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 7]
    ]
    print(validate_sodoku(sudoku_board))
    sudoku_board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    print(validate_sodoku(sudoku_board))
    sudoku_board = [
        [5, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 9, 0, 5, 0, 3, 0, 0],
        [0, 3, 0, 0, 0, 2, 0, 0, 0],
        [8, 0, 0, 7, 0, 0, 0, 0, 9],
        [0, 0, 2, 0, 0, 0, 8, 0, 0],
        [4, 0, 0, 0, 0, 6, 0, 0, 3],
        [0, 0, 0, 3, 0, 0, 0, 4, 0],
        [0, 0, 3, 0, 8, 0, 7, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 7]
    ]
    print(validate_sodoku(sudoku_board))