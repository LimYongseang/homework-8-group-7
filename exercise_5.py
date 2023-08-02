def reverse_ascending(numbers):
    result = []
    start = 0
    for i in range(1, len(numbers)):
        if numbers[i] <= numbers[i - 1]:
            result.extend(numbers[start:i][::-1])
            start = i
    result.extend(numbers[start:][::-1])
    return result
