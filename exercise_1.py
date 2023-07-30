def replace_last(numbers):
    ...
    if numbers == []:
        return []
    else: 
        new = []
        last_digit = numbers[-1]
        new.append(last_digit)
        for num in numbers[0:len(numbers)-1]:
            new.append(num)
        return new

#psuedo
#create a new list
#input last number first 
#input everthing else afterward in normal order

## test
# numbers = [1, 2, 3, 4, 8]
# print(replace_last([]))
# print(replace_last([1]))
# print(replace_last([1, 2, 3, 4]))
# print(replace_last([2, 3, 4, 1]))
# print(replace_last(numbers))