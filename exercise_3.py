


def remove_all_after(numbers, n):
    ...
    
    if n in numbers:
        return numbers[0:numbers.index(n)+1]
    else:
        return numbers
# a = remove_all_after([1, 2, 3, 4, 5], 4)
# print(a)
# b = remove_all_after([1, 1, 2, 2, 3, 3], 4)
# print (b)
# c = remove_all_after([1, 1, 2, 2, 3, 3], 2)
# print (c)