def is_lowercase(c):
    return ord('a') <= ord(c) <= ord('z')

def is_uppercase(c):
    return ord('A') <= ord(c) <= ord('Z')

def is_digit(c):
    return ord('0') <= ord(c) <= ord('9')

def to_uppercase(c):
    if not is_lowercase(c):
       return
    starting_position = ord('a')
    current_char_position = ord(c)
    current_pos_in_alphabet = current_char_position - starting_position
    upper_case_starting_position = ord('A')
    uppercase_conversion_position = upper_case_starting_position + current_pos_in_alphabet

    return chr(uppercase_conversion_position)

def is_alphanumeric(character):
    return is_lowercase(character) or is_uppercase(character) or is_digit(character)

def split(text, splitter):
    """
    Time complexity: O(n) where n is the number of characters in the string
    Space complexity: O(n) where n is the number of characters in the string
    Worst case: O(n)
    Amortized time: O(n)
    """
    if len(text) <= 0:
        return []

    buffer = []
    split_strings = []
    for character in text:
        if character != splitter:
            buffer.append(character)
        else:
            new_string = "".join(buffer)
            split_strings.append(new_string)
            buffer = []

    new_string = "".join(buffer)
    split_strings.append(new_string)
    return split_strings

def join(array, joiner):
    """
    Time complexity: O(n^2) where n is the number of characters in the string
    Space complexity: O(n) where n is the number of characters in the string
    Worst case: O(n)
    Amortized time: O(n)
    """
    size = len(array)
    if size <= 0:
        return ""
    buffer = []
    count = 0
    for word in array:
        for character in word:
            buffer.append(character)
        count += 1
        if count <= size - 1:
            buffer.append(joiner)
    return "".join(buffer)


def index_of(needle, haystack):
    """
    n is the number of letters in needle
    Time complexity: O(n)
    Space complexity: O(1)
    Amortized time: O(n)
    Worst case: O(n)
    """
    if len(needle) <= 0:
        return -1
    count = 0
    for character in needle:
        if character == haystack:
            return count
        count += 1
    return -1

if __name__ == '__main__':
    # print(is_lowercase('a'))
    # print(is_uppercase('b'))
    # print(is_digit('9'))
    # print(is_alphanumeric('3'))
    # print(is_alphanumeric('a'))
    # print(is_alphanumeric('&'))
    # print(to_uppercase('j'))
    # print(to_uppercase('e'))
    # print('4 is not a lowercase number: ', to_uppercase('4'))
    # print('E is not a lowercase number: ', to_uppercase('E'))
    print(split("beekeeper needed", "e"))
    print(split("split by space", " "))
    print(split("/home/./..//Documents/", "/"))
    print(split("", "?"))
    print(join(["join", "by", "space"], " "))
    print(join(["b", "", "k", "", "p", "r n", "", "d", "d!!"], "ee"))
    print(join(['', 'home', '.', '..', '', 'Documents', ''], "/"))
    print(index_of("Beekeeper needed!!", "k"))
    print(index_of("Beekeeper needed!!", "e"))
    print(index_of("split by space", " "))