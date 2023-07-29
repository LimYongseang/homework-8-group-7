def chunking_by(numbers, chunck):
    result = []
    temp = []
    time = 0
    if not numbers or type(chunck) != int:
        return result  
    elif chunck == 0:
        return numbers
    else:
        for number in numbers:
            
            temp.append(number)
            time += 1

            if time == chunck:
                result += [temp]
                temp = []
                time = 0
        result += [temp]
    return result
    

# print(chunking_by([5, 4, 7, 3, 4, 5, 4], 3))
# chunking_by([5, 4, 7, 3, 4, 5, 4], 3) == [[5, 4, 7], [3, 4, 5], [4]]
# chunking_by([3, 4, 5], 1) == [[3], [4], [5]]