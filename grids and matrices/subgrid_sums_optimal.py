def backward_sum(grid):
    R,C = len(grid), len(grid[0])
    res = [row.copy() for row in grid]
    for r in range(R - 1, -1, -1):
        for c in range(C - 1, -1, -1):
            if r + 1 < R:
                res[r][c] += res[r + 1][c]
            if c + 1 < C:
                res[r][c] += res[r][c + 1]
            if r + 1 < R and c + 1 < C:
                res[r][c] -= res[r + 1][c + 1]
    return res

if __name__ == '__main__':
    grid_of_ints = [[5]]
    print(backward_sum(grid_of_ints))
    grid_of_ints = [[1, 2, 3]]
    print(backward_sum(grid_of_ints))
    grid_of_ints = [
        [-1, 2, 3],
        [4, 0, 0],
        [-2, 0, 9]
    ]
    print(backward_sum(grid_of_ints))