def positive_sum(arr):
    sum = 0
    for e in arr:
        if e > 0:
            sum += e
    return sum


positive_sum([1, -4, 7, 12])
