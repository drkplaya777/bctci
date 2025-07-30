def distance_to_river(field):
    row_boundary, column_boundary = len(field), len(field[0])

    def has_footprints(row, column):
        return 0 <= row < row_boundary and 0 <= column < column_boundary and field[row][column] == 1

    current_row, current_column = 0, 0
    # find start of part
    while field[current_row][current_column] != 1:
        current_row += 1
    closet = current_row
    directions = [-1, 0, 1]
    while current_column < column_boundary:
        for dir_r in directions:
            next_row, next_column = current_row + dir_r, current_column + 1
            if has_footprints(next_row, next_column):
                current_row, current_column = next_row, next_column
                closet = min(closet, current_row)
                break
    return closet

if __name__ == '__main__':
    """
    Time complexity: O(n + m) where n represents finding the first paw print and m represents moving around
    Space complexity: O(1), as I use no extra space
    """
    snowfield = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [1, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 1],
    ]
    print(distance_to_river(snowfield))
    snowfield = [
        [1, 0, 0, 0, 0, 0],
    ]
    print(distance_to_river(snowfield))
