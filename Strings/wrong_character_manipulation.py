def is_alphanumeric(character):
    if is_lowercase(character):
        return "lowercase"
    elif is_uppercase(character):
        return "uppercase"
    elif is_digit(character):
        return "digit"

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

if __name__ == '__main__':
    print(is_lowercase('a'))
    print(is_uppercase('b'))
    print(is_digit('9'))
    print(is_alphanumeric('3'))
    print(is_alphanumeric('a'))
    print(is_alphanumeric('B'))
    print(to_uppercase('j'))
    print(to_uppercase('e'))
    print('4 is not a lowercase number: ', to_uppercase('4'))
    print('E is not a lowercase number: ', to_uppercase('E'))
