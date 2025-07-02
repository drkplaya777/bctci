a = float('inf')
b = float('-inf')

c = 300
d = -300

def compare(x, y):
    print('X is', x)
    print('Y is', y)
    if x > y:
        print("True")
    else:
        print("False")

def three_way_merge(arr1, arr2, arr3):
    p1, p2, p3 = 0, 0, 0
    result = []

    while p1 < len(arr1) or p2 < len(arr2) or p3 < len(arr3):
        min_value = float('inf')
        if p1 < len(arr1):
            min_value = min(min_value, arr1[p1])
        if p2 < len(arr2):
            min_value = min(min_value, arr2[p2])
        if p3 < len(arr3):
            min_value = min(min_value, arr3[p3])

        if p1 < len(arr1) and arr1[p1] == min_value:
            p1 += 1
        if p2 < len(arr2) and arr2[p2] == min_value:
            p2 += 1
        if p3 < len(arr3) and arr3[p3] == min_value:
            p3 += 1

        if not result or result[-1] != min_value:
            result.append(min_value)
    return result

if __name__ == '__main__':
    print(three_way_merge([2, 3, 3, 4, 5, 7], [3, 3, 9], [3, 3, 9]))
    print(three_way_merge([1, 1, 1], [1], [1, 1]))
    print(three_way_merge([1, 2, 3], [], [14, 15]))