def reverse_case_match(string: str):
    left = 0
    right = len(string) - 1

    while left < len(string) and right >= 0:
        if string[left].isalpha() and not string[left].islower():
            left += 1
        elif string[right].isalpha() and not string[right].isupper():
            right -= 1
        else:
            if string[left].lower() != string[right].lower():
                return False
            left += 1
            right -= 1
    return True

if __name__ == '__main__':
    print(reverse_case_match("haDrRAHd"))
    print(reverse_case_match("harHrARd"))
    print(reverse_case_match(""))
    print(reverse_case_match("9haDrRAHd9"))