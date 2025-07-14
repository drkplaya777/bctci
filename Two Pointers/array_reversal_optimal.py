def reverse(arr):
    l, r = 0, len(arr) - 1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    return
if __name__ == '__main__':
    test = ['J', 'e', 'r', 'e', 'm', 'y']
    reverse(test)
    print(test)
