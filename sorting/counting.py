def counting(array, k):
    output = list(array)
    histogram = [0] * k

    for i in array:
        histogram[i] += 1

    index = 0
    pos = 0
    for i in range(0, k):
        for j in range(0, histogram[i]):
            output[index] = pos
            index += 1
        pos += 1
    return output
