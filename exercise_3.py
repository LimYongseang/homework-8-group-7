def remove_all_after(numbers, n):
    result = []
    for number in numbers:
        result.append(number)
        if number == n:
            break
    return result
