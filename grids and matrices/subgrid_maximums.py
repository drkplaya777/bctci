def is_valid(board, r, c):
    return 0 <= r < len(board) and 0 <= c < len(board[0])


def find_max(grid):
    new_grid = [row.copy() for row in grid]
    R = len(grid) - 1
    C = len(grid[0]) - 1

    for row in range(R, -1, -1):
        for col in range(C, -1, -1):
            current_max = new_grid[row][col]
            one_row_down, one_col_down = row + 1, col
            one_row_to_right, one_col_to_right = row, col + 1

            if is_valid(grid, one_row_down, one_col_down):
                current_max = max(current_max, new_grid[one_row_down][one_col_down])

            if is_valid(grid, one_row_to_right, one_col_to_right):
                current_max = max(current_max, new_grid[one_row_to_right][one_col_to_right])

            new_grid[row][col] = current_max
    return new_grid


if __name__ == '__main__':
    grid_of_ints = [
        [1, 5, 3],
        [4, -1, 0],
        [2, 0, 2]
    ]
    print(find_max(grid_of_ints))
    grid_of_ints = [[5]]
    print(find_max(grid_of_ints))
    grid_of_ints = [[1, 2, 3]]
    print(find_max(grid_of_ints))
