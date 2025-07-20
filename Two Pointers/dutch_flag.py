def fly_dutch_flag(arr):
    left, right = 0, len(arr) - 1
    # Put all R and W before B
    while left < right:
        if arr[left] == 'R' or arr[left] == 'W':
            left += 1
        elif arr[right] == 'B':
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    # find where B starts
    boundary = 0
    while boundary < len(arr) and (arr[boundary] == 'R' or arr[boundary] == 'W'):
        boundary += 1

    # Put all R before all W
    left, right = 0, boundary - 1
    while left < right:
        if arr[left] == 'R':
            left += 1
        elif arr[right] == 'W':
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr

if __name__ == '__main__':
    print(fly_dutch_flag(['R', 'W', 'B', 'B', 'W', 'R', 'W']))
    print(fly_dutch_flag(['R', 'R', 'R']))
    print(fly_dutch_flag([]))