def missing_numbers(array, low, high):
    p1 = 0
    p2 = low
    result = []

    while p1 < len(array) and p2 <= high:
        if array[p1] < p2:
            p1 += 1
        elif array[p1] == p2:
            p1 += 1
            p2 += 1
        else:
            result.append(p2)
            p2 += 1

    if p2 <= high:
        result.extend(range(p2, high + 1))

    return result

if __name__ == '__main__':
    print(missing_numbers([6, 9, 12, 15, 18], 9, 13))
    print(missing_numbers([], 9, 9))
    print(missing_numbers([6, 7, 8, 9], 7, 8))
    print(missing_numbers([], 1, 5))
    print(missing_numbers([1, 2, 3, 4, 5], 1, 5))