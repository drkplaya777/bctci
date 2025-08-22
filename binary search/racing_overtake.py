def find_overtake(arr1, arr2):
    def is_before(val):
        return arr1[val] > arr2[val]

    left, right = 0, len(arr1) - 1

    if not is_before(0):
        return left

    if is_before(right):
        return len(arr1)

    while right - left > 1:
        mid = (left + right) // 2
        if is_before(mid):
            left = mid
        else:
            right = mid
    return right

def run_tests():
    tests = [
        ([2, 4, 6, 8, 10], [1, 3, 5, 9, 11], 3),
        ([2, 3, 4, 5, 6], [1, 2, 3, 6, 7], 3),
        ([3, 4, 5], [2, 5, 6], 1),
        ([2, 3, 4], [1, 2, 3], 3)
    ]

    for p1, p2, want in tests:
        result = find_overtake(p1, p2)
        assert result == want, f"\nfind_overtake({p1, p2}) got: {result}, want: {want} \n"
        print(f"\nfind_overtake({p1, p2}) got: {result}")

if __name__ == '__main__':
    run_tests()
