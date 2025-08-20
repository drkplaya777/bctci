def count_divisible_by_k(arr, target, positive_int):
    def first_is_before(val):
        return val < target

    def second_is_before(val):
        return val <= target

    if len(arr) == 0:
        return True

    left, right = 0, len(arr) - 1
    if arr[left] > target or arr[right] < target:
        return True
    if arr[left] == target:
        first_occurrence = left
    else:
        while right - left > 1:
            mid = (left + right) // 2
            if first_is_before(arr[mid]):
                left = mid
            else:
                right = mid

        first_occurrence = right

    left, right = 0, len(arr) - 1
    if arr[right] == target:
        last_occurrence = right
    else:
        while right - left > 1:
            mid = (left + right) // 2
            if second_is_before(arr[mid]):
                left = mid
            else:
                right = mid

        last_occurrence = left

    count_of_characters = (last_occurrence - first_occurrence) + 1
    return count_of_characters % positive_int == 0
    # if count_of_characters % positive_int == 0:
    #     return True
    # return False

if __name__ == '__main__':
    tests = [
        # Example 1
        ([1, 2, 2, 2, 2, 2, 2, 3], 2, 3, True),
        # Example 2
        ([1, 2, 2, 2, 2, 2, 2, 3], 2, 4, False),
        # Example 3: 0 occurrences, 0 is multiple of any number
        ([1, 2, 2, 2, 2, 2, 2, 3], 4, 3, True),
        # Example 4
        ([1, 1, 2, 2, 2], 1, 3, False),
        # Edge case - empty array
        ([], 1, 2, True),
        # single occurrence, at the start
        ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 1, 1, True),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 1, 2, False),
        # single occurrence, at the end
        ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 19, 1, True),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 19, 2, False),
        # # single occurrence, in the middle
        ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 9, 1, True),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 9, 2, False),
        # # smaller than any elements
        ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 0, 1, True),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 0, 2, True),
        # # larger than any elements
        ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 20, 1, True),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 20, 2, True),
        # # Edge case - every occurrence is target
        ([5, 5, 5, 5, 5], 5, 5, True),
        ([5, 5, 5, 5, 5], 5, 3, False),
    ]

    for array, target, positive, want in tests:
        result = count_divisible_by_k(array, target, positive)
        assert result == want, f"\ncount_divisible_by_k({array, target, positive}) : got {result}, want: {want}"
        print(f"\ncount_divisible_by_k({array, target, positive}): got: {result}")
