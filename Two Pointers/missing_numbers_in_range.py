def missing_in_range(arr, low, high):
    if not arr:
        return list(range(low, high + 1))
    result = []
    left, right = 0, len(arr) - 1
    while arr[left] < low or arr[right] > high:
        if left < len(arr) and arr[left] < low:
            left += 1
        if right > 0 and arr[right] > high:
            right -= 1

    for number in range(low, high + 1):
        if number != arr[left] and number != arr[right]:
            result.append(number)

    return result

if __name__ == '__main__':
    print(missing_in_range([6, 9, 12, 15, 18], 9, 13))
    print(missing_in_range([], 9, 9))
    print(missing_in_range([6, 7, 8, 9], 7, 8))
