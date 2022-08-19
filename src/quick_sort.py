# origin = [5, 7, 2, 9, 33, 12, 1, 4, 22, 1, 4, 1]


def partition(array: list, low: int, high: int):
    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i += 1

            # swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # return the position from where partition is done
    return i + 1


def quick_sort_recursive(array, low, high):
    if low < high:
        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pivot = partition(array, low, high)

        # recursive call on the left of pivot
        quick_sort_recursive(array, low, pivot - 1)

        # recursive call on the right of pivot
        quick_sort_recursive(array, pivot + 1, high)


def quick_sort(array):
    return quick_sort_recursive(array, 0, len(array) - 1)


# sorted = quick_sort(origin)

# print(origin)
# print(sorted)
