def sum_subgrid(grid):
    result = [row.copy() for row in grid]
    row_boundary = len(grid) - 1
    col_boundary = len(grid[0]) - 1

    for row_index in range(row_boundary, -1, -1):
        for col_index in range(col_boundary, -1, -1):
            if row_index + 1 > row_boundary:
                one_below = 0
            else:
                one_below = result[row_index + 1][col_index]

            if col_index + 1 > col_boundary:
                one_to_the_right = 0
            else:
                one_to_the_right = result[row_index][col_index + 1]

            if row_index + 1 > row_boundary or col_index + 1 > col_boundary:
                bottom_right = 0
            else:
                bottom_right = result[row_index + 1][col_index + 1]

            result[row_index][col_index] = result[row_index][col_index] + one_below + one_to_the_right - bottom_right

    return result

if __name__ == '__main__':
    grid_of_ints = [[5]]
    print(sum_subgrid(grid_of_ints))
    grid_of_ints = [[1, 2, 3]]
    print(sum_subgrid(grid_of_ints))
    grid_of_ints = [
        [-1, 2, 3],
        [4, 0, 0],
        [-2, 0, 9]
    ]
    print(sum_subgrid(grid_of_ints))
