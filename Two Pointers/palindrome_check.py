def is_palindrome(string: str):
    if not string:
        return True

    first_finger = 0
    second_finger = len(string) - 1
    palindrome = True

    while first_finger < second_finger:
        if string[first_finger] != string[second_finger]:
            return False
        first_finger += 1
        second_finger -= 1

    return palindrome


if __name__ == '__main__':
    print(is_palindrome("level"))
    print(is_palindrome("naan"))
    print(is_palindrome("Jeremy"))
