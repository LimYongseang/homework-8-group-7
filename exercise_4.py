def chunking_by(numbers, chunck):
    result = []
    temp = []
    time = 0
    if not numbers:
        return result  
    elif chunck == 0 or type(chunck) != int:
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
    

