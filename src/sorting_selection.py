origin = [5, 7, 2, 9, 33, 12, 1, 4, 22, 1, 4, 1]


def sort_selection(list: list):
    a = list.copy()
    length = len(a)
    for j in range(length):
        for i in range(j + 1, length):
            if a[j] > a[i]:
                a[i], a[j] = a[j], a[i]
    return a


sorted = sort_selection(origin)

print(origin)
print(sorted)
