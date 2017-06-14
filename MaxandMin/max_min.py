def find_max_min(argument):
    max = 0
    min = 1000000000 #The assumption is that there's no instance where the least number will be greater than this
    result = []

    for arg in argument:
        if arg > max:
            max = arg
        if arg < min:
            min = arg

    if max == min:
        number = len(argument)
        result.append(number)
    else:
        result.append(min)
        result.append(max)

    return result