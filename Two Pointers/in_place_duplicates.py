def number_of_uniques(arr):
    writer, seeker = 0, 0
    while seeker < len(arr):
        if seeker == 0 or arr[seeker] != arr[seeker - 1]:
            arr[writer] = arr[seeker]
            writer += 1
            seeker += 1
        else:
            seeker += 1
    return writer

if __name__ == '__main__':
    print(number_of_uniques([1,1,2,2]))
    print(number_of_uniques([]))
    print(number_of_uniques([1, 2, 2, 3, 3, 3, 5]))