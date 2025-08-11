def binary_search(arr, target):
    # Elements in the array?
    n = len(arr)
    if n == 0:
        return -1
    l, r = 0, n - 1

    # Element in bounds or the first value?
    if arr[l] >= target or arr[r] < target:
        if arr[l] == target:
            return 0
        return -1

    # Calculate midpoint and check for value as long as space exists between pointers
    while r - l > 1:
        midpoint = (r + l) // 2
        if arr[midpoint] < target:
            l = midpoint
        else:
            r = midpoint
    if arr[r] == target:
        return r
    return -1

if __name__ == '__main__':
    print(binary_search([-2, 0, 3, 4, 7, 9, 11], 3))
    print(binary_search([-2, 0, 3, 4, 7, 9, 11], 5))