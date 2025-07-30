def is_valid(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])


def track_snow_fox(snow_field):
    row = len(snow_field) - 1
    column = 0
    current_row = len(snow_field) - 1
    while row > 0:
        if snow_field[row][column] == 0 and is_valid(snow_field, row, column + 1):
            column += 1
        else:
            if snow_field[row][column] == 1:
                current_row = row
            row -= 1
            column = 0
    return current_row


if __name__ == '__main__':
    """
    Time complexity: O(n x m) where n represents the number of rows and m represents the number of columns
    Space complexity: O(1), as I use no extra space
    """
    field = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [1, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 1],
    ]
    print(track_snow_fox(field))
    field = [
        [1, 0, 0, 0, 0, 0],
    ]
    print(track_snow_fox(field))
