# origin = [5, 7, 2, 9, 33, 12, 1, 4, 22, 1, 4, 1]


def merge(left: list, right: list) -> list:
    len_left = len(left)
    if len_left == 0:
        return right

    len_right = len(right)
    if len_right == 0:
        return left

    full_len = len_left + len_right

    result = []
    index_left = 0
    index_right = 0

    # print(left, right)

    # Go through both arrays until all the elements
    # make it into the resultant array
    while len(result) < full_len:
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        # If you reach the end of either array, then you can
        # add the remaining elements from the other array to
        # the result and break the loop
        if index_left == len_left:
            result += right[index_right:]
            break

        if index_right == len_right:
            result += left[index_left:]
            break

    return result


def merge_sort(a: list):
    # a = list.copy()
    length = len(a)

    # exit from recurse
    if length < 2:
        return a

    midpoint = length // 2

    left = merge_sort(a[:midpoint])
    right = merge_sort(a[midpoint:])

    # print("LR", length, midpoint, left, right)

    return merge(left, right)


# sorted = merge_sort(origin)

# print(origin)
# print(sorted)
