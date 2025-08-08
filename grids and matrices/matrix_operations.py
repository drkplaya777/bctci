class Matrix:
    def __init__(self, grid):
        self.matrix = [row.copy() for row in grid]

    def transpose(self):
        for row in range(len(self.matrix)):
            for col in range(row):
                self.matrix[row][col], self.matrix[col][row] = self.matrix[col][row], self.matrix[row][col]

    def reflect_horizontally(self):
        for row in self.matrix:
            row.reverse()

    def reflect_vertically(self):
        self.matrix.reverse()

    def rotate_clockwise(self):
        self.transpose()
        self.reflect_horizontally()

    def rotate_counterclockwise(self):
        self.transpose()
        self.reflect_vertically()


if __name__ == '__main__':
    matrix = Matrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    matrix.transpose()
    print(matrix.matrix)
    matrix = Matrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    matrix.reflect_horizontally()
    print(matrix.matrix)
    matrix = Matrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    matrix.reflect_vertically()
    print(matrix.matrix)
    matrix = Matrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    matrix.rotate_clockwise()
    print(matrix.matrix)
    matrix = Matrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    matrix.rotate_counterclockwise()
    print(matrix.matrix)