def common_elements(arr1, arr2):
    p1, p2 = 0, 0
    res = []
    while p1< len(arr1) and p2 < len(arr2):
        if arr1[p1] == arr2[p2]:
            res.append(arr1[p1])
            p1 += 1
            p2 += 1
        elif arr1[p1] < arr2[p2]:
            p1 += 1
        else:
            p2 += 1
    return res

if __name__ == '__main__':
    print(common_elements([1,2,3], [1,3,5]))
    print(common_elements([1, 1, 1], [1, 1]))
    print(common_elements([13, 21, 35], [12, 35, 53]))
    print(common_elements([11, 78, 125], [10, 78, 125]))