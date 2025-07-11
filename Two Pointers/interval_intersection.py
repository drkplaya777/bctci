# Assumes that int1 and int2 overlap
def get_intersection(int1, int2):
    overlap_start = max(int1[0], int2[0])
    overlap_end = min(int1[1], int2[1])
    return [overlap_start, overlap_end]

def interval_intersection(arr1, arr2):
    p1, p2 = 0, 0
    n1, n2 = len(arr1), len(arr2)
    result = []
    while p1 < n1 and p2 < n2:
        int1 = arr1[p1]
        int2 = arr2[p2]
        if int1[1] < int2[0]:
            p1 += 1
        elif int2[1] < int1[0]:
            p2 += 1
        else:
            result.append(get_intersection(int1, int2))
            if int1[1] < int2[1]:
                p1 += 1
            else:
                p2 += 1
    return result

if __name__ == '__main__':
    print(interval_intersection([[0, 1], [4, 6], [7, 8]], [[2,3], [5, 9], [10, 11]]))
    print(interval_intersection([[2, 4], [5, 8]], [[3,3], [4,7]]))
    """
    2,4 5,8
        p
    3,3 4,7
        p
    """
