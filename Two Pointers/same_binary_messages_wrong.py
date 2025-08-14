def check_message(arr):
    left, right = len(arr) - 1, len(arr) - 1
    left_skip_counter, right_skip_counter = 0, 0

    while left >= 0 and right >= 0:
        if arr[left] not in [0, 1, 2]:
            left -= 1
        if arr[right] not in [10, 11, 12]:
            right -= 1

        if arr[left] == 2:
            left_skip_counter += 1
            left -= 1
        if arr[right] == 12:
            right_skip_counter += 1
            right -= 1

        if left_skip_counter > 0:
            left -= 1
            left_skip_counter -= 1
        if right_skip_counter > 0:
            right -= 1
            right_skip_counter -= 1

        if arr[left] == 1 and arr[right] == 11:
            left -= 1
            right -= 1
        else:
            return False

        if arr[left] == 0 and arr[right] == 10:
            left -= 1
            right -= 1
        else:
            return False

    while right > 0:
        if arr[right] not in [10, 11, 12]:
            right -= 1
        elif arr[right] == 12:
            right_skip_counter += 1
            right -= 1
        elif right_skip_counter > 0:
            right -= 1
            right_skip_counter -= 1
        else:
            right -= 1

    while left > 0:
        if arr[left] not in [0, 1, 2]:
            left -= 1
        elif arr[left] == 2:
            left_skip_counter += 1
            left -= 1
        elif left_skip_counter > 0:
            left -= 1
            left_skip_counter -= 1
        else:
            left -= 1

    return True

if __name__ == '__main__':
    print(check_message([0, 10, 1, 11]))
    print(check_message([0, 2, 1, 10, 11]))
    print(check_message([1, 11, 0, 10, 2, 12]))