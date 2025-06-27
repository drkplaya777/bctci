

def two_sum(arr):
    left, right = 0, len(arr) - 1

    while left < len(arr) and right >= 0:
        if left == right:
            left += 1
            right = len(arr) - 1
        if arr[left] + arr[right] != 0:
            right -= 1
        else:
            return True
    return False

if __name__ == '__main__':
    """
    -3 0 1 2
             l
           r
    """
    print(two_sum([-5, -2, -1, 1, 1, 10]))
    print(two_sum([0, 1, 2]))
    print(two_sum([-5, -3, -1, 0, 2, 4, 6]))
    print(two_sum([]))