def replace_last(numbers):
    result = []
    if not numbers:
        return result
    last = numbers[-1]
    result.append(last)
    for index, number in enumerate(numbers):
        if number == last:
            pass
        else:
            result.append(number)
    return result
