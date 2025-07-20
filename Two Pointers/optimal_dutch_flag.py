def sort_colors(arr):
    r_count = sum(1 for character in arr if character == 'R')
    w_count = sum(1 for character in arr if character == 'W')

    index = 0
    for _ in range(r_count):
        arr[index] = 'R'
        index += 1
    for _ in range(w_count):
        arr[index] = 'W'
        index += 1
    while index < len(arr):
        arr[index] = 'B'
        index += 1

    return arr

if __name__ == '__main__':
    print(sort_colors(['R', 'W', 'B', 'B', 'W', 'R', 'W']))
    print(sort_colors(['R', 'R', 'R']))
    print(sort_colors([]))