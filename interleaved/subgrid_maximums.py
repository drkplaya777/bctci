def is_valid(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])


def calculate_subgrid_maximums(grid):
    R = len(grid)
    C = len(grid[0])
    result = [row.copy() for row in grid]
    print(R)
    print(C)
    print(list(range(R)))
    print(list(range(C)))

    for r in range(R, -1, -1):
        for c in range(C, -1, -1):
            if is_valid(grid, r + 1, c):
                result[r][c] = max(result[r][c], result[r + 1][c])
            if is_valid(grid, r, c + 1):
                result[r][c] = max(result[r][c], result[r][c + 1])
    return result


def run_tests():
    tests = [
        # Example from book
        ([[1, 5, 3],
          [4, -1, 0],
          [2, 0, 2]],
         [[5, 5, 3],
          [4, 2, 2],
          [2, 2, 2]]),
        # # Edge case - 1x1 grid
        # ([[5]], [[5]]),
        # # Edge case - single row
        # ([[1, 2, 3]], [[3, 3, 3]]),
        # # Edge case - single column
        # ([[1], [2], [3]], [[3], [3], [3]]),
        # # Edge case - negative numbers
        # ([[-1, -2],
        #   [-3, -4]],
        #  [[-1, -2],
        #   [-3, -4]]),
    ]

    for grid, want in tests:
        got = calculate_subgrid_maximums(grid)
        assert got == want, f"\nsubgrid_maximums({grid}): got: {got}, want: {want}\n"


if __name__ == '__main__':
    run_tests()