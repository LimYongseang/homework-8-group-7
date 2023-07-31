


def remove_all_after(numbers, n):
    ...
    # num = n[0]
    return numbers[0:numbers.index(num)+1]

a = remove_all_after([1, 2, 3, 4, 5], [4, 5])
print(a)
b = remove_all_after([1, 1, 2, 2, 3, 3], [2])
print (b)
c = remove_all_after([1, 1, 2, 2, 3, 3], 2)
print (c)