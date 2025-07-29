def is_valid(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 0


def spiral(n):
    val = n * n - 1
    res = [[0] * n for _ in range(n)]
    r, c = n - 1, n - 1
    directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]  # counterclockwise
    current_direction = 0  # start going down
    while val > 0:
        res[r][c] = val
        val -= 1
        if not is_valid(res, r + directions[current_direction][0],
                        c + directions[current_direction][1]):  # can we go in that direction
            current_direction = (current_direction + 1) % 4  # nope, switch directions
        r, c = r + directions[current_direction][0], c + directions[current_direction][1]  # assumes next move is good
    return res


if __name__ == '__main__':
    print(spiral(3))
    print(spiral(5))
