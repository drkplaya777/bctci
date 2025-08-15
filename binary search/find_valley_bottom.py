def is_before(midpoint, value_after):
    return midpoint < value_after


def find_bottom(arr):
    left, right = 0, len(arr) - 1

    while right - left > 1:
        mid = (left + right) // 2

        if is_before(arr[mid], arr[mid + 1]):
            right = mid
        else:
            left = mid

    if arr[left] < arr[right]:
        return arr[left]
    return arr[right]


def run_tests():
    tests = [
        ([6, 5, 4, 7, 9], 4),
        ([5, 6, 7], 5),
        ([7, 6, 5], 5),
        ([2, 1], 1),
        ([3, 2, 4], 2)
    ]

    for arr, want in tests:
        result = find_bottom(arr)
        assert result == want, f"\nfind_bottom({arr}) : got: {result}, want: {want}"
        print(f"\nfind_bottom({arr}): got: {result}")


if __name__ == '__main__':
    run_tests()
