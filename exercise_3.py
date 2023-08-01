def remove_all_after(numbers, n):
    if n in numbers:
        return numbers[0 : numbers.index(n) + 1]
    else:
        return numbers
