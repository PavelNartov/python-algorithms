origin = [5, 7, 2, 9, 33, 12, 1, 4, 22, 1, 4, 1]


def counting_sort(array):
    size = len(array)

    # initialize output array with all zeros
    output = [0] * size

    maximum = max(array) + 1

    # initialize count array with all zeros
    count = [0] * maximum

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, maximum):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    # for i in range(0, size):
    #     array[i] = output[i]

    return output


sorted = counting_sort(origin)

print(origin)
print(sorted)
