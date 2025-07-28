def is_valid(room, r, c):
    return 0 <= r < len(room) and 0 <= c < len(room) and room[r][c] != 1


def move_piece(grid, piece, r, c):
    moves = []
    kings_directions = [
        [-1, 0], [1, 0], [0, -1], [0, 1],
        [-1, -1], [-1, 1], [1, 1], [1, -1]  # diagonals
    ]
    knight_directions = [
        [-2, -1], [-2, 1],  # Jump two down
        [-1, -2], [-1, 2],
        [1, -2], [1, 2],
        [2, -1], [2, 1]
    ]
    if piece.lower() == 'king' or piece.lower() == 'queen':
        directions = kings_directions
    else:
        directions = knight_directions

    for dir_r, dir_c in directions:
        new_r = r + dir_r
        new_c = c + dir_c
        if piece.lower == 'queen':
            while is_valid(grid, new_r, new_c):
                moves.append([new_r, new_c])
                new_r += dir_r
                new_c += dir_c
        elif is_valid(grid, new_r, new_c):
            moves.append([new_r, new_c])

    return moves


if __name__ == '__main__':
    board = [
        [0, 0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 1, 0, 1, 1, 0],
        [1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0]
    ]
    print(move_piece(board, 'king', 3, 5))
    print(move_piece(board, 'knight', 4, 3))
    print(move_piece(board, 'queen', 4, 4))
