def same_messages(arr):
    p1, p2 = len(arr) - 1, len(arr) - 1
    skip1, skip2 = 0, 0

    while p1 >= 0 and p2 >= 0:
        if arr[p1] > 2:
            p1 -= 1
        elif arr[p1] == 2:
            skip1 += 1
            p1 -= 1
        elif skip1 > 0:
            skip1 -= 1
            p1 -= 1

        elif arr[p2] < 10:
            p2 -= 1
        elif arr[p2] == 12:
            skip2 += 1
            p2 -= 1
        elif skip2 > 0:
            skip2 -= 1
            p2 -= 1
        else:
            if arr[p1] != (arr[p2] - 10):
                return False
            p1 -= 1
            p2 -= 1

    while p1 >= 0:
        if arr[p1] > 2:
            p1 -= 1
        elif arr[p1] == 2:
            skip1 += 1
            p1 -= 1
        elif skip1 > 0:
            skip1 -= 1
            p1 -= 1
        else:
            return False

    while p2 >= 0:
        if arr[p2] < 10:
            p2 -= 1
        elif arr[p2] == 2:
            skip2 += 1
            p2 -= 1
        elif skip2 > 0:
            skip2 -= 1
            p2 -= 1
        else:
            return False

    return True

if __name__ == '__main__':
    print(same_messages([0, 10, 1, 11]))
    print(same_messages([0, 2, 1, 10, 11]))
    print(same_messages([1, 11, 0, 10, 2, 12]))