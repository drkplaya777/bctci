def merge_arrays(arr1, arr2):
    left, right = 0, 0
    merged_array = []

    while left < len(arr1) and right < len(arr2):
        if arr1[left] < arr2[right]:
            merged_array.append(arr1[left])
            left += 1
        elif arr2[right] < arr1[left]:
            merged_array.append(arr2[right])
            right += 1
        else:
            merged_array.append(arr1[left])
            merged_array.append(arr2[right])
            left += 1
            right += 1

    while left < len(arr1):
        merged_array.append(arr1[left])
        left += 1
    while right < len(arr2):
        merged_array.append(arr2[right])
        right += 1

    return merged_array


if __name__ == '__main__':
    """
    1 3 4 5  2 4 4
          l
                   r
    """
    print(merge_arrays([1, 3, 4, 5], [2, 4, 4]))
    print(merge_arrays([-1], []))
    print(merge_arrays([1, 3, 4, 5], [2, 4, 5, 6]))
    print(merge_arrays([], [1, 2, 3]))
    print(merge_arrays([1, 1, 1, 1], [1, 1, 1]))
