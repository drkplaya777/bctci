def move_every_smaller_before_larger(arr, pivot):
    left, right = 0, len(arr) - 1
    while left < right:
        if arr[left] <= pivot:
            left += 1
        elif arr[right] > pivot:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr

def find_starting_place_of_larger_than_pivot(arr, pivot):
    left, boundary = 0, 0
    while boundary < len(arr) and arr[boundary] <= pivot:
        boundary += 1

    return boundary

def move_less_than_before_pivot(arr, boundary, pivot):
    left, right = 0, boundary - 1
    while left < right:
        if arr[left] < pivot:
            left += 1
        elif arr[right] == pivot:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr

def partition_quicksort(arr, pivot):
    small_before_large = move_every_smaller_before_larger(arr, pivot)
    boundary = find_starting_place_of_larger_than_pivot(small_before_large, pivot)
    sorted_values = move_less_than_before_pivot(small_before_large, boundary, pivot)

    return sorted_values

if __name__ == '__main__':
    print(partition_quicksort([1, 7, 2, 3, 3, 5, 3], 4))
    print(partition_quicksort([5, 2, 1], 3))
    print(partition_quicksort([1, 7, 2, 3, 3, 5, 3], 3))
    print(partition_quicksort([], 1))
    print(partition_quicksort([1], 1))
    print(partition_quicksort([1, 2], 1))
    print(partition_quicksort([2, 1], 1))
    print(partition_quicksort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 4))
