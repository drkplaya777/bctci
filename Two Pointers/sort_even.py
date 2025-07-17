def sort_even(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        if arr[left] % 2 == 0:
            left += 1
        elif arr[right] % 2 == 1:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr

if __name__ == '__main__':
    print(sort_even([1,2,3,4]))
    print(sort_even([5, 3, 1, 5]))