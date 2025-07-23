def swap_prefix_and_suffix(arr):
    left, right = 0, len(arr) - 1
    suffix = int(2 * len(arr) / 3)

    # reverse entire array
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    # reverse suffix
    left = 0
    right = suffix - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    # reverse prefix
    left = suffix
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr

if __name__ == '__main__':
    print(swap_prefix_and_suffix(['b', 'a', 'd', 'r', 'e', 'v', 'i', 'e', 'w']))
    print(swap_prefix_and_suffix([]))

