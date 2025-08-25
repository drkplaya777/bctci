def fetch(value):
    pass


def search_in_huge_array(target):
    def find_end_of_array():
        starting_position = 1
        current_position = starting_position
        previous_position = starting_position
        possible_boundary = False

        while not possible_boundary:
            if fetch(current_position) == -1:
                possible_boundary = True
            else:
                previous_position = current_position
                current_position *= 2

        def is_before(value):
            return fetch(value) != -1

        left = previous_position
        right = current_position

        while right - left > 1:
            mid = (left + right) // 2
            if is_before(mid):
                left = mid
            else:
                right = mid
        return right - 1

    def binary_search(end_of_array):
        def is_before(val):
            return fetch(val) < target

        if fetch(0) > target or fetch(end_of_array) < target:
            return -1
        elif fetch(0) == target:
            return 0
        elif fetch(end_of_array) == target:
            return end_of_array

        left, right = 0, end_of_array

        while right - left > 1:
            mid = (left + right) // 2
            if is_before(mid):
                left = mid
            else:
                right = mid
        if fetch(right) == target:
            return right
        return -1

    return binary_search(find_end_of_array())

