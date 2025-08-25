def find_intersecting_intervals(arr1, arr2):
    p1, p2 = 0, 0
    results = []

    while p1 < len(arr1) and p2 < len(arr2):
        # first case: do they end before
        if arr1[p1][1] < arr2[p2][0]:
            p1 += 1
        elif arr2[p2][1] < arr1[p1][0]:
            p2 += 1
        else:
            start_of_intersection = max(arr1[p1][0], arr2[p2][0])
            end_of_intersection = min(arr1[p1][1], arr2[p2][1])

            if start_of_intersection != end_of_intersection:
                results.append([start_of_intersection, end_of_intersection])

            if arr1[p1][1] == arr2[p2][1]:
                p1 += 1
                p2 += 1
            elif arr1[p1][1] < arr2[p2][1]:
                p1 += 1
            else:
                p2 += 1

    return results

