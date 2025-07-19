def solution(arr, pivot):
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

if __name__ == '__main__':
    print(solution([1, 7, 2, 3, 3, 5, 3], 4))
    print(solution([5, 2, 1], 3))
    print(solution([1, 7, 2, 3, 3, 5, 3], 3))
    print(solution([], 1))
    print(solution([1], 1))
    print(solution([1, 2], 1))
    print(solution([2, 1], 1))
    print(solution([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 4))