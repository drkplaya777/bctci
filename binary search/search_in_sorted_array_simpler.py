def find_through_api(target, fetch):
    def is_before(idx):
        return fetch(idx) != -1 and fetch(idx) < target

    l, r = 0, 1
    # Step 1: Get the rightmost boundary
    while fetch(r) != -1:
        r *= 2

    # Step 2: Binary search
    while r - l > 1:
        mid = (l + r ) // 2
        if is_before(mid):
            l = mid
        else:
            r = mid

    if fetch(l) == target:
        return l
    if fetch(r) == target:
        return r
    return -1