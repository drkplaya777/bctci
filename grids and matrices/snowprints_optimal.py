def distance_to_river(field):
    R, C = len(field), len(field[0])
    def has_footprints(r, c):
        return 0 <= r < R and 0 <= c < C and field[r][c] == 1
    r, c = 0, 0
    while field[r][c] != 1:
        r += 1
    closet = r
    directions_row = [-1, 0, 1]
    while c < C:
        for dir_r in directions_row:
            new_r, new_c = r + dir_r, c + 1
            if has_footprints(new_r, new_c):
                r, c = new_r, new_c
                closet = min(closet, r)
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
