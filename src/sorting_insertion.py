origin = [5, 7, 2, 9, 33, 12, 1, 4, 22, 1, 4, 1]


def sort_insertion(list: list):
    a = list.copy()
    length = len(a)
    for step in range(1, length):
        key = a[step]
        j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    return a


sorted = sort_insertion(origin)

print(origin)
print(sorted)
