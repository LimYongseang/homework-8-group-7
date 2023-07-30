


def remove_all_after(numbers, n):
    ...
    return numbers[:numbers.index(n)+1]

a = remove_all_after([1, 2, 3, 4, 5], 4, 5)
print(a)