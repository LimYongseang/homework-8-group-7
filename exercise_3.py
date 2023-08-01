def remove_all_after(numbers, n):
    ...
    
    if n in numbers:
        return numbers[0:numbers.index(n)+1]
    else:
        return numbers
    
a = remove_all_after([1, 2, 3, 4, 5], 3)
print(a)
b = remove_all_after([1, 1, 2, 2, 3, 3], 4)
print (b)
c = remove_all_after([1, 1, 2, 2, 3, 3], 2)
print (c)
d = remove_all_after([1, 2, 3, 4, 5], 3)
print(d)
e = remove_all_after([1, 1, 2, 2, 3, 3], 2)
print (e)
f = remove_all_after([], 0)
print (f)
g = remove_all_after([], 3)
print (g)
h = remove_all_after([1, 2, 3, 4, 5], 6)
print (h)
i =remove_all_after(
        [
            0,
            4,
            5,
            6,
            6,
        ],
        1,
    )
print (h)
print(i)
