def reverse_ascending(numbers):
    for index, number in enumerate(numbers):
        prev_index = 0
        curren = number
        prev_index = index - 1

        while prev_index >= 0 and numbers[prev_index] < curren:
            numbers[prev_index + 1] = numbers[prev_index]
            numbers[prev_index] = curren
            prev_index -= 1

    return numbers
