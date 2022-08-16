origin = [5, 7, 2, 9, 33, 12, 1, 4, 22, 1, 4, 1]


def sort_bubble(list: list):
    a = list.copy()
    length = len(a)
    for j in range(length):
        for i in range(length - j - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
    return a


b = sort_bubble(origin)

print(origin)
print(b)
