import string

def is_lowercase(c):
    return ord('a') <= ord(c) <= ord('z')

def is_uppercase(c):
    return ord('A') <= ord(c) <= ord('Z')

def is_space(c):
    return c == " "

def is_punctuation(c):
    return c in string.punctuation

def to_lowercase(c):
    if not is_uppercase(c):
       return
    starting_position = ord('A')
    current_char_position = ord(c)
    current_pos_in_alphabet = current_char_position - starting_position
    lower_case_starting_pos = ord('a')
    lowercase_conversion = lower_case_starting_pos + current_pos_in_alphabet

    return chr(lowercase_conversion)

def is_sentence_a_palindrome(sentence: str) -> bool:
    p1, p2 = 0, len(sentence) - 1
    is_palindrome = True

    while is_palindrome and p1 < p2:
        while is_punctuation(sentence[p1]) or is_space(sentence[p1]):
            p1 += 1
        if is_uppercase(sentence[p1]):
            front_str = to_lowercase(sentence[p1])
        else:
            front_str = sentence[p1]

        while is_punctuation(sentence[p2]) or is_space(sentence[p2]):
            p2 -= 1
        if is_uppercase(sentence[p2]):
            back_str = to_lowercase(sentence[p2])
        else:
            back_str = sentence[p2]

        if front_str != back_str:
            is_palindrome = False

        p1 += 1
        p2 -= 1

    return is_palindrome
