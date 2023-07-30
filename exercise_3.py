


def remove_all_after(numbers, n):
    ...
    return numbers[0:numbers.index(n)+1]

a = remove_all_after([1, 2, 3, 4, 5], 3)
print(a)
b = remove_all_after([1, 1, 2, 2, 3, 3], 2)
print (b)