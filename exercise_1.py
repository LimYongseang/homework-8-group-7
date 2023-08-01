def replace_last(numbers):
    ...
    if numbers == []:
        return []
    else:
        new = []
        last_digit = numbers[-1]
        new.append(last_digit)
        for num in numbers[0 : len(numbers) - 1]:
            new.append(num)
        return new
