is_stolen = lambda t: t >= 3

def find_time_bike_stolen(t1, t2):
    left, right = t1, t2

    while right - left > 1:
        mid = (left + right) // 2
        if not is_stolen(mid):
            left = mid
        else:
            right = mid
    return right

if __name__ == '__main__':
    print(find_time_bike_stolen(1, 5))
