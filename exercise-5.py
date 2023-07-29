def reverse_ascending(numbers):
    
    
    for index, number in enumerate(numbers):
        prev_index = 0
        curren = number
        prev_index  = index - 1
            
        while prev_index >= 0 and numbers[prev_index] < curren:
            numbers[prev_index + 1] = numbers[prev_index]
            numbers[prev_index] = curren
            prev_index -= 1
        
    return numbers
    


print(reverse_ascending([5,4,3,2,1,0]))

# list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
# list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]


'''
sort numbers from big to 
'''