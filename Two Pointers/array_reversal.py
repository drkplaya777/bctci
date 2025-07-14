def reverse_array(arr):
    if not arr:
        return []
    p1, p2 = 0, len(arr) - 1
    while p1 < p2:
        temp = arr[p1]
        arr[p1] = arr[p2]
        arr[p2] = temp
        p1 += 1
        p2 -= 1
    return arr

if __name__ == '__main__':
    print(reverse_array(['J', 'e', 'r', 'e', 'm', 'y']))
    assert reverse_array(['J', 'e', 'r', 'e', 'm', 'y']) == ['y', 'm', 'e', 'r', 'e', 'J']