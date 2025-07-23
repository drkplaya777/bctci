def shift_word(arr, word):
    writer, seeker, current_char = 0, 0, 0
    while seeker < len(arr):
        if current_char < len(word) and arr[seeker] == word[current_char]:
            current_char += 1
            seeker += 1
        else:
            arr[writer] = arr[seeker]
            writer += 1
            seeker += 1
    # the writer ends after the non-sequence
    for char in word:
        arr[writer] = char
        writer += 1

    return arr

if __name__ == '__main__':
    print(shift_word(['s', 'e', 'e', 'k', 'e', 'r', 'a', 'n', 'd', 'w', 'r', 'i', 't', 'e', 'r'], 'edit'))
    print(shift_word(['b', 'a', 'c', 'b'], 'ab'))
    print(shift_word(['b', 'a', 'b', 'c'], 'b'))
    print(shift_word([], []))
    print(shift_word(['a', 'z', 'd'], 'b'))