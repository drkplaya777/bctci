def two_sum(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        if arr[left] + arr[right] > 0:
            right -= 1
        elif arr[left] + arr[right] < 0:
            left += 1
        else:
            return True
    return False

if __name__ == '__main__':
    print(two_sum([-5, -2, -1, 1, 1, 10]))
    print(two_sum([]))
    print(two_sum([-3, 0, 0, 1, 2]))
    print(two_sum([-5, -3, -1, 0, 2, 4, 6]))