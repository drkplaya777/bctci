def sort_valley_array(arr):
    if len(arr) == 0:
        return []
    left, right = 0, len(arr) - 1
    result = [0]*len(arr)
    i = len(arr) - 1
    while left < right:
        if arr[left] > arr[right]:
            result[i] = arr[left]
            left += 1
            i -= 1
        else:
            result[i] = arr[right]
            right -= 1
            i -= 1
    result[0] = arr[left]
    return result

if __name__ == '__main__':
    print(sort_valley_array([8,4, 2, 6]))
    print(sort_valley_array([]))
    print(sort_valley_array([1, 2]))
    print(sort_valley_array([2, 2, 1, 1]))
