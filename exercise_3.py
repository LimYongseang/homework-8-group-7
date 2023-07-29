def remove_all_after(numbers, n):
    result = []
    for number in numbers:
        result.append(number)
        if number == n:
            break
    return result

print(remove_all_after([1, 1, 2, 2, 3, 3], 2))
'''
use for loop to to go through each elements in the given list
then append element to the result list
using if to compare with the n if meet return result list
test edge cases'''